## Frontend Architecture Design Record

This file serves as the "how" and "why" of the implementation for the frontend.

---

## Frontend:

 - ### Tech Stack:
    - Typecript
      - Industry standard and used at Tails.
      - More complex than regular JS but more safe.
   - Vue
      - Industry standard, used at Tails
 - ### Software Design Philosophy:
    - DDD
      - Offers good separation of UI, Infrastructure, domain logic, application logic
 - ### Testing:
    - Vitest
      - Popular choice and used at Tails

---

### Alternative Considerations:

 - ### Tech Stack:
   - Angular
      - Prior experience but not aligned with Tails

### Key Domains:

- UI
   - User experience is key.
   - Should be component-based.
- Application
   - This layer will orchestrate functionality requested by the UI.
- Domain
   - Whule this will be fairly lean, it will contain relevant business logic for the frontend.
- Infrastructure
   - Responsible for communication with the backend.

### Application Folder Structure

- `ui/`
   - `components/` 
      - (Contains components for the frontend)
   - `pages/`
      - `homepage/`
         - (Contains the search bar and list of stores)
- `application/`
   - `services`
      - (Use DTO's and interfaces to build up responses)
   - `dtos`
      - (contains response and request DTO's)
- `domain/`
   - `value-objects/` 
      - (Business logic)
   - `services/` 
      - (functions that return business logic)
   - `interfaces/`
      - (abstract methods which are implemented in infra layer)
- `infrastructure/`
   - `repositories/` 
      - (code regarding requests to the backend)

### Application Flow:



### Containerisation:
- Docker will be used for the frontend, one container will suffice here similarly to the backend, a network will need to be constructed to link both containers together
   
