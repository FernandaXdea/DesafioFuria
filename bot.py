from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests


TOKEN = "7683036669:AAHivrOkx2GPxH6NEDFzZD9uDOrLXoBsNWE"



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = """
    🎮 Olá, fã FURIA! Use um dos comandos:
    /start - Mostra esta mensagem
    /noticias - Últimas notícias do time
    /jogadores - Lista de jogadores
    /agenda - Próximos jogos
    """
    await update.message.reply_text(mensagem)



async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    noticias = [
        "FURIA vence NAVI no Major!",
        "Novo patrocínio com Red Bull.",
        "FURIA anuncia novo técnico."
    ]
    resposta = "📰 ÚLTIMAS NOTÍCIAS:\n\n" + "\n\n".join(noticias)
    await update.message.reply_text(resposta)



async def jogadores(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jogadores = {
        "KSCERATO": "Entry Fragger",
        "yuurih": "AWPer",
        "arT": "IGL",
        "chelo": "Support",
        "VINI": "Rifler"
    }
    resposta = "👾 JOGADORES DA FURIA:\n\n" + "\n".join([f"{nome}: {funcao}" for nome, funcao in jogadores.items()])
    await update.message.reply_text(resposta)


async def agenda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jogos = [
        "10/05 - FURIA vs MIBR",
        "15/05 - FURIA vs Liquid",
        "20/05 - FURIA vs G2"
    ]
    resposta = "📅 PRÓXIMOS JOGOS:\n\n" + "\n".join(jogos)
    await update.message.reply_text(resposta)



if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("noticias", noticias))
    app.add_handler(CommandHandler("jogadores", jogadores))
    app.add_handler(CommandHandler("agenda", agenda))

    print("Bot rodando...")
    app.run_polling()