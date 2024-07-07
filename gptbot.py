import telebot
import openai

TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'

# Инициализация бота
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Установка ключа API для OpenAI
openai.api_key = OPENAI_API_KEY

# Базовый промт для бота
BASE_PROMPT = "Ты ассистент, который помогает в поиске информации. Ответь на вопросы пользователя."

# Функция для получения ответа от ChatGPT
def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Используйте нужную версию модели
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, использующий модель ChatGPT. Задай мне вопрос!")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text
    prompt = f"{BASE_PROMPT}\n\nПользователь: {user_message}\nБот:"
    bot_response = get_chatgpt_response(prompt)
    bot.reply_to(message, bot_response)

# Запуск бота
if __name__ == "__main__":
    bot.polling()