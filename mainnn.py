import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# =================================================================
# !! ضع التوكن الخاص بك هنا !!
# =================================================================
BOT_TOKEN = "8383225800:AAH1k4V60K4-E5RzGxQpONsaCVpCCR5hHeo" 

# =================================================================
# !! قائمة الروابط - تم تعديلها لتشمل تقسيم مادة السيركت !!
# =================================================================
DRIVE_LINKS = {
    # --- !! تم التعديل هنا !! ---
    "Circuit": {
        "type": "nested", # تم تغيير النوع ليسمح بالتداخل
        "resources": {
            "محاضرات": {
                "Dr Lotfy": "https://drive.google.com/drive/folders/1MIdq0uhqq3L6DEdj5Fs_3ATeCgvsyUtf?usp=drive_link",
                "Dr Mohammed Farahat": "https://drive.google.com/drive/folders/1ex7Bqqn0F0ppMA7MVR-mwHpReDyEFO6m?usp=drive_link",
                "Dr Mohey": "https://drive.google.com/drive/folders/1E5UVz-WOHIgk8a_YjbnpDq47RauKvUEt?usp=drive_link",
                "Dr Enas": "URL_Cirhttps://drive.google.com/drive/folders/1kDx_xY06FBmMCPef5uDd87Wur2HL3Ih5?usp=drive_linkcuit_Lec_Enas",
                "Dr Nihad": "https://drive.google.com/drive/folders/1Qke2Cf7yeGpw8wQKisBvAuNcOuBCaExT?usp=drive_link"
            },
            "مذكرات": {
                "Eng Elkholi": "https://drive.google.com/drive/folders/169ZONXx_BzOLkHzNw7M6vNTivTwqyp17?usp=drive_link",
                "Eng Mohamed Gameel": "https://drive.google.com/drive/folders/1viXVe6NADXTnnt1L6EOpHE9ormUAoCnq?usp=drive_link",
                "Eng Taisir": "https://drive.google.com/drive/folders/1WzD4unJm6BlpuzYzABlhsnS6T5geHHMx?usp=drive_link"
            },
            "شيتات": "https://drive.google.com/drive/folders/1eS2gpgVtVKca71DP5IGiGsoXk-ZMLOso?usp=drive_link", # رابط مباشر
            "امتحانات": "https://drive.google.com/drive/folders/1vJAuOBMM9eC09VnS9wb4YykazOUpz5kc?usp=drive_link"  # رابط مباشر
        }
    },
    # --- مادة الرياضيات (كما هي) ---
    "Math 3": {
        "type": "nested",
        "resources": {
            "محاضرات": {
                "Dr Rabab": {
                    "Chapter 3": {
                        "lecture 1": "https://drive.google.com/drive/folders/1R6Kt5nh30dtjI_uVHdkWonnocI5DRd-T?usp=drive_link", 
                        "lecture 2": "https://drive.google.com/drive/folders/1JPN-Cpa8O8QO1vIXI_O_wAsCow4WkPaj?usp=drive_link",
                        "lecture 3": "https://drive.google.com/drive/folders/1gWFPsHooUyj0J7VmSwWSfYYPSofM47aU?usp=drive_link", 
                        "lecture 4": "https://drive.google.com/drive/folders/1guXA6memlz36V6F18axb4gPxv5QOLFkV?usp=drive_link",
                        "lecture 5": "https://drive.google.com/drive/folders/1Zw_KY9UzzRBM-RonKJ5Sc8XApi9rqeT5?usp=drive_link",
                    },
                    "Chapter 4": "https://drive.google.com/drive/folders/1YqLta9eFrYukxm22XXpY2nfhplCsuiXh?usp=drive_link",
                    "Chapter 5": {
                        "lecture 8": "https://drive.google.com/drive/folders/1s3ZfwNyAQRFPpvNUyOOmJ_7oqXne5rhR?usp=drive_link", 
                        "lecture 9": "https://drive.google.com/drive/folders/1e9h0JGAcwybXPbpHoS9DHQJI12G-VM0T?usp=drive_link",
                        "lecture 10": "https://drive.google.com/drive/folders/1HJ6s74AbPYdEo4WzFHEZKvW4vX3LWW8j?usp=drive_link",
                    },
                },
                "Dr Nazera": {
                    "Chapter 1": {
                        "lecture 1": "https://drive.google.com/drive/folders/1i41mxJljgn-I08u7zvBGqpEBy8BMPZb2?usp=drive_link", 
                        "lecture 2": "https://drive.google.com/drive/folders/1eDdeX3qprZWVJdhAnFPK94nZCrfWAzxX?usp=drive_link",
                        "lecture 3": "https://drive.google.com/drive/folders/1AIkUIhGnKAkaS0OboDY9g1DCsmxvGWXY?usp=drive_link", 
                        "lecture 4": "https://drive.google.com/drive/folders/1mWegdZPM9Ndy6KpGNTsBvEnKEY_WooIM?usp=drive_link",
                        "lecture 5": "https://drive.google.com/drive/folders/17lTKWlPDJKwYXUn4l4EgIo1HAZtL-o3N?usp=drive_link",
                    },
                    "Chapter 2": {
                        "lecture 6": "https://drive.google.com/drive/folders/1mC1wt_yjAVxN9Y1XKUpBZ0nkL88JW1VZ?usp=drive_link", 
                        "lecture 7": "https://drive.google.com/drive/folders/1BT1zRL02V3xfurbMIUBd0G7scTAOyCx4?usp=drive_link",
                        "lecture 8": "https://drive.google.com/drive/folders/11zqJU1Xvh6ygvQ6oXInuut1udJYaXgMu?usp=drive_link", 
                        "lecture 9": "https://drive.google.com/drive/folders/1uGCIsXThULZPcPVYnMtg5bN7n_SkGHTr?usp=drive_link",
                    }
                }
            },
            "الكتاب": "https://drive.google.com/file/d/1Mij6o1Flh_28JC7wCMnF1XCxsLijoR7F/view?usp=drive_link",
            "مذكرات": {
                "Chapter 1": "https://drive.google.com/drive/folders/1Apf_pv81vvM0otQngErhMlJBGr-70Qpk?usp=drive_link",
                "Chapter 2": "https://drive.google.com/drive/folders/12C8hIheZ5fv-_S4ufzWERNKDIkaqkVWt?usp=drive_link",
                "Chapter 3": "https://drive.google.com/drive/folders/1LF-QR8F74o696p5jHMqROyE1dyIQ5Sia?usp=drive_link",
                "Chapter 4": "https://drive.google.com/drive/folders/1Kklu4e_Tg8htu3vskdwhWzbxhSQdbOlv?usp=drive_link",
                "Chapter 5": "https://drive.google.com/drive/folders/1vNj9Qo_ywZ5PmStCKStLixEhz1mClVt4?usp=drive_link",
            },
            "امتحانات": "https://drive.google.com/drive/folders/1gZwkh6uENiL-ieI1CgTqnXqlk1sAm8Ln?usp=drive_link",
        }
    }
}
# =================================================================

