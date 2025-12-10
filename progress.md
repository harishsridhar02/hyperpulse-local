# Progress Log 


## Date: 6th December (Initial Setup)
- Set up Python Virtual Environment
- Installed all the necessary Tech Stack
- Made the project structure on VS Code
- Cloned the repository
- Created and ran a simple Flask App
- The first time I tried running the Web3 client, I hit a deadend, where it started saying "Connection Failed to RPC"
- Going through another method, asking doubts in ChatGPT and also understanding the entire process of how the block number is being retrieved, asking questions to myself ? - such as Why am I recieving blocks I didn't create? How are the blocks being produced? etc.
- Ran the code for web3.py and was able to retrieve the latest confirmed block number on Ethereum at the moment I made the request.



## Date: 7th December (Setting up the Telegram Bot)

- I started by creating a new branch 'feature/telegram-bot'.
- To set up any bot, the basic thing to do is to open the Telegram app and then use @BotFather to make all the kinds of bots you want to make. So, that is what I did. 
- The next thing I did was to setup the entire bot, give it a name and then get the Token ID for it.
- Once the API Token was generated, I saved the Token in a ".env" file.
- The next immedeate thing I did was to was to go through Gemini in understanding how I could set it up and it gave me a basic code, which it asked me to just copy and paste. 
- I went through the entire code, trying to understand each part of the code, trying to understand each component of the code.
- While trying to learn and understand these concepts, I faced a lot fo dfficulty in trying to visualize these topics in real-time. After getting some udnerstanding on the topic.
- After getting a basic understanding, I wrote the code given in Gemini into "main.py" file. 
- I used libraries such as async and Polling.
- My brief understanding:
    - **Polling**: It is like a loop, the bot constantly asks Telegram for updates.
    - **Async**: It handles other tasks while waiting for network responses. 
- Among all this, there was a major roadblock that I hit during the process. "The Git Permission Crisis"
-The *major problem* was that I was not able to push onto the repo due me not being a contributor, the solution to this was for me to "fork" the repo.
- This was not the only Roadblock that I hit, the other Roadblocks that I hit were: - 
    - **Environment Variable Wipe**: I created a new '.env' file for the bot taken but accidentally overwrote the Blockchain and Database keys i.e 'HYPERLIQUID_RPC_URL' & 'DATABSE_URL'. After which I restored all the other variables such as the Telegram Bot Token, Hyperliquid RPC URL, Database URL, Start Block and the Blocks Per Batch variable.
    - **Libraries Mess-Up**: There were number of 'ImportErrors' that kept occuring, especially when I was trying to run the telegram-bot code, after which I ran a troubleshoot and understood that the modern python library for telegram is something else and not just the word 'telegram'.
        - **The FIX:** Ran 'pip uninstall telegram' and then ran 'pip install python-telegram-bot' and then verified the version installed.
    - **Invalid Token Crash**: The Error that occurred was  'telegra,.error.InvalidToken: You must pass the token you recieved from BotFather!'. I started debugging the code and it looked correct wehn I looked at the code, there were no problems but turns out there were some hidden spaces/ whitespaces that were occuring due to copy-pasting. 
        - **The FIX:** Cleaned the '.env' file format which helped me to remove the spaces after which I added the 'token = token.strip()' in my file to remove allt he unwatned spaces that might be present.
- Finally, after doing all this, I was able to run my Telegram bot. I ran the code and the Terminal showed 'Bot is polling...'
- To verify I searched my bot on Telegram and sent '/start' and the Bot replied : 'Hello Harish! HyperPulse is Active.'
- Succesfully completed PR2 i.e. **Interface Layer**
- This **EIP** thing that was mentioned in the chat, I did some research about and this is what I understood...
    - EIP stands for **Ethereum Improvement Proposal**. It's how developers agree on standards. 
    - In this situation, the standard being followed is EIP-1474. 
    - It defines the list of commands that every node must understand. 
    - To go about the task, i.e. 'check out what RPC calls are, and where they're used (bonus: find the EIP where the standard for RPC URLs id defined)'
        - **RPC** stands for *Remote Procedure Call*.
        - For Example, **Computer A** wants to run a function but it doesn't have the data i.e. the Blockchain. So, it sends a message to **Computer B** that does have the node in question and says something like "Run this function for me and then send me back the result".
    - They are used everywhere, anywhere an app or a user needs to talk to the blockchain without needing to download the entire large sums of GBs of data.
- Now, I would probably put down all the questions that I asked myself during the process and some of them I got the answers to, some I still need to get answers to because they need more in-depth learning and understanding. 
- These questions are the questions I had so far so, a mix of **PR-1** and **PR-2**:-
    - Is it safe to put this Token in the code (Telegram bot token)?
    - What is Polling? Does the script stop running if this funciton doesn't exist? How does it know when to reply?
    - Why does Python care so much about the kind of telegram library we are using, how does it matter if it is just 'telegram' or 'python-telegram-bot'?
    - A proper understanding of each code that I had generated through *Gemini*... 
    - What is the differenc ebetween the '.env.example' file and the '.env' file?
    - Why can I not justpush my *Virtual Environment* directly onto the repo?
- These were all the questions I had while solving the **PR-1** and **PR-2** phases... 




## Date: 8th December (Validator Works)

- Merge Conflict - 1st task

- Transaction Hash Setup
    - Creating Utility File
    - Hit a deadend where I tried to setup the file and tried executing it but the bot wanst displaying any image and wasnt taking any input of the random transaction hash I was trying to upload.

- Re-Writing the entire main.py code to get a clear understanding on what is going on, so modifying the libraries being imported, making changes in the code to a cleaner one.
and will also be easier to interpret.

- Assigning Internal State Flags for the Bot's memory. Like State 0 means Menu select where the user is currently looking at the menu buttons. State 1 is Waiting for the Hash, where the user just clicked on Status (The Initial Model) the bot is now waiting for them to type the text i.e. waiting for the input. 

- Searched through the internet for the common basic format for a transaction hash used that as my pattern for Finite Automata

- Opened my bot on Telegram and tried running all the commands that I set up to check if the bot is working appropriately. For Example in this case, I was checking if I put a string of letters in the textbox after I start my code is it detecting if it is a Hash or not, so I tried two test words, one was just "banana" and the other was a random hash I found on the internet. 

- After running both the tests, my bot was able to run the format and be able to properly detect between the two.

- I checked if the menu options were working, in this situation, as an example I put two options i.e Show Transaction Status and PnL Ratio.
 
- Both the options had worked the way it was supposed to work, for the PnL ratio, I still hadnt developed it so it gave me the Error message and the Show Transaction option asked me for my Transaction Hash and then on the basis of it being current or not, it accepts it and gives out a message saying the Hash given is Valid.

- Now for the next phase the target is as follows:-
    - Importing Web3 into the *connection.py* file of the bot
    - Making sure that the Regular Expression that we are using is in the right format. Like basically I would even if the user gives me a a hash that follows all the criteria of the Regex it might end up not existing.
    - So, I would need a try/except block to handle the Transaction Not Found error without the bot crashing.
    - Along with this, I would also run the TestNet Verification. Here I would check if the **HYPERLIQUID_RPC_URL** points to the Testnet and not the Mainnet.