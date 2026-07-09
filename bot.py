k
m	mport os
import telebot
from telebot import types

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

def main_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("Kepala Sekolah", "Guru")
    kb.row("Siswa", "Kelas")
    kb.row("SPMB", "PPDB SMP")
    kb.row("Surat", "Dapodik")
    kb.row("Keuangan", "Tools")
    kb.row("Agenda", "BOS")
    return kb

@bot.message_handler(commands=["start", "help"])
def start(message):
    bot.send_message(
        message.chat.id,
        "OPS-BOT SDN 1 LANGSE\n\nSilakan pilih menu.",
        reply_markup=main_keyboard()
    )

def balas(m, t):
    bot.reply_to(m, t)

@bot.message_handler(func=lambda m: True)
def menu(message):
    t = message.text

    if t == "Kepala Sekolah":
        balas(message, "Ahmad Junaedi Fatah, S.Pd. SD.\nSedang dikembangkan.")

    elif t == "Guru":
        balas(message, "Urung di-update lurrr")

    elif t == "Siswa":
        balas(message, "Ken Zura disit nggo isi-isi")

    elif t == "Kelas":
        balas(message, "fitur ke depan untuk manage perkelas")

    elif t == "SPMB":
        balas(message, "kira-kira penting ora ya?\nSedang dikembangkan.")

    elif t == "PPDB SMP":
        balas(message, "kie sing nggawe Pak Eka puyeng wkwkwk\nSedang dikembangkan.")

    elif t == "Surat":
        balas(message, "fitur generate semua surat. Tinggal kasih prompt: buat surat tugas diklat untuk Pak Jun. Langsung dibikin sama AI")

    elif t == "Dapodik":
        balas(message, "fitur dapodik berikut link dll")

    elif t == "Keuangan":
        balas(message, "kie jatahe Bu Mar")

    elif t == "Agenda":
        balas(message, "bisa jadwal lomba, TKA, anbk, dll")

    elif t == "Tools":
        balas(message, "kie sing dadi master bot")

    elif t == "BOS":
        balas(message, "jatahe juragan Bu Puji")

    else:
        balas(message, "Silakan pilih menu.")

bot.infinity_polling()
