## API Architecture Design Record

This file serves as the "how" and "why" of the implementation for the API.

---

### Entrypoints:

- GET `/postcodes`
    - Returns all postcodes for testing purposes
- GET `/search`
    - Returns a list of postcodes that match a search term
- GET `/all-product-data`
    - A general endpoint for getting all the info about all products
- GET `/healthcheck`
    - Standard healthcheck for early API testing

---

### Reasoning:

We do not implement a full CRUD layout due to it not being necesary as per the PRD.

The main functionalities are: 

- Searching stores
- Getting in-depth data from Postcodes.io

Some additional endpoints are supplied for developers to test functionality of the application. 
