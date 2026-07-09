import os
import telebot
from telebot import types

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row("🏫 Profil", "👨‍🏫 Guru")
    keyboard.row("👨‍🎓 Siswa", "📚 Kelas")
    keyboard.row("📋 Absensi", "🎓 MPLS")
    keyboard.row("📄 Surat", "📖 Dapodik")
    keyboard.row("💰 BOS", "☎️ Kontak")

     bot.send_message(
       message.chat.id,
       "🏫 BOT OPERATOR SDN 1 LANGSE\n\nSilakan pilih menu.",
                                                        reply_markup=keyboard
                                                            )
                            )

@bot.message_handler(commands=['kepsek'])
def kepsek(message):
    text = """
👨‍💼 KEPALA SEKOLAH

Nama :
Ahmad Junaedi Fatah, S.Pd.SD

NIP :
-

Alamat :
-

Ketik /start untuk kembali.
"""
    bot.reply_to(message, text)


@bot.message_handler(commands=['guru'])
def guru(message):
    text = """
👨‍🏫 DATA GURU SDN 1 LANGSE

1. Ahmad Junaedi Fatah, S.Pd.SD (Kepsek)
2. Marsiah, S.Pd.
3. Puji Lestari, S.Pd.
4. Eka Priawan, S.Pd.
5. Andin Setyowati, S.Pd.
6. Desti Nur Islami, S.Pd.
7. Nani Hidayani, S.Pd.I.
8. Kristiana Dewi, S.A.P.
9. Rizal Agustianto (PJOK)
10. Zaenal

Ketik /start untuk kembali.
"""
    bot.reply_to(message, text)


@bot.message_handler(commands=['siswa'])
def siswa(message):
    bot.reply_to(message,
"""👨‍🎓 MENU SISWA

Fitur sedang dikembangkan.

Ketik /start untuk kembali.
""")


@bot.message_handler(commands=['kelas'])
def kelas(message):
    bot.reply_to(message,
"""📚 DATA KELAS

Kelas 1
Kelas 2
Kelas 3
Kelas 4
Kelas 5
Kelas 6

Ketik /start untuk kembali.
""")


@bot.message_handler(commands=['absen'])
def absen(message):
    bot.reply_to(message,
"""📋 ABSENSI

Menu absensi akan segera tersedia.

Ketik /start untuk kembali.
""")


@bot.message_handler(commands=['komite'])
def komite(message):
    text = """
👥 KOMITE SDN 1 LANGSE

Ketua :
Wasimin

Wakil Ketua :
Sutomo
Hantoro

Ketik /start untuk kembali.
"""
    bot.reply_to(message, text)


@bot.message_handler(commands=['dapodik'])
def dapodik(message):
    bot.reply_to(message,
"""📖 DAPODIK

Menu Dapodik.

Ketik /start untuk kembali.
""")


@bot.message_handler(commands=['surat'])
def surat(message):
    bot.reply_to(message,
"""📄 SURAT

Menu Surat Menyurat.

Ketik /start untuk kembali.
""")


@bot.message_handler(commands=['bos'])
def bos(message):
    bot.reply_to(message,
"""💰 DANA BOS

Menu BOS.

Ketik /start untuk kembali.
""")


@bot.message_handler(commands=['mpls'])
def mpls(message):
    bot.reply_to(message,
"""🎓 MPLS

Menu MPLS.

Ketik /start untuk kembali.
""")


@bot.message_handler(commands=['kontak'])
def kontak(message):
    text = """
☎️ KONTAK SDN 1 LANGSE

Alamat :
Desa Langse, Glagahamba RT 04

WhatsApp :
08xxxxxxxxxx

Email :
sdn1langse@gmail.com

Website :
-

Ketik /start untuk kembali.
"""
    bot.reply_to(message, text)


@bot.message_handler(commands=['medsos'])
def medsos(message):
    text = """
🌐 MEDIA SOSIAL

Facebook :
SDN 1 Langse

Instagram :
-

TikTok :
-

YouTube :
-

Ketik /start untuk kembali.
"""
    bot.reply_to(message, text)


@bot.message_handler(commands=['eraport'])
def eraport(message):
    bot.reply_to(message,
"""📝 E-RAPORT

Menu E-Raport.

Ketik /start untuk kembali.
""")


@bot.message_handler(commands=['keuangan'])
def keuangan(message):
    bot.reply_to(message,
"""💵 KEUANGAN

Menu Keuangan Sekolah.

Ketik /start untuk kembali.
""")


print("Bot Operator SDN 1 Langse berjalan...")
bot.infinity_polling()
