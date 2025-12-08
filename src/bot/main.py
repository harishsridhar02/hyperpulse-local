import os
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):  # Defining it's behavior
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"Hello {user_name}! HyperPulse is Active.")


if __name__ == '__main__':
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not token:
        exit("Error: No token found in .env!")
        
    token = token.strip()  # Clean the token
    print(f"DEBUG: My Token is: '{token}'") 
    
    # 1. Build the Bot
    app = ApplicationBuilder().token(token).build()
    
    # 2. Wire up the "start" command (YOU WERE MISSING THIS)
    app.add_handler(CommandHandler("start", start))
    
    # 3. Start the Loop (YOU WERE MISSING THIS)
    print("Bot is polling... Go say /start on Telegram!")
    app.run_polling()