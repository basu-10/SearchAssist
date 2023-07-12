'''
user must provide their key while running as module! import , then initialize with keys
OR, can also setup key in a .env.private file and run this file as script: python -m file123.py
'''
from googleapiclient.discovery import build
import pprint

from dotenv import dotenv_values
config = dotenv_values(".env.secret") 

import logging
logging.basicConfig(filename='error.log', level=logging.ERROR) # Set up logging configuration
                    
class GoogleSearchAPI:
    def __init__(self, api_key, cse_key):
        self.api_key = api_key
        self.cse_key = cse_key
        self.resource = build("customsearch", 'v1', developerKey=self.api_key).cse()

    def search(self, query):
        try:
            result_raw = self.resource.list(q=query, cx=self.cse_key).execute()
            with open("result_raw.txt", 'w') as f:
                f.write(str(result_raw))
            return result_raw
        except Exception as e:
            logging.errors(f'Error {e} occured')

    def trim_results(self, result_raw):
        result_trimmed = []
        for i in result_raw['items']:
            title = i['title']
            snippet = i['snippet']
            url = i['link']
            d = {'title': title, 'snippet': snippet, 'url': url}
            result_trimmed.append(d)
        with open("result_trimmed.txt", 'w') as f:
            f.write(str(result_trimmed))
        return result_trimmed

    def pprint_results(self, result_trimmed):
        for i in result_trimmed:
            pprint.pprint(i)

if __name__=="__main__":
    
    query = input("Query? ")

    api_key = config['api_key']
    cse_key = config['cse_key']
    search_api = GoogleSearchAPI(api_key, cse_key)
    result_raw = search_api.search(query)
    result_trimmed = search_api.trim_results(result_raw)
    search_api.pprint_results(result_trimmed)
