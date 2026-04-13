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
   - TDD/BDD (lite)
      - Since the frontend contains a lot of functionality, BDD allows for outlining this functionality ready for implementation using the Gherkin syntax. While this is not a full implementation of BDD, at the very least it contains the same spirit.
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
      - (Use DTO's and interfaces to build up requests/responses)
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
- `tests/`
   - `unit/`
- `configs/`
   - `lint.yaml`
      - (lint checking before commit)
- `Makefile`

### Application Wireframes:

The wireframe diagrams below showcase 2 main states within the program. The first shows the search bar closed and some initial stores loaded. This list of stores will be scrollable and dynamically generated based on the search term searched. The second wireframe depicts the dropdown list which is also dynamically generated as a result of typing in the search bar. The main list of stores should update once the user searches a term.

![wireframe](/docs/coding%20test%20wireframe.drawio.svg)

### User Stories (Gherkin Syntax)

- ### Landing page:

   - GIVEN a user enters the landing page.
   - WHEN the landing page loads.
   - THEN the search bar will be visible at the top of the page.
---
   - GIVEN a user enters the landing page
   - WHEN the landing page loads
   - THEN the initial list of stores will have some data visible.
---
   - GIVEN a user clicks on the search bar.
   - WHEN the user starts typing words.
   - THEN the type ahead feature will suggest what next letters the user can type.
---
   - GIVEN a user clicks on the search bar.
   - WHEN the user starts typing words.
   - THEN the search bar dropdown list will regenerate with each letter typed and show relevant suggestions.
---
   - GIVEN a user clicks on the search bar.
   - WHEN the user starts typing words.
   - AND the user selects a result.
   - THEN the dropdown list will dissapear, the search bar clears and the main list of stores updates to show relevant results.
---
   - GIVEN a user clicks on the search bar.
   - WHEN the user starts typing words.
   - AND the user hits search but does not select a valid option.
   - THEN the dropdown list will dissapear, the search bar clears and the main list of stores updates to show relevant results which match the words entered.
---
   - GIVEN a user is at the top of the page.
   - WHEN the user scroll down to view more stores in the main store list.
   - THEN aside from the first three results, more results will be lazy loaded upon scrolling further.
---
   - GIVEN a user selects the option to search by postcode
   - WHEN the user begins typing a valid postcode
   - THEN hinting should appear, and functionality should remain the same as for searching by name

### Containerisation:
- Docker will be used for the frontend, one container will suffice here similarly to the backend, a network will need to be constructed to link both containers together.
   
