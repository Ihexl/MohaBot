import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Welcome {user_first_name}, looking for some owls HUH ?")
    help_text = (  
        # "Here are the commands you can use:\n"  
        # "/start - Start the bot\n"  
        # "/help - List all available commands\n"  
        # "/caps <text> - Convert the text to uppercase\n"  
        # "/title <text> - Convert the text to Title case\n"
        # "Just send any message and I'll echo it back!"
        "عيني خالي هاي الأوامر التفيدك:\n"
        "/start - راح يرحب بيك ويعفطلك"
        )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)  



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_title = ' '.join(context.args).title()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_title)

# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):  
#     help_text = (  
#         "Here are the commands you can use:\n"  
#         "/start - Start the bot\n"  
#         "/help - List all available commands\n"  
#         "/caps <text> - Convert the text to uppercase\n"  
#         "/title <text> - Convert the text to Title case\n"
#         "Just send any message and I'll echo it back!"
#         )
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)  


if __name__ == '__main__':
    application = ApplicationBuilder().token('8087343908:AAHbWMRAszEEwbcE6QjYf6Dbg_OhgNRpXwM').build()
    
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)  
    caps_handler = CommandHandler('caps', caps)
    title_handler = CommandHandler('title', title)
    # help_handler = CommandHandler('help', help_command)  

    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)  
    application.add_handler(caps_handler)  
    application.add_handler(title_handler)  
    # application.add_handler(help_handler)  


    application.run_polling()


