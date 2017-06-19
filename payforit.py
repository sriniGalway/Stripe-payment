# importing the requests library
import requests

subscriptionID = '921201' #Transaction is done based on subscriptionID
# api-endpoint
url = "https://fpay.fonix.io/rest/subscriptions/" + subscriptionID

# your API key here
API_KEY = "live_IifwlWoCmvmpEGyKMyGUCA"

headers = {'X-API-KEY': API_KEY} #Your API key must be added as a HTTP header

# sending post request and saving the response as response object
r = requests.post(url, headers=headers)

# printing response in json format
print r.text
