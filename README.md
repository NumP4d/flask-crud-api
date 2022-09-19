# webinterpret-task

## Starting up environment

Run the services using docker compose:

`docker compose up --build`

optionally in detached mode:

`docker compose up --build -d`

## API Endpoints

### Home API:

`http://localhost:8000/`

### Seller endpoints:

`http://localhost:8000/seller`

Methods: GET and POST

`http://localhost:8000/seller/<seller_id>`

Methods: GET

### Product endpoints

`http://localhost:8000/product/<seller_id>`

Methods: GET and POST

### Transaction endpoints

`http://localhost:8000/transaction/<product_id>`

Methods: GET and POST
