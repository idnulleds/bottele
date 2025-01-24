from telegram.ext import Updater, CommandHandler

# Token bot dari BotFather
TOKEN = '7723104250:AAGUjNZnYMsmoy7vnto7cFb6V4BoBhheYaQ'  # Ganti dengan token bot Anda

# Fungsi yang akan dijalankan saat pengguna mengetik /start
def start(update, context):
    user = update.effective_user  # Mendapatkan informasi pengguna
    chat_id = update.effective_chat.id  # Mendapatkan chat ID

    # Pesan balasan
    message = (
        f"👋 Halo, {user.first_name}!\n\n"
        f"Berikut adalah informasi Anda:\n"
        f"- Username: @{user.username if user.username else 'Tidak ada'}\n"
        f"- ID Chat: {chat_id}\n"
    )

    # Kirim pesan ke pengguna
    context.bot.send_message(chat_id=chat_id, text=message)

# Main function untuk menjalankan bot
def main():
    updater = Updater(token=TOKEN, use_context=True)

    # Tambahkan handler untuk command /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Mulai polling
    print("Bot sedang berjalan...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
