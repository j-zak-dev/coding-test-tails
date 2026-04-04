## Coding test project requirements document

This document serves as the main source of requirements for the project. It is the first document which has been created and puts the pre-defined requirements into my own words.

---

### Chosen Track: Full-stack

### Task: 

Create a full-stack implementation which will combine a dockerised frontend and backend for searching stores.

---

### Backend Requirements:

- Create an API that searches stores from `stores.json`
- Order stores by postcode
- Integrate with Postcode.io to fetch alt and long data (Additional requiremtnt)
- Retirn stores within a given radius of a postcode ordered north to south (Additional requirement)
- Include unit tests

### Frontend Requirements:

- Build a search interface with a search field and results list
- Type ahead suggestions with 100ms debounce
- Display 3 results initially, lazy load more on scroll

