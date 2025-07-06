from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '7763417903:AAFji0twD3pYdaPwDUWnOqt8nhMo-M3reMQ'

def start(update, context):
    user = update.message.from_user
    print(f"👤 User started the bot: {user.first_name} (Username: @{user.username}, ID: {user.id})")
    update.message.reply_text("👋 Hello! Your bot is working!")

def handle_message(update, context):
    update.message.reply_text("💬 I'm still learning!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    updater.bot.set_my_commands([
        ("start", "Start the bot"),
    ])

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    print("✅ Bot is running...")
    updater.idle()

if __name__ == '__main__':
    main()
