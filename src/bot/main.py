import os 
import re # Regular Expression Library
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler,
    ContextTypes, 
    CallbackQueryHandler,  # Handles Button Clicks 
    MessageHandler, # Handles the Input Messages (Manage Memory)
    filters, 
    ConversationHandler
)

load_dotenv()

MENU_SELECT, WAITING_FOR_HASH = range(2)

"""
Assigning numbers to each stage of the conversation
It creates the map for our bot
It is a Python Shortcut
For Example:
MENU_SELECT = 0
WAITING_FOR_HASH = 1
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    
    # Define Buttons (Added EXIT)
    keyboard = [
        [InlineKeyboardButton("PnL Ratio", callback_data='pnl')],
        [InlineKeyboardButton("Transaction Status", callback_data='status')],
        [InlineKeyboardButton("Exit", callback_data='exit')] # <--- NEW BUTTON
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text(f"Hello {user}! Select an option:", reply_markup=reply_markup)
    else:
        # If we are coming back from a button click/loop
        await update.callback_query.message.reply_text(f"Welcome back {user}! Select an option:", reply_markup=reply_markup)
        
    return MENU_SELECT
   

"""
Creating the Buttons
callback_data is the Secret ID sent to the both when the button is clicked
Sending the message with the buttons
It tells the system which state it is in right now... State 0, State 1, etc...
InlineKeyboardButton is the Button like the individual one and the frame that
holds that buttons together in rows and columns is the Markup
"""
async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    choice = query.data

    
    if choice == 'exit':
        await query.edit_message_text("Bot Closed. Type /start to open again.")
        return ConversationHandler.END

    
    elif choice == 'status':
        await query.edit_message_text(
            text="You selected: **Transaction Status**.\nPlease paste your Transaction Hash below:",
            parse_mode='Markdown'
        )
        return WAITING_FOR_HASH
    
    
    elif choice == 'pnl':
        await query.message.reply_text("🚧 PnL Feature coming soon!")
        
       
        await start(update, context) 
        return MENU_SELECT
"""
For Example, the option: "Transaction Status" is selected. 
The Transaction Hash has to be pasted there to inputted.
What the bot does internally is it moves the User to the NEXT STATE
i.e. Waiting for Input
Once this is done, the conversation is ended. After the Hash is Validated. (Initial Setup)
Added logic for Exit Button 
"""

async def process_hash(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    pattern = r"^0x[a-fA-F0-9]{64}$"
    
    if re.match(pattern, user_input):
        await update.message.reply_text(f"**Valid Hash!**\nProcessing {user_input[:10]}...")
        
        
        await update.message.reply_text("Done! What else?")
        await start(update, context) 
        return MENU_SELECT 
        
    else:
        await update.message.reply_text("❌ Invalid! Try again:")
        return WAITING_FOR_HASH

if __name__ == '__main__':
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token: exit("Error: No token found!")
    
    app = ApplicationBuilder().token(token.strip()).build()
    
   
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MENU_SELECT: [CallbackQueryHandler(menu_handler)],
            WAITING_FOR_HASH: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_hash)],
        },
        fallbacks=[CommandHandler("start", start)]
    )
    
    app.add_handler(conv_handler)
    print("Interactive Bot is Polling... Send /start!")
    app.run_polling()

"""
If the system is in State 0 then watch for Button Clicks i.e. Menu
If the system is in State 1 then watch for Text i.e. Waiting
If the system gets stuck then "/start" resets

"""

