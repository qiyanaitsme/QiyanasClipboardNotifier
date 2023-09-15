import bot

def run_bot():
    bot.send_message_to_bot("Жду данных из буфера обмена.")
    last_clipboard_content = ""
    while True:
        content = bot.check_clipboard()
        if content != last_clipboard_content:
            bot.send_message_on_clipboard_change(content)
            last_clipboard_content = content

if __name__ == '__main__':
    run_bot()