'''
can run as:
python SearchAssist.py
OR,
python SearchAssist.py --api-key YOUR_API_KEY --cse-key YOUR_CSE_KEY --query SEARCH_QUERY

provide your own YOUR_API_KEY, YOUR_CSE_KEY, SEARCH_QUERY
'''
from googleapiclient.discovery import build
import pprint
import argparse
import logging
from dotenv import dotenv_values

# Set up logging configuration
logging.basicConfig(filename='error.log', level=logging.ERROR)

config = dotenv_values(".env.secret")

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
            logging.error(f'Error {e} occurred')

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Google Search API Client")

    # command line arguments
    parser.add_argument("--api-key", help="Your API Key")
    parser.add_argument("--cse-key", help="Your CSE Key")
    parser.add_argument("--query", help="Search query")

    args = parser.parse_args()

    api_key = args.api_key or config['api_key']
    cse_key = args.cse_key or config['cse_key']
    query = args.query or input("Enter your search query: ")

    search_api = GoogleSearchAPI(api_key, cse_key)
    result_raw = search_api.search(query)
    result_trimmed = search_api.trim_results(result_raw)
    search_api.pprint_results(result_trimmed)
