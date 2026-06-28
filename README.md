# Telegram Bot - FREE Deployment

## 🚀 Overview

This is a Telegram Bot deployed on **Render.com** with **GitHub Actions CI/CD**.

## ✨ Features

- ✅ **FREE Hosting** on Render.com
- ✅ **GitHub Actions CI/CD** for automatic deployment
- ✅ **Environment Variables** for secure configuration
- ✅ **24/7 Uptime**
- ✅ **Python 3.9+** support

## 📋 Prerequisites

1. **Telegram Bot Token** - Get from [@BotFather](https://t.me/BotFather)
2. **Render Account** - [Create free account](https://render.com)
3. **GitHub Account** - Already connected

## 🔧 Setup Instructions

### Step 1: Get Telegram Bot Token

1. Open Telegram
2. Search for [@BotFather](https://t.me/BotFather)
3. Send `/newbot` command
4. Follow the instructions to create your bot
5. Copy the bot token

### Step 2: Deploy to Render.com

1. Go to [render.com](https://render.com) and sign up
2. Connect your GitHub account
3. Click "New" → "Web Service"
4. Select this repository: `Nikhilsin527/telegram-bot`
5. Click "Connect & Deploy"
6. Set environment variables:
   - **Name:** `BOT_TOKEN`
   - **Value:** Your Telegram bot token
7. Click "Create Web Service"

### Step 3: Get Bot URL

1. Wait for deployment to complete (2-3 minutes)
2. Copy the bot URL from Render dashboard
3. Send the URL to [@BotFather](https://t.me/BotFather)
4. Bot will be activated!

## 📁 Project Structure

```
telegram-bot/
├── main.py              # Bot code
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── .github/
    └── workflows/
        └── deploy.yml  # GitHub Actions workflow
```

## 🎯 Available Commands

- `/start` - Start the bot
- `/help` - Show help message
- `/echo <text>` - Echo your message
- `/time` - Show current time

## 🔄 Automatic Deployment

This bot uses **GitHub Actions** for automatic deployment:

1. Push code to this repository
2. GitHub Actions automatically deploys to Render
3. Bot updates automatically!

## 💰 Cost

- **Render.com:** FREE tier (750 hours/month)
- **GitHub:** FREE
- **Total Cost:** **$0/month**

## 📊 Usage Limits

- **Free Tier:** 750 hours/month
- **RAM:** 512MB
- **Storage:** 3GB

## 🔒 Security

- Bot token stored in environment variables
- No sensitive data in code
- Automatic HTTPS

## 🐛 Troubleshooting

### Bot not responding?
1. Check if Render deployment is successful
2. Verify BOT_TOKEN environment variable
3. Check bot logs in Render dashboard

### Deployment failed?
1. Check GitHub Actions logs
2. Verify Python version (3.9+)
3. Check requirements.txt

## 📚 Resources

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [python-telegram-bot](https://python-telegram-bot.org/)
- [Render Documentation](https://render.com/docs)
- [GitHub Actions](https://docs.github.com/en/actions)

---

**Deployed with ❤️ using GitHub + Render**