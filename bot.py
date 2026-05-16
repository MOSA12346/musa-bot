import telebot
import random

# التوكن حقك مضبوط وجاهز
TOKEN = '7611796590:AAEmh_Z3w2eX3tXW2TqA3u9F3fXN_Z8LwM8'
bot = telebot.TeleBot(TOKEN)

# قائمة ألعاب كت تويت
cut_tweet = [
    "لو خيروك تعيش في جزيرة لحالك أو مع شخص تكرهه؟",
    "وش أكثر شيء يرفع ضغطك في الجروبات؟",
    "أخر أكلة أكلتها وش كانت؟",
    "أكبر مغامرة سويتها في حياتك وش هي؟",
    "لو ربحت مليون ريال الحين وش أول شيء بتشتريه؟"
]

# قائمة ألعاب لو خيروك
choose_game = [
    "لو خيروك: تاكل شطة حارة بالملعقة 🌶️ أو ليمونة كاملة بقشرها 🍋؟",
    "لو خيروك: تعيش بدون جوال أسبوع 📱 أو بدون مكيف بالصيف ☀️؟",
    "لو خيروك: تسافر للمستقبل 🚀 أو ترجع للماضي ⏳؟"
]

# قائمة الأحكام
rules_game = [
    "نفذ: غير اسمك بالجروب إلى 'أنا فنان' لمدة ساعة 😂",
    "نفذ: ارسل آخر صورة في الاستوديو عندك بدون غش 📸",
    "نفذ: أرسل بصمة صوت تقول فيها (يا ليل ما أطولك) بصوت عالي 🎤"
]

# 1. أمر الترحيب بالعضو الجديد
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for member in message.new_chat_members:
        name = member.first_name
        bot.reply_to(message, f"✨ يا هلا وغلا بالمنور الجديد {name}! نورت الجروب يا غالي 🌹")

# 2. أمر المغادرة
@bot.message_handler(content_types=['left_chat_member'])
def member_left(message):
    name = message.left_chat_member.first_name
    bot.send_message(message.chat.id, f"🚶‍♂️ العضو {name} غادرنا.. بالتوفيق له.")

# 3. الردود التفاعلية والألعاب
@bot.message_handler(func=lambda message: True)
def reply_to_all(message):
    text = message.text.strip()
    
    # ردود عامة
    if text == "السلام عليكم":
        bot.reply_to(message, "وعليكم السلام ورحمة الله وبركاته، يا هلا والله وغلا! 👋")
    elif text == "هلا" or text == "هلاو":
        bot.reply_to(message, "هلا بك زود يا غالي، منور الجروب! ❤️")
    elif text == "المطور":
        bot.reply_to(message, "👑 مطور البوت والزعيم هو الكفو: موسى!")
    elif text == "منور":
        bot.reply_to(message, "النور نورك ونور الأعضاء يا بعد قلبي ✨")
    elif text == "هههه" or text == "ههههه" or text == "هههههه":
        bot.reply_to(message, "عساها دوم الضحكة يا رب 😂❤️")
    elif text == "ماتشتغل" or text == "ما يشتغل":
        bot.reply_to(message, "كل شيء شغال تمام يا وحش، جرب الأوامر الحين!")
        
    # أوامر الألعاب
    elif text == "كت تويت":
        bot.reply_to(message, f"🤔 | {random.choice(cut_tweet)}")
    elif text == "لو خيروك":
        bot.reply_to(message, f"⚖️ | {random.choice(choose_game)}")
    elif text == "احكام" or text == "أحكام":
        bot.reply_to(message, f"⚖️ | {random.choice(rules_game)}")
        
    # أمر الأيدي
    elif text == "ايدي" or text == "الايدي" or text == "id":
        user_id = message.from_user.id
        name = message.from_user.first_name
        bot.reply_to(message, f"👤 اسمك: {name}\n🆔 أيديك: `{user_id}`", parse_mode="Markdown")

print("البوت شغال الحين بنجاح...")
bot.infinity_polling()
