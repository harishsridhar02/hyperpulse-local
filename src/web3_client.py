from web3 import Web3  # Import Web3 library

RPC_URL = "https://ethereum.publicnode.com"  # Public RPC Endpoint


web3 = Web3(Web3.HTTPProvider(RPC_URL))  # Intializing web3 client

print("Connected:", web3.is_connected())  # Checking Connection

if web3.is_connected():     # Get Latest block
    latest_block = web3.eth.block_number
    print("Latest Block:", latest_block)
else:
    print("Failed to connect to RPC")


# So basically this is a Read-Only command 
# We do not produce blocks. Blockchain data is public and everyone can read it
# We are simply fetching what the network alrady created
