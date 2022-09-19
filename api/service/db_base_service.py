from flask import jsonify, abort
from sqlalchemy.exc import IntegrityError, DataError
from psycopg2 import errorcodes as pg_errorcodes
from api.model import db


class DbBaseService():
    __unique_name__ = 'name'

    def __init__(self, model, schema):
        self._model = model
        self._schema = schema()
        self._schema_many = schema(many=True)

    def get(self, id):
        item = self._model.query.get_or_404(id,
            description=f'There is no {self._model.__name__} with id {id}')
        return jsonify(self._schema.dump(item))

    def get_all(self):
        items = self._model.query.all()
        return jsonify(self._schema_many.dump(items))

    def create(self, body):
        try:
            new_item = self._model(**body)
            db.session.add(new_item)
            db.session.commit()
        except KeyError as exc:
            abort(400, f"{exc}")
        except IntegrityError as exc:
            db.session.rollback()
            description = f'Incorrect data parameter {exc}, pgcode: {exc.__cause__.pgcode}!'
            if exc.__cause__.pgcode == \
                pg_errorcodes.UNIQUE_VIOLATION:
                description = f'The {self._model.__name__} of name ' \
                    f'{body.get(self.__unique_name__)} already exists!'
            if exc.__cause__.pgcode == \
                pg_errorcodes.NOT_NULL_VIOLATION:
                description = f'Cannot handle null value for parameters!'
            abort(400, description)
        except DataError as exc:
            abort(400, f'Incorrect representation for parameter!')
        except TypeError as exc:
            abort(400, f"{exc}")
        return f'{self._model.__name__} created.'


class DbChildBaseService(DbBaseService):
    def __init__(self, model, schema, model_parent, parent_id_name):
        super().__init__(model, schema)
        self._model_parent = model_parent
        self._parent_id_name = parent_id_name

    def _check_for_master_id(self, id):
        self._model_parent.query.get_or_404(id,
            description=f'There is no {self._model_parent.__name__} '
                        f'with id {id}.'
        )

    def get_for_parent_id(self, id):
        self._check_for_master_id(id)
        items = self._model.query.filter_by(**{self._parent_id_name: id}).all()
        return jsonify(self._schema_many.dump(items))

    def create(self, body, id):
        self._check_for_master_id(id)
        body[self._parent_id_name] = id
        return super().create(body)
