# reg-test

## Setup
1. Make sure python and pip are installed
2. Install any virtual environment package like 'venv' to ensure installed packages are project localized `python3 -m venv .venv`
3. Install additional packages specified for the project `pip install -r /path/to/requirements.txt`

## Configuration
Tests uses predefined base url recorded in a so called `.env` file.
In order to execute tests, the environment specific env file must be created on the machince.
File content should host the following attributes with an appropriate value 
- PYTEST_BASE_URL = <base url value> in form of <scheme://domain/> eg: https://solarpunk.buzz/

Note! Upon new base_url (eg: on swithching between environments), flush the .auth directory to make sure logged in state is captured according to the environment in use!

## Execution
`pytest`
    -- options [See Playwright guidance](https://playwright.dev/python/docs/running-tests#running-tests)