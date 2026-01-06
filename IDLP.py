print("It is running. Go to your boot and press /start.")
import telebot
import instaloader

TOKEN = "Your_Bot_Token_Here"

bot = telebot.TeleBot(TOKEN)

def get_instagram_info(username):
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        info = {
            "👤 user name": profile.username,
            "📛 full name": profile.full_name,
            "👥 Followers": profile.followers,
            "➡️ Following": profile.followees,
            "📸 Publications": profile.mediacount,
            "📝 Bio": profile.biography or "nothing",
            "🔗 Link": f"https://instagram.com/{profile.username}"
        }
        return info
    except Exception as e:
        return {"❌ mistake": str(e)}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! 👋\nSend me your Instagram username to get Account info. Developer Team / https://t.me/+4tTmLzKdR4tlMTk1 / Developer channel / https://t.me/turmux1245")

@bot.message_handler(func=lambda m: True)
def handle_username(message):
    username = message.text.strip().replace("@", "")
    bot.send_message(message.chat.id, f"🔍 Searching for account information: {username}")
    info = get_instagram_info(username)
    response = "\n".join(f"{k}: {v}" for k, v in info.items())
    bot.send_message(message.chat.id, response)

bot.polling()