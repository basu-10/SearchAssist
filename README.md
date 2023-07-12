# SearchAssist
Other tutorials and guides were needlessly complicated without providing better usage.
Hence made this module to use as a local package(for now) in your projects that does Google Search.


This code provides a basic implementation of a Google Search API wrapper that allows you to perform search queries and retrieve and format search results. It utilizes the googleapiclient library and the dotenv library for configuration.

### Setup:
python -m venv .venv
source .venv/bin/activate
pip install -U google-api-python-client
pip install -U python-dotenv

### To run:
1. You can run as script with _python SearchAssist.py_ , but the **.env.secret** file needs to be ready before that.
Set up the .env.secret file with the appropriate API and CSE keys obtained from the Google API Console(https://developers.google.com/custom-search/v1/overview) and Custom Search Engine(https://programmablesearchengine.google.com/controlpanel/all).

2. _import_ it as a module in other .py files and initialize with the keys.
   A sample Run.py file is provided to demonstarate the usage of this module when imported




TO DO:
. upload to pypi
. CLI usable  
