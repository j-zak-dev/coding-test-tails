## Backend Architecture Design Record

This file serves as the "how" and "why" of the implementation for the backend

---

## Backend:

 - ### Tech stack:
    - Python 
      - Aligns with chosen workplace language
      - Good personal experience with the language itself

    - FastAPI
      - Suggested in the project description
      - Aligns with workplace
      - Quick and easy to get started

    - Entrypoints
      - REST
         - Accepted industry standard
      - JSON payloads
         - Prior experience with JSON
         - Industry standard
 - ### Software Design Philosophy:
    - Domain Driven Design
      - Aligns With workplace
      - Improving understanding and skills in this area
      - Clean separation of logic 
- ### Storage:
   - File based
      - Simple application with no need for SQL-based storage
      - Simple and fast to implement
- ### Testing:
   - Pytest
      - Simple testing library
      - Aligns with chosen language (Python)


## Alternative considerations:

### Tech Stack: 
- Typescript:
   - Not entirely aligned with Tails backend implementations
   - Will use this for the frontend
- ExpressJS
   - Prior experience but does not align with what the company uses
   - Prefer to work in Python with FastAPI

### Storage:
- Postgres Database
   - Common industry standard but too advanced for this project.
- Firebase
   - Good prior experience and NoSQL but requires substantial setup.

---

### DDD Backend Architecture Diagram

```Mermaid
flowchart TB;

   Entrypoint --> Application --> Domain --> Infrastructure;

```

Due to the simplicity of the overall application, we only require four main domains:

- Entrypoints
   - Accepts requests
   - Returns responses
   - Contains its own DTO's
- Application
   - Heavy lifting and orchestration
   - Depends on the domain layer for business logic and communication with infrastructure layer
   - Contains its own response/request DTO's
- Domain
   - Business logic for the application
   - Contains value objects
   - Contains abstract methods implemented by infrastructure layer
- Infrastructure
   - Functions related to returning data
   - Storage of data itself

---

### Application Flow:

```Mermaid

flowchart TB;

1[Entrypoint layer receives a request from the frontend]

2[Entrypoint layer uses an interface in the application layer to call an abstract method in the application layer]

3[Application layer defines the method called by entrypoints layer and  can call on the domain layer method to compute the request. It can also call the infrastructure layer via an interface contained in the domain layer.]

4[Domain layer contains methods that the application layer calls. It also contains interfaces implemented in infrastructure layer.]

5[The response travels back up the chain of layers, going from infra to application and finally entrypoints, at which point it is returned to the frontend]

1 --> 2
2 --> 3
3 --> 4
4 --> 5

```
---

### Application Folder Structure:


- `Entrypoints/`
   - `api/` 
      - (contains REST entrypoint definitions)
- `Application/`
   - `services/`
      - (implements interfaces and DTOs to build up responses)
   - `dtos/` 
      - (Request and response models)
- `Domain/`
   - `value-objects/` 
      - (Business logic)
   - `aggregates/`
      - (implements value objects)
   - `services/` 
      - (implementation of methods called by application)
   - `interfaces/`
      - (Abstract methods implemented in infrastructure layer)
- `Infrastructure/`
   - `repositories/` 
      - (code regarding the return of data)
   - `stores.json`
      - (data store)
- `tests/`
   - `unit/`
- `configs/`
   - `lint.yaml` 
      - (check code before commit)
- `Makefile`
   - (For running commands)
---

### Gherkin Syntax Flow:

 - GIVEN the frontend landing page is loaded.
 - WHEN the backend receives the GET request.
 - THEN the entrypoint layer will use the application layer to get all postcodes using the domain layer interface, which is implemented by infrastructure layer and returns in alphabetical order (additional requirement).

 ```mermaid
   flowchart LR;

   1[Entrypoint calls application function]
   2[Application uses injected interface from domain]
   3[Infrastructure implements abstract method and builds query and returns response]
   4[Applicationlayer builds response for entrypoint layer]
   5[Entrypoint layer returns response to frontend]

   1 --> 2
   2 --> 3
   3 --> 4
   4 --> 5
 ```
---
 - GIVEN a search request is sent.
 - WHEN the entrypoint layer receives the request.
 - THEN the entrypoint layer will use the application layer to get all postcodes using the domain layer interface, which is implemented by infrastructure layer and returns in alphabetical order (additional requirement).


  ```mermaid
   flowchart LR;

   1[Entrypoint calls application function]
   2[Application uses injected interface from domain]
   3[Infrastructure implements abstract method and builds query and returns response]
   4[Applicationlayer builds response for entrypoint layer]
   5[Entrypoint layer returns response to frontend]

   1 --> 2
   2 --> 3
   3 --> 4
   4 --> 5
 ```
---
 - GIVEN a healthcheck request is sent.
 - WHEN the entrypoint layer receives the request.
 - THEN the entrypoint layer will return a simple healthcheck response.

 ```mermaid
   flowchart LR;

   1[Entrypoint layer receives a healthcheck request]
   2[Entrypoint layer returns healthcheck response]

   1 --> 2

 ```
### Domain Aggregates

 - Store
   - StoreName
   - Postcode
   - LatAndLong

### Domain Value Objects
 - Storename: string 
 - Postcode: string
 - LatAndLong: list[string]

### Containerisation

Docker will be use to containerise and run the backend. Since this is a simple implementation, one container running all the backend code will suffice. A network will need to be created to link the backend and frontend containers together. 





