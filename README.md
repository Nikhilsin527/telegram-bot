# Mira AI Bot - Telegram AI Assistant

## 🤖 Overview

This is a Mira-like AI assistant Telegram Bot deployed on **Render.com** with **GitHub Actions CI/CD**.

## ✨ Features

- ✅ **AI Responses** using OpenAI API
- ✅ **Multiple Commands** with nice UI
- ✅ **User Memory** - Remember preferences
- ✅ **Inline Buttons** - Quick access commands
- ✅ **Error Handling** - Robust code
- ✅ **Auto Deployment** - GitHub Actions ready

## 📋 Prerequisites

1. **Telegram Bot Token** - Get from [@BotFather](https://t.me/BotFather)
2. **OpenAI API Key** - Get from [platform.openai.com](https://platform.openai.com/api-keys)
3. **Render Account** - [Create free account](https://render.com)
4. **GitHub Account** - Already connected

## 🔧 Setup Instructions

### Step 1: Get Telegram Bot Token

1. Open Telegram
2. Search for [@BotFather](https://t.me/BotFather)
3. Send `/newbot` command
4. Follow the instructions to create your bot
5. Copy the bot token

### Step 2: Get OpenAI API Key

1. Go to [platform.openai.com](https://platform.openai.com/api-keys)
2. Sign up or login
3. Click "Create new secret key"
4. Copy the API key

### Step 3: Deploy to Render.com

1. Go to [render.com](https://render.com) and sign up
2. Connect your GitHub account
3. Click "New" → "Web Service"
4. Select this repository: `Nikhilsin527/telegram-bot`
5. Click "Connect & Deploy"
6. Set environment variables:
   - **Name:** `BOT_TOKEN`
   - **Value:** Your Telegram bot token
   - **Name:** `OPENAI_API_KEY`
   - **Value:** Your OpenAI API key
7. Click "Create Web Service"

### Step 4: Get Bot URL

1. Wait for deployment to complete (2-3 minutes)
2. Copy the bot URL from Render dashboard
3. Send the URL to [@BotFather](https://t.me/BotFather)
4. Bot will be activated!

## 🎯 Available Commands

- `/start` - Start the bot with keyboard
- `/help` - Show help message
- `/chat <message>` - Chat with AI
- `/memory <key> <value>` - Save user memory
- `/time` - Show current time
- `/date` - Show current date
- `/clear` - Clear conversation history

## 🎨 Features

### Inline Buttons

- **💬 Chat** - Start AI chat
- **🧠 Memory** - View saved memory
- **❓ Help** - Show help
- **⏰ Time** - Show current time
- **📅 Date** - Show current date

### User Memory

Bot remembers user preferences:
- `/memory name Nikhil` - Save name
- `/memory age 25` - Save age
- `/memory location Mumbai` - Save location

## 🔄 Automatic Deployment

This bot uses **GitHub Actions** for automatic deployment:

1. Push code to this repository
2. GitHub Actions automatically deploys to Render
3. Bot updates automatically!


n## 💰 Cost

| Service | Cost |
|---------|------|
| **GitHub** | FREE |
| **Render.com** | FREE (750 hours/month) |
| **OpenAI API** | $0.02/1K tokens |
| **TOTAL** | **~$1/month** |

## 📊 Usage Limits

- **Free Tier:** 750 hours/month
- **RAM:** 512MB
- **Storage:** 3GB

## 🔒 Security

- API keys stored in environment variables
- No sensitive data in code
- Automatic HTTPS

## 🐛 Troubleshooting

### Bot not responding?
1. Check if Render deployment is successful
2. Verify BOT_TOKEN and OPENAI_API_KEY environment variables
3. Check bot logs in Render dashboard

### Deployment failed?
1. Check GitHub Actions logs
2. Verify Python version (3.9+)
3. Check requirements.txt

### AI not responding?
1. Verify OPENAI_API_KEY is correct
2. Check OpenAI account balance
3. Verify API key has credits

## 📚 Resources

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [python-telegram-bot](https://python-telegram-bot.org/)
- [OpenAI API](https://platform.openai.com/docs/api-reference)
- [Render Documentation](https://render.com/docs)
- [GitHub Actions](https://docs.github.com/en/actions)

## 🎉 Enjoy Your Mira AI Bot!

**Deployed with ❤️ using GitHub + Render + OpenAI**