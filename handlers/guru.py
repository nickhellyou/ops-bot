from telebot import types

def register(bot):

    @bot.message_handler(commands=['guru'])
        def guru(message):
                text = """
                👨‍🏫 GURU DAN KARYAWAN SDN 1 LANGSE

                1. Ahmad Junaidi, S.Pd.
                2. Marsiah, S.Pd.
                3. Puji Lestari, S.Pd.
                4. Eka Priawan, S.Pd.
                5. Andin Setyowati, S.Pd.
                6. Desti Nur Islami, S.Pd.
                7. Nani Hidayani, S.Pd.I.
                8. Kristiana Dewi, S.A.P.
                9. Rizal Agustianto (PJK)
                10. Zaenal ...

                Ketik /start untuk kembali ke menu utama.
                """
                        bot.reply_to(message, text)
