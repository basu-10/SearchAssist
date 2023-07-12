# SearchAssist
While testing out chatgpt with google searches,I found most tutorials and guides to be needlessly complicated without any better usage than the package itself.
Hence made this module to use as a local package(for now) in your projects that does Google Search, with error handling, secrets storage, run as script or import.


This code provides a basic implementation of a Google Search API wrapper that allows you to perform search queries and retrieve and format search results. It utilizes the googleapiclient library and the dotenv library for configuration.

### Setup:
* Download the files
* python -m venv .venv
* source .venv/bin/activate
* pip install -U google-api-python-client
* pip install -U python-dotenv
* IMPORTANT: Rename the *env.secret* file to *.env.secret* (Without this step python-dotenv can't find the file)

### To run:
1. You can run as script with _python SearchAssist.py_ , but the **.env.secret** file needs to be ready before that.
Set up the .env.secret file with the appropriate API and CSE keys obtained from the Google API Console(https://developers.google.com/custom-search/v1/overview) and Custom Search Engine(https://programmablesearchengine.google.com/controlpanel/all).

2. _import_ it as a module in other .py files and initialize with the keys. Then invoke the search() method with your query string, trim the results, and pprint them.
   All of these steps are provided in a _Run.py_ file. 



TO DO:
* upload to pypi
* CLI usable  
