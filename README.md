# Hudl Login Automation Tests

This project automates login functionality tests for hudl (https://www.hudl.com) 
using **Selenium, Pytest, and Page Object Model (POM)**.


## 📂 Structure
- `pages/` → Page Object classes
- `tests/` → Test cases
- `reports/` → Test Run Reports
- `conftest.py` → Setup & teardown for browser
- `requirements.txt` → Dependencies

## Setup

1. Clone repo
2. Install the requirements in the requirements.txt
3. Run the tests using pytest -v tests/test_login.py 
4. If you want the report use pytest -v tests/test_login.py --html=reports/reports.html


## Improvements
1. Multiple accounts expecting the same failure can be parametrised 
2. Use of different browsers to cover cross browser testing