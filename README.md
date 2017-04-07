# Nitrogen Sports API
Unofficial API for Nitrogen Sports. Automates common interactions with the site using Selenium.

## Setup
These instructions are for Windows Powershell. There will be some differences for OS X / MacOS, like in activating the virtual environment and using the web driver.

Before the scraper will work correctly, you'll need to put the [Chromium web driver](https://sites.google.com/a/chromium.org/chromedriver/) (chromedriver.exe) inside of the *chromedriver* directory.
```
# Get into a new virtualenv
virtualenv venv
.\venv\Scripts\activate.ps1

# Install the requirements
pip install -r requirements.txt

# TODO hey how do they run this thing?

# Then eventually when you're done...
deactivate
```