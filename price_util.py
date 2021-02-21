# test print

import os
import requests
import json

mykey = os.getenv( 'NOMICS_API_KEY' )

# input: ticker symbol in string
# output: current price of the crypto
def currentPrice( id ):
	ticker = "https://api.nomics.com/v1/currencies/ticker?"
	key = "key=" + mykey
	ids = "&ids=" + id
	interval = "&interval=1d"
	perPage = "&per-page=100"
	page = "&page=1"
	
	response = requests.get( ticker + key + ids + interval + perPage + page )

	if( response.status_code != 200 ):
		return null
	else:
		formattedRes = json.dumps( response.json(), indent=2 )

		return formattedRes



