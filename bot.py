import telebot
import random
import os
from flask import Flask, request

BOT_TOKEN = "8848206161:AAErWtrs1I6txPGc644b_zFuIe8OZ18pom4"
OWNER_ID = 6728562312

bot = telebot.TeleBot(BOT_TOKEN)

# --- كود الردود والألعاب الأساسية ---
custom_commands = {}
protection_enabled = True

CUT_TWEET_QUESTIONS = [
    "هل تقدر تعيش أسبوع كامل بدون جوال وإنترنت؟ 🤔",
    "وش أكبر غطة سويتها في حياتك ومحد يدري عنها؟ 🤫",
    "لو خيروك تسافر الحين مع شخص واحد من القروب، من تختار؟ ✈️"
]

JUDGMENTS = [
    "الحكم: غير صورتك الشخصية في تليجرام لصورة مضحكة لمدة 24 ساعة! 🎭",
    "الحكم: أرسل بصمة صوت (فويس) للقروب وأنت تغني فيها لمدة 10 ثواني! 🎤"
]

def is_admin(chat_id, user_id):
    if user_id == OWNER_ID: return True
    try:
        admins = bot.get_chat_administrators(chat_id)
        return any(admin.user.id == user_id for admin in admins)
    except: return False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 البوت شغال الحين على سيرفر Render أونلاين 24 ساعة!")

@bot.message_handler(func=lambda m: m.text and m.text.strip() == 'المطور')
def send_owner(message):
    bot.reply_to(message, f'👤 المالك الرسمي هو: <a href="tg://user?id={OWNER_ID}">موسى</a>', parse_mode="HTML")

@bot.message_handler(func=lambda m: m.text and m.text.strip() in ['كت تويت', 'كت تويك'])
def game_cut(message):
    bot.reply_to(message, f"💬 <b>كت تويت:</b>\n\n{random.choice(CUT_TWEET_QUESTIONS)}", parse_mode="HTML")

@bot.message_handler(func=lambda m: m.text and m.text.strip() in ['احكام', 'حكم'])
def game_judge(message):
    bot.reply_to(message, f"⚖️ <b>حكم:</b>\n\n{random.choice(JUDGMENTS)}", parse_mode="HTML")

@bot.message_handler(func=lambda m: m.text)
def global_handler(message):
    text = message.text.strip().lower()
    if text in ['السلام عليكم', 'سلام عليكم']:
        bot.reply_to(message, "وعليكم السلام ورحمة الله وبركاته، نورت! 👋")
    elif text in ['هاي', 'هلا']:
        bot.reply_to(message, f"هلا والله يا {message.from_user.first_name}! ✨")

# --- إعداد سيرفر وهمي صغير لـ Render عشان ما يطفي ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Running!"

if __name__ == "__main__":
    # تشغيل البوت في الخلفية وسيرفر الويب في الواجهة
    import threading
    threading.Thread(target=bot.infinity_polling, daemon=True).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
