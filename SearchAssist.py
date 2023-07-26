"""
This Python package provides a command-line tool to leverage the Google Custom Search API for easy web searches.
"""

'''
Can run as:
python SearchAssist.py --q "SEARCH QUERY"
OR,
python SearchAssist.py --api-key YOUR_API_KEY --cse-key YOUR_CSE_KEY --q "SEARCH QUERY"

provide your own 
YOUR_API_KEY from https://developers.google.com/custom-search/v1/overview
YOUR_CSE_KEY from https://programmablesearchengine.google.com/controlpanel/all
SEARCH_QUERY 
'''

from googleapiclient.discovery import build
import pprint
import logging

import argparse
import os
from dotenv import dotenv_values

# Set up logging configuration
logging.basicConfig(filename="error.log", level=logging.ERROR)

config = dotenv_values(".env.secret")


class GoogleSearchAPI:
    def __init__(self, api_key, cse_key):
        self.api_key = api_key
        self.cse_key = cse_key
        self.resource = build("customsearch", "v1", developerKey=self.api_key).cse()

    def search(self, query):
        try:
            result_raw = self.resource.list(q=query, cx=self.cse_key).execute()            
            return result_raw
        except Exception as e:
            logging.error(f"Error {e} occurred")

    def trim_results(self, result_raw):
        result_trimmed = []
        for i in result_raw["items"]:
            title = i["title"]
            snippet = i["snippet"]
            url = i["link"]
            d = {"title": title, "snippet": snippet, "url": url}
            result_trimmed.append(d)        
        return result_trimmed

    def pprint_results(self, result_trimmed):
        for i in result_trimmed:
            pprint.pprint(i)


class Process:
    def save_to_env_file(api_key, cse_key, file_path):
        with open(file_path, "w") as file:
            file.write(f"API_KEY={api_key}\n")
            file.write(f"CSE_KEY={cse_key}\n")

    def get_keys_from_env(file_path):
        config = dotenv_values(file_path)
        api_key = config.get("API_KEY")
        cse_key = config.get("CSE_KEY")
        return api_key, cse_key


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Google Search API Client")

    # command line arguments
    parser.add_argument("--api-key", help="Your API Key")
    parser.add_argument("--cse-key", help="Your CSE Key")
    parser.add_argument("--q", required=True, help="Search query")

    args = parser.parse_args()
    env_file_path = ".env.secret"

    api_key, cse_key = "", ""

    # Check if the API key and CSE key are provided as command-line arguments
    if args.api_key and args.cse_key:
        # Save the provided keys to the .env.secret file
        Process.save_to_env_file(args.api_key, args.cse_key, env_file_path)
    else:
        # Check if the .env.secret file exists and load keys from there
        if os.path.exists(env_file_path):
            api_key, cse_key = Process.get_keys_from_env(env_file_path)
        else:
            print(".env.secret file not exists")

        if not api_key or not cse_key:
            print("Error: API key or CSE key not found in .env.secret.")
            # Prompt the user to enter the keys if not found in the file
            api_key = input("Enter your API key: ")
            cse_key = input("Enter your CSE key: ")
            Process.save_to_env_file(api_key, cse_key, env_file_path)
    
    print("Searching for:", args.q)
    # search logic
    search_api = GoogleSearchAPI(api_key, cse_key)
    result_raw = search_api.search(args.q)
    result_trimmed = search_api.trim_results(result_raw)
    search_api.pprint_results(result_trimmed)

