# SearchAssist - A Command-line Search Assistant
SearchAssist is a Python command-line tool designed to simplify web searches using the Google Custom Search API. It allows you to quickly search for information using a shorter or longer command-line syntax. Additionally, you can integrate SearchAssist into your projects as a module to perform searches programmatically.

Why not googler?
While "googler" is a command-line utility that allows direct Google searches from the terminal, it has limitations as it doesn't offer easy manipulation or processing of search results. On the other hand, SearchAssist leverages the Google Custom Search API, enabling programmable searches from within a Python environment. This integration into Python projects allows for greater flexibility and customization in handling search results. SearchAssist provides both raw results and a prettified format, making it easier to tailor the search functionality according to your application's specific needs. Furthermore, it stores API and CSE keys in a separate file, allowing for seamless usage across various modules



### Setup:
* Download the files
* $ python -m venv .venv
* $ source .venv/bin/activate
* $ pip install -r requirements.txt

Get the appropriate API and CSE keys obtained from the Google API Console(https://developers.google.com/custom-search/v1/overview) and Custom Search Engine(https://programmablesearchengine.google.com/controlpanel/all).

### How to Run:
1. Shorter Way:
   <br> Use the following command for a quick search:
   <br> `$ python SearchAssist.py --q "Your search query"`
   
When running this command, you will be prompted to enter your Google Custom Search Engine (CSE) and API key. Once entered, the keys will be saved to the .env.secret file, and you won't need to provide them again for subsequent searches.


2. Longer Way:
   <br> Alternatively, you can use the longer command-line syntax to save the CSE and API keys explicitly:   
   <br> `$ python SearchAssist.py --api-key YOUR_API_KEY --cse-key YOUR_CSE_KEY --q "Your search query"`
   
   This command will save the provided CSE and API keys to the .env.secret file and then proceed with the search.
   The benefit of using the longer way is that it supports using separate API/CSE keys for each search query.
   Additionally, once the longer way has been used, the same keys will be used for subsequent searches when using the shorter syntax.

3. Using SearchAssist in Your Projects:
   You can import SearchAssist as a module in your Python files to perform searches programmatically.
   To get started, follow these steps:
   ```
   from SearchAssist import GoogleSearchAPI #Import GoogleSearchAPI
   #Initialize GoogleSearchAPI
   api_key = 'YOUR_API_KEY'
   cse_key = 'YOUR_CSE_KEY'
   search_api = GoogleSearchAPI(api_key, cse_key)
   #Perform a Search
   query = 'Your search query'
   result_raw = search_api.search(query)
   #Trim the Results
   result_trimmed = search_api.trim_results(result_raw)
   #Print the results
   search_api.pprint_results(result_trimmed)
   ```
With these steps, you can seamlessly integrate the GoogleSearchAPI module into your projects or use it to search from CLI. Customize the code as needed to suit your specific use cases and enjoy simplified web searching! Happy coding!



TO DO:
* Upload to PyPI to make the module accessible to a wider audience.

