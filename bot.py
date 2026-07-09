import os
import telebot
from telebot import types

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

def main_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("🏫 Profil", "👨‍🏫 Guru")
    kb.row("👨‍🎓 Siswa", "📚 Kelas")
    kb.row("📋 Absensi", "🎓 MPLS")
    kb.row("📄 Surat", "📖 Dapodik")
    kb.row("💰 BOS", "☎️ Kontak")
    return kb

@bot.message_handler(commands=["start","help"])
def start(message):
    bot.send_message(message.chat.id,
                     "🏫 BOT OPERATOR SDN 1 LANGSE\n\nSilakan pilih menu.",
                     reply_markup=main_keyboard())

@bot.message_handler(commands=["kepsek"])
def kepsek(message):
    bot.reply_to(message,"👨‍💼 KEPALA SEKOLAH\n\nAhmad Junaedi Fatah, S.Pd.SD")

@bot.message_handler(commands=["guru"])
def guru(message):
    bot.reply_to(message,"👨‍🏫 DATA GURU\n1. Ahmad Junaedi Fatah, S.Pd.SD (Kepala Sekolah)\n2. Marsiah, S.Pd.\n3. Puji Lestari, S.Pd.\n4. Eka Priawan, S.Pd.\n5. Andin Setyowati, S.Pd.\n6. Desti Nur Islami, S.Pd.\n7. Nani Hidayani, S.Pd.I.\n8. Kristiana Dewi, S.A.P.\n9. Rizal Agustianto (PJOK)\n10. Zaenal")

@bot.message_handler(commands=["siswa"])
def siswa(message): bot.reply_to(message,"👨‍🎓 Menu siswa masih dalam pengembangan.")

@bot.message_handler(commands=["kelas"])
def kelas(message): bot.reply_to(message,"📚 Kelas 1\n📚 Kelas 2\n📚 Kelas 3\n📚 Kelas 4\n📚 Kelas 5\n📚 Kelas 6")

@bot.message_handler(commands=["absen"])
def absen(message): bot.reply_to(message,"📋 Menu Absensi")

@bot.message_handler(commands=["mpls"])
def mpls(message): bot.reply_to(message,"🎓 Menu MPLS")

@bot.message_handler(commands=["surat"])
def surat(message): bot.reply_to(message,"📄 Menu Surat")

@bot.message_handler(commands=["dapodik"])
def dapodik(message): bot.reply_to(message,"📖 Menu Dapodik")

@bot.message_handler(commands=["bos"])
def bos(message): bot.reply_to(message,"💰 Menu BOS")

@bot.message_handler(commands=["kontak"])
def kontak(message): bot.reply_to(message,"☎️ Kontak SDN 1 Langse")

@bot.message_handler(func=lambda m: True)
def menu(message):
    t=message.text
    if t=="🏫 Profil": kepsek(message)
    elif t=="👨‍🏫 Guru": guru(message)
    elif t=="👨‍🎓 Siswa": siswa(message)
    elif t=="📚 Kelas": kelas(message)
    elif t=="📋 Absensi": absen(message)
    elif t=="🎓 MPLS": mpls(message)
    elif t=="📄 Surat": surat(message)
    elif t=="📖 Dapodik": dapodik(message)
    elif t=="💰 BOS": bos(message)
    elif t=="☎️ Kontak": kontak(message)

print("Bot Operator SDN 1 Langse berjalan...")
bot.infinity_polling()