# --- باقي الكود (بدون أي تغيير) ---
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# --- دوال مساعدة للتنقل ---
async def show_subjects_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subjects = list(DRIVE_LINKS.keys())
    keyboard = [[KeyboardButton(s)] for s in subjects] + [[KeyboardButton("رجوع للقائمة الرئيسية")]]
    await update.message.reply_text("اختر المادة:", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

async def show_resource_types_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, subject):
    resources = list(DRIVE_LINKS[subject]['resources'].keys())
    keyboard = [[KeyboardButton(r)] for r in resources] + [[KeyboardButton("رجوع للمواد")]]
    await update.message.reply_text(f"اختر نوع المحتوى لمادة {subject}:", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

async def show_doctors_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, subject, resource):
    doctors = list(DRIVE_LINKS[subject]['resources'][resource].keys())
    keyboard = [[KeyboardButton(d)] for d in doctors] + [[KeyboardButton(f"رجوع لمحتوى {subject}")]]
    await update.message.reply_text("اختر الدكتور:", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

async def show_chapters_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, subject, resource, doctor):
    chapters = list(DRIVE_LINKS[subject]['resources'][resource][doctor].keys())
    keyboard = [[KeyboardButton(c)] for c in chapters] + [[KeyboardButton("رجوع للدكاترة")]]
    await update.message.reply_text("اختر الشابتر:", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

async def show_lectures_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, subject, resource, doctor, chapter):
    lectures = list(DRIVE_LINKS[subject]['resources'][resource][doctor][chapter].keys())
    keyboard = [[KeyboardButton(l)] for l in lectures] + [[KeyboardButton("رجوع للشباتر")]]
    await update.message.reply_text("اختر المحاضرة:", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

# --- الدالة الرئيسية والتعامل مع الرسائل ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.clear()
    keyboard = [[KeyboardButton("الترم الأول")], [KeyboardButton("الترم الثاني (قريباً)")]]
    await update.message.reply_text("ازيك يا بشمهندس صباح الخير ❤️", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text
    ud = context.user_data

    # --- أزرار الرجوع الأساسية ---
    if message_text == "الترم الأول": await show_subjects_menu(update, context); return
    if message_text == "رجوع للقائمة الرئيسية": await start(update, context); return
    if message_text == "رجوع للمواد": ud.clear(); await show_subjects_menu(update, context); return
    
    # --- منطق التنقل المتداخل ---
    subject = ud.get('subject')
    resource = ud.get('resource')
    doctor = ud.get('doctor')
    chapter = ud.get('chapter')

    # أزرار الرجوع المتداخلة
    if subject and message_text == f"رجوع لمحتوى {subject}": ud.pop('resource', None); await show_resource_types_menu(update, context, subject); return
    if doctor and message_text == "رجوع للدكاترة": ud.pop('doctor', None); await show_doctors_menu(update, context, subject, resource); return
    if chapter and message_text == "رجوع للشباتر": ud.pop('chapter', None); await show_chapters_menu(update, context, subject, resource, doctor); return

    # 5. اختيار المحاضرة (المستوى الأخير)
    if chapter:
        lectures = DRIVE_LINKS[subject]['resources'][resource][doctor][chapter]
        if message_text in lectures:
            link = lectures[message_text]
            await update.message.reply_text(f"🔗 رابط {message_text}:\n{link}")
        return

    # 4. اختيار الشابتر
    if doctor:
        chapters = DRIVE_LINKS[subject]['resources'][resource][doctor]
        if message_text in chapters:
            chapter_content = chapters[message_text]
            if isinstance(chapter_content, str):
                await update.message.reply_text(f"🔗 رابط {message_text}:\n{chapter_content}")
            elif isinstance(chapter_content, dict):
                ud['chapter'] = message_text
                await show_lectures_menu(update, context, subject, resource, doctor, message_text)
        return

    # 3. اختيار الدكتور (أو الشابتر في حالة المذكرات)
    if resource:
        next_level_data = DRIVE_LINKS[subject]['resources'][resource]
        if message_text in next_level_data:
            selected_item_content = next_level_data[message_text]
            
            if isinstance(selected_item_content, str):
                await update.message.reply_text(f"🔗 رابط {message_text}:\n{selected_item_content}")

            elif isinstance(selected_item_content, dict):
                ud['doctor'] = message_text # نفترض أنه دكتور وننتقل للمستوى التالي
                await show_chapters_menu(update, context, subject, resource, message_text)
        return

    # 2. اختيار نوع المحتوى
    if subject:
        resources = DRIVE_LINKS[subject]['resources']
        if message_text in resources:
            resource_content = resources[message_text]
            if isinstance(resource_content, str):
                await update.message.reply_text(f"🔗 رابط {message_text}:\n{resource_content}")
            elif isinstance(resource_content, dict):
                ud['resource'] = message_text
                next_level_keys = list(resource_content.keys())
                keyboard = [[KeyboardButton(k)] for k in next_level_keys] + [[KeyboardButton(f"رجوع لمحتوى {subject}")]]
                await update.message.reply_text("اختر:", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))
        return
    
    # 1. اختيار المادة
    if message_text in DRIVE_LINKS:
        ud['subject'] = message_text
        subject_data = DRIVE_LINKS[message_text]
        if subject_data['type'] == 'standard':
            await update.message.reply_text(f"روابط {message_text}:\n" + "\n".join([f"{k}: {v}" for k, v in subject_data['links'].items()]))
            ud.clear()
        elif subject_data['type'] == 'nested':
            await show_resource_types_menu(update, context, message_text)
        return

def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is starting...")
    application.run_polling()
   

if __name__ == "__main__":
    main()