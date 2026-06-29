import os
import json
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# Get API keys from environment variables
BOT_TOKEN = os.environ.get('BOT_TOKEN')
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY')

if not BOT_TOKEN:
    print("ERROR: BOT_TOKEN environment variable not set!")
    exit(1)

# User memory storage (in-memory for demo)
user_memory = {}

# AI Response Function using OpenRouter API
def get_ai_response(prompt, user_id):
    """Get AI response using OpenRouter API"""
    try:
        import openai
        
        if not OPENROUTER_API_KEY:
            return "⚠️ OpenRouter API key not configured. Please set OPENROUTER_API_KEY environment variable."
        
        openai.api_key = OPENROUTER_API_KEY
        
        # Get user memory if exists
        user_context = user_memory.get(user_id, {})
        memory_text = ""
        if user_context:
            memory_text = f"\n\nUser Information:\n"
            for key, value in user_context.items():
                memory_text += f"- {key}: {value}\n"
        
        # Create prompt with memory context
        full_prompt = f"You are a helpful AI assistant. User memory:\n{memory_text}\n\nUser says: {prompt}"
        
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly, helpful AI assistant. Be concise and friendly."},
                {"role": "user", "content": full_prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        return f"❌ AI Error: {str(e)}"

# Bot Commands
def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message with keyboard"""
    user_id = update.effective_user.id
    
    # Create keyboard
    keyboard = [
        [InlineKeyboardButton("💬 Chat", callback_data="chat")],
        [InlineKeyboardButton("🧠 Memory", callback_data="memory")],
        [InlineKeyboardButton("❓ Help", callback_data="help")],
        [InlineKeyboardButton("⏰ Time", callback_data="time")],
        [InlineKeyboardButton("📅 Date", callback_data="date")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        '👋 Welcome to Mira AI Bot!\n\n'
        'I am your personal AI assistant. Select a command below or type /chat to start chatting!\n\n'
        'Made with ❤️ by Mira',
        reply_markup=reply_markup
    )

def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message"""
    help_text = (
        '📚 **Available Commands:**\n\n'
        '/start - Start the bot\n'
        '/help - Show this help message\n'
        '/chat - Start AI chat\n'
        '/memory - Manage user memory\n'
        '/time - Show current time\n'
        '/date - Show current date\n'
        '/clear - Clear conversation history\n\n'
        '💡 **Tips:**\n'
        '- Use the buttons below for quick access\n'
        '- I remember your preferences\n'
        '- Ask me anything!'
    )
    
    update.message.reply_text(help_text, parse_mode='Markdown')

def chat_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start AI chat"""
    user_id = update.effective_user.id
    
    if context.args:
        # User provided a message
        user_message = ' '.join(context.args)
        ai_response = get_ai_response(user_message, user_id)
        update.message.reply_text(f"🤖 AI: {ai_response}")
    else:
        update.message.reply_text(
            '💬 **AI Chat Started!**\n\n'
            'Type your message and I will respond with AI-powered help!\n\n'
            'Example: /chat Hello, how are you?'
        )

def memory_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manage user memory"""
    user_id = update.effective_user.id
    
    if context.args:
        if len(context.args) >= 2:
            key = context.args[0]
            value = ' '.join(context.args[1:])
            user_memory[user_id] = user_memory.get(user_id, {})
            user_memory[user_id][key] = value
            update.message.reply_text(f"✅ Memory saved: {key} = {value}")
        else:
            update.message.reply_text('Usage: /memory <key> <value>')
    else:
        # Show current memory
        user_mem = user_memory.get(user_id, {})
        if user_mem:
            memory_text = '🧠 **Your Memory:**\n\n'
            for key, value in user_mem.items():
                memory_text += f"- {key}: {value}\n"
            update.message.reply_text(memory_text)
        else:
            update.message.reply_text('🧠 **No memory saved yet.**\n\nUsage: /memory <key> <value>')

def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show current time"""
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    update.message.reply_text(f"⏰ Current time: {current_time}")

def date_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show current date"""
    current_date = datetime.now().strftime('%Y-%m-%d (%A)')
    update.message.reply_text(f"📅 Current date: {current_date}")

def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Clear conversation history"""
    user_id = update.effective_user.id
    user_memory[user_id] = {}
    update.message.reply_text('🗑️ Conversation history cleared!')

def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks"""
    query = update.callback_query
    query.answer()
    
    user_id = query.from_user.id
    
    if query.data == "chat":
        query.edit_message_text(
            '💬 **AI Chat Started!**\n\n'
            'Type your message and I will respond with AI-powered help!'
        )
    elif query.data == "memory":
        user_mem = user_memory.get(user_id, {})
        if user_mem:
            memory_text = '🧠 **Your Memory:**\n\n'
            for key, value in user_mem.items():
                memory_text += f"- {key}: {value}\n"
            query.edit_message_text(memory_text)
        else:
            query.edit_message_text('🧠 **No memory saved yet.**\n\nUsage: /memory <key> <value>')
    elif query.data == "help":
        help_text = (
            '📚 **Available Commands:**\n\n'
            '/start - Start the bot\n'
            '/help - Show this help message\n'
            '/chat - Start AI chat\n'
            '/memory - Manage user memory\n'
            '/time - Show current time\n'
            '/date - Show current date\n'
            '/clear - Clear conversation history\n\n'
            '💡 **Tips:**\n'
            '- Use the buttons below for quick access\n'
            '- I remember your preferences\n'
            '- Ask me anything!'
        )
        query.edit_message_text(help_text, parse_mode='Markdown')
    elif query.data == "time":
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query.edit_message_text(f"⏰ Current time: {current_time}")
    elif query.data == "date":
        current_date = datetime.now().strftime('%Y-%m-%d (%A)')
        query.edit_message_text(f"📅 Current date: {current_date}")

def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle regular messages"""
    user_id = update.effective_user.id
    user_message = update.message.text
    
    # Get AI response
    ai_response = get_ai_response(user_message, user_id)
    
    update.message.reply_text(f"🤖 AI: {ai_response}")

def main():
    """Start the bot"""
    # Create the Application
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("chat", chat_command))
    app.add_handler(CommandHandler("memory", memory_command))
    app.add_handler(CommandHandler("time", time_command))
    app.add_handler(CommandHandler("date", date_command))
    app.add_handler(CommandHandler("clear", clear_command))
    
    # Register callback query handler for buttons
    app.add_handler(CallbackQueryHandler(button_callback))
    
    # Register message handler for text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start the Bot
    print("🤖 Mira AI Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()