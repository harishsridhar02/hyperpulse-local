import re

def is_valid_tx(text: str) -> bool:
    """
    Validates if the input string matches the standard EVM transaction hash format.
    
    Args:
        text (str): The input string to validate.
        
    Returns:
        bool: True if the string is a valid 64-character hex string starting with '0x'.
    """
    pattern = r"^0x[a-fA-F0-9]{64}$"
    
    if re.match(pattern, text):
        return True
    return False



""" 
Transaction Hash is basically something similar to 
a Tracking Number for packages. So everytime a trade 
is made, a Transaction Hash is generated. 

This Transaction hash is unique which mean no other trade will have the same transaction hash as you do.
It is the proof that the action or the trade has happened.
Anyone with the hash can look up the details of the transaction that was made.
Details such as Amount, time , etc.

This Transaction has must follow a specific pattern.
We use Regular Expressions to validate these patterns.
For Example, it should start with '0x' followed by 64 hexadecimal characters.

"""