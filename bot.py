import os
import telebot
from telebot import types

TOKEN=os.getenv("TOKEN")
bot=telebot.TeleBot(TOKEN)

def main_keyboard():
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("馃懆鈥嶐煉� Kepala Sekolah","馃懆鈥嶐煆� Guru")
    kb.row("馃懆鈥嶐煄� Siswa","馃摎 Kelas")
    kb.row("馃彨 SPMB","馃帓 PPDB SMP")
    kb.row("馃搫 Surat","馃摉 Dapodik")
    kb.row("馃挵 Keuangan","馃搮 Agenda")
    kb.row("鈿欙笍 Tools","馃捈 BOS")
    return kb

@bot.message_handler(commands=["start","help"])
def start(message):
    bot.send_message(message.chat.id,"馃彨 OPS-BOT SDN 1 LANGSE\n\nSilakan pilih menu.",reply_markup=main_keyboard())

def balas(m,t):
    bot.reply_to(m,t)

@bot.message_handler(func=lambda m:True)
def menu(message):
    t=message.text
    if t=="馃懆鈥嶐煉� Kepala Sekolah":
        balas(message,"馃懆鈥嶐煉� Menu Kepala Sekolah\nSedang dikembangkan.")
    elif t=="馃懆鈥嶐煆� Guru":
        balas(message,"馃懆鈥嶐煆� Menu Guru")
    elif t=="馃懆鈥嶐煄� Siswa":
        balas(message,"馃懆鈥嶐煄� Menu Siswa")
    elif t=="馃摎 Kelas":
        balas(message,"馃摎 Menu Kelas")
    elif t=="馃彨 SPMB":
        balas(message,"馃彨 Menu SPMB\nSedang dikembangkan.")
    elif t=="馃帓 PPDB SMP":
        balas(message,"馃帓 Menu PPDB SMP\nSedang dikembangkan.")
    elif t=="馃搫 Surat":
        balas(message,"馃搫 Menu Surat")
    elif t=="馃摉 Dapodik":
        balas(message,"馃摉 Menu Dapodik")
    elif t=="馃挵 Keuangan":
        balas(message,"馃挵 Menu Keuangan")
    elif t=="馃搮 Agenda":
        balas(message,"馃搮 Agenda Sekolah")
    elif t=="鈿欙笍 Tools":
        balas(message,"鈿欙笍 TOOLS\n馃彌锔� BMD\n馃搫 Generator Surat\n馃敘 Nomor Surat")
    elif t=="馃捈 BOS":
        balas(message,"馃捈 Menu BOS")
    else:
        balas(message,"Silakan pilih menu.")

bot.infinity_polling()
