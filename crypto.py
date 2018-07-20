import urllib.request as urllib2
import json, sys

def sumCrypto(volume, boughtAt, curPrice):
	return ( (float(curPrice)/float(boughtAt)) * float(volume))


btcUrl = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'
ltcUrl = 'https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD'
ethUrl = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD'

response = urllib2.urlopen(btcUrl)
data = json.loads(response.read())
print('profit at  : ' + str(.15275428*data['USD']* .7)  + ' after taxes')