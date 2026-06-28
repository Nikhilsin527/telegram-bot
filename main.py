import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Get bot token from environment variable
BOT_TOKEN = os.environ.get('BOT_TOKEN')

if not BOT_TOKEN:
    print("ERROR: BOT_TOKEN environment variable not set!")
    print("Please set BOT_TOKEN in Render environment variables.")
    exit(1)

# Bot commands
def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        'Hello! I am your Telegram Bot.\n\n'
        'Commands:\n'
        '/start - Start the bot\n'
        '/help - Show help\n'
        '/echo <text> - Echo your message\n'
        '/time - Show current time'
    )

def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Available commands:\n\n'
        '/start - Start the bot\n'
        '/help - Show this help message\n'
        '/echo <text> - Echo your message back\n'
        '/time - Show current time'
    )

def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo the user message."""
    if context.args:
        text = ' '.join(context.args)
        update.message.reply_text(f'Echo: {text}')
    else:
        update.message.reply_text('Please provide text after /echo command.')

def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show current time."""
    from datetime import datetime
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    update.message.reply_text(f'Current time: {current_time}')

def main():
    """Start the bot."""
    # Create the Application
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler("time", time_command))

    # Register message handler for text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the Bot
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()