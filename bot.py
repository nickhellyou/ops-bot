import os
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
    kb.row("Keuangan", "Agenda")
    kb.row("Tools", "BOS")
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
        balas(message, "Menu Kepala Sekolah\nSedang dikembangkan.")

    elif t == "Guru":
        balas(message, "Menu Guru")

    elif t == "Siswa":
        balas(message, "Menu Siswa")

    elif t == "Kelas":
        balas(message, "Menu Kelas")

    elif t == "SPMB":
        balas(message, "Menu SPMB\nSedang dikembangkan.")

    elif t == "PPDB SMP":
        balas(message, "Menu PPDB SMP\nSedang dikembangkan.")

    elif t == "Surat":
        balas(message, "Menu Surat")

    elif t == "Dapodik":
        balas(message, "Menu Dapodik")

    elif t == "Keuangan":
        balas(message, "Menu Keuangan")

    elif t == "Agenda":
        balas(message, "Agenda Sekolah")

    elif t == "Tools":
        balas(
            message,
            "TOOLS\n"
            "- BMD\n"
            "- Generator Surat\n"
            "- Nomor Surat"
        )

    elif t == "BOS":
        balas(message, "Menu BOS")

    else:
        balas(message, "Silakan pilih menu.")

bot.infinity_polling()
