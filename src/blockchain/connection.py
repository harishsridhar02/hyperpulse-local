"""
This file looks at the .env file to find
the HYPERLIQUID_RPC_URL, the address of the blockchain node.
It then uses the Web3 library to establish a line.
It returns a w3 object. Any other part of the code that is present, 
for example, the "bot" can grab this w3 object to ask questions.
"What is the gass fee?" 
"Did the trade pass?"

# What is a gas fee? ->  Gas fee is the fee you pay the Validator to move 
data or a trade on the blcokchain. 
It is used as an incentive and for spam prevention.

"""
"""
Hyperliquid Connection Module.

This module handles the initialization of the Web3 connection to the 
Hyperliquid EVM (Ethereum Virtual Machine) node using RPC URLs 
configured in the environment variables.

"""

import os 
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

def get_hyperliquid_connection():

    rpc_url = os.getenv("HYPERLIQUID_RPC_URL")

    if not rpc_url:

        raise ValueError("Error: HYPERLIQUID_RPC_URL is missing...")
    
    return Web3(Web3.HTTPProvider(rpc_url))     # To create the connection

if __name__ == "__main__": 

    try: # Testing to see if the block runs directly
        w3 = get_hyperliquid_connection()
        if w3.is_connected():
            print(f"Connected! Latest Block: {w3.eth.block_number}")
        
        else:
            print("Connected FAILED!")
    
    except Exception as e:
        print(f"Error: {e}")
