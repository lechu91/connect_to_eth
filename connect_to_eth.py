from web3 import Web3
from web3.providers.rpc import HTTPProvider

#If you use one of the suggested infrastructure providers, the url will be of the form
#now_url  = f"https://eth.nownodes.io/{now_token}"
#alchemy_url = f"https://eth-mainnet.alchemyapi.io/v2/{alchemy_token}"
#infura_url = f"https://mainnet.infura.io/v3/05d545fd8cc5446a9b6e02369555a845"

def connect_to_eth():
	url = f"https://mainnet.infura.io/v3/05d545fd8cc5446a9b6e02369555a845"
	w3 = Web3(HTTPProvider(url))
	assert w3.isConnected(), f"Failed to connect to provider at {url}"
	return w3
	

if __name__ == "__main__":
	connectToEth()
