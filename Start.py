from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

async def auto_approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()

if __name__ == '__main__':
    app = ApplicationBuilder().token("7802094872:AAEmOJMyP_KVhW6WRe4vDkd7zJMVt6LskEg").build()
    app.add_handler(ChatJoinRequestHandler(auto_approve))
    app.run_polling()
