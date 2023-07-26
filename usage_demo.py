'''
 needs a file named ".env.secret" with the contents:
 api_key=your_api_string
 cse_key=your_cse_key

 '''
import SearchAssist
from dotenv import dotenv_values

config = dotenv_values(".env.secret") 
api_key = config['api_key']
cse_key = config['cse_key']

google_client=SearchAssist.GoogleSearchAPI(api_key, cse_key)
query = input("q? ")

# search_api = GoogleSearchAPI()
result_raw = google_client.search(query)
result_trimmed = google_client.trim_results(result_raw)
google_client.pprint_results(result_trimmed)
