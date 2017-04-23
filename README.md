# Nitrogen Sports API
Unofficial API for Nitrogen Sports.

## Running the example betting system
To demonstrate the API, an example betting system included. It bets soccer match draws with a modified Martingale escalation on losses.

Here's how you can run that with Powershell. There will be some differences for Linux or MacOS, like in activating the virtual environment.

**Notes:** All development and testing has been with Python 3.x so compatibility with 2 is unknown. NodeJS is needed - it's a prerequisite that cannot be taken care of by pip.

```
# Make and activate new virtualenv 'venv'
virtualenv venv
.\venv\Scripts\activate.ps1

# Install the requirements
pip install -r requirements.txt

# Edit parameters in soccer_draws_system.py as desired

# Run the system
python soccer_draws_system.py

# Then eventually you might need...
[Ctrl+C]
deactivate
```
