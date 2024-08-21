pip install python-telegram-bot
pip install pyTelegramBotAPI
import telebot
import google.generativeai as genai
pip install google-generativeai python-telegram-bot pyTelegramBotAPI
API_TOKEN = '7409504523:AAGAgx5XgGouc7i2LkVWzoQvTSXlJzpn9bY'
SMART_KEY = 'AIzaSyAQ1It5QqGX_yhKCFOY9hHMGPO34_M2nn0'
from google.colab import userdata
userdata.get('SMART_KEY')
print(dir(genai))
genai.configure(api_key=SMART_KEY)
bot = telebot.TeleBot(API_TOKEN)
# Handle '/start' command
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Hello! I'm your Colab bot. Send me commands!")

# Handle '/run' command to execute code in Colab
@bot.message_handler(commands=['run'])
def handle_run(message):
    bot.reply_to(message, "You can use this command to run code, but it's not yet implemented!")

# Handle all other messages with Gemini AI response
@bot.message_handler(func=lambda message: True)
def handle_all_other_messages(message):
    user_input = message.text

    try:
        # Use the correct method to generate text
        response = genai.generate_text(prompt=user_input)
        print(f"Gemini AI response: {response}")  # Debug: Print the entire response object

        # Check if the response contains generated text
        if 'text' in response:
            bot_reply = response['text'][0]  # Assuming the first item in 'text' is the response
        else:
            bot_reply = "Sorry, I didn't get a response from the AI."

    except Exception as e:
        bot_reply = f"Sorry, I couldn't generate a response due to an error: {e}"
        print(f"Error: {e}")  # Debug: Print the error message

    bot.reply_to(message, bot_reply)

# Start listening for messages
bot.polling()
