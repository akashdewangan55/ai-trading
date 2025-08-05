from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import 7710160278:AAEuNEnQOfIz2zNMWGWLLNCiNwiBn_4h-gw
from predictor import predict_color_number
from database import log_trade, get_stats

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Welcome to AI Trading Predictor Bot! Use /predict to get a prediction.")

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = predict_color_number()
    await update.message.reply_text(f"🎯 Predicted Color: {result['color']}\n🎯 Predicted Number: {result['number']}\nConfidence: {result['confidence']*100:.1f}%")

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stats_text = get_stats()
    await update.message.reply_text(stats_text)

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("predict", predict))
    app.add_handler(CommandHandler("stats", stats))
    app.run_polling()

if __name__ == "__main__":
    main()