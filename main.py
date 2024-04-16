from telegram import ReplyKeyboardMarkup, Update, Bot, KeyboardButton
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)


import logging
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'common.settings')
django.setup()
from data.models import User, Category


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
MENU = "🍴 Menyu"
BASKET = "📥 Savat"
REQUEST_LOCATION = "📍 Manzilini yuborish"
LOCATION = "KAFE LOKATSIYASI"
ABOUT_ORDER = "🚀 Buyurtma haqida"
ADVICE = "✍️Fikr bildirish"
CONTACT = "☎️Kontaktlar"
SETTINGS = "⚙️ Sozlamalar"

MAIN_KEYBOARD = [
    [
        MENU,
        BASKET,
    ],
    [LOCATION, ABOUT_ORDER],
    [ADVICE, CONTACT],
    [SETTINGS]
]

ZOR_5 = "😊Hammasi yoqdi ❤️"
ZOR_4 = "☺️Yaxshi ⭐️⭐️⭐️⭐️"
ZOR_3 = "😐 Yoqmadi ⭐️⭐️⭐️"
ZOR_2 = "☹️ Yomon ⭐️⭐️"
ZOR_1 = "😤 Juda yomon👎🏻"
HOME = "🏠 Bosh menu"


MARKS = [[ZOR_5], [ZOR_4], [ZOR_3], [ZOR_2], [ZOR_1]]

categories = Category.objects.all()
CATE_BUTTONS = []
for x in range(0, len(categories)-1, 2):
    CATE_BUTTONS.append([categories[x], categories[x+1]])


def start(update: Update, context: CallbackContext):
    """Starts the conversation and asks the user about their gender."""
    update.message.reply_text(
        "Kerakli bo'limni tanlang",
        reply_markup=ReplyKeyboardMarkup(
            MAIN_KEYBOARD,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",
        ),
    )

    User.objects.create(
        first_name=update.message.from_user.first_name,
        last_name=update.message.from_user.last_name,
        nick_name=update.message.from_user.username,
    )


def menu(update: Update, context: CallbackContext):

    update.message.reply_text(""
                                  "🇮🇹 Italiyani yetkazib berish!\n,"
                                  "🍝 Italiyancha pasta korobochkalarda!\n"
                                  "⏰ С 11:00 до 01:00\n"
                                  "🛵 Hoziroq buyurtma bering!\n"
                                  "\n*Ob havo va yo'l tirbandliklar sababli yetkazish narxi o'zgarishi mumkin\n\n"
                                  "Qaysi manzilga yetkazilsin?\n"
                                  "Manzilni kiriting yoki \'📍 Manzilini yuborish\' tugmachasini bosing 👇🏻",
                                  reply_markup=ReplyKeyboardMarkup([[
                                      KeyboardButton(REQUEST_LOCATION, request_location=True)]],
                                    one_time_keyboard=True,
                                    resize_keyboard=True,
                                  ))


def menu_list(update, context):
    update.message.reply_html(
                "🇮🇹 Italiyani yetkazib berish!\n"
                "🍝 Italiyancha pasta korobochkalarda!\n"
                "⏰ С 11:00 до 01:00\n "
                "🛵 Hoziroq buyurtma bering!\n "
                "*Ob havo va yo'l tirbandliklar sababli yetkazish narxi o'zgarishi mumkin",

                reply_markup=ReplyKeyboardMarkup(
                    CATE_BUTTONS,
                    one_time_keyboard=False,
                    input_field_placeholder="Quyidagilardan birini tanlang",
                    resize_keyboard=True
                    )
                    )


def user_locations(update: Update, context: CallbackContext):
    user_location = update.message.location
    chat_id = update.message.from_user.id

    bot = Bot(token='6435050827:AAGIu4VhD3WpWXkHnCXPM9mmdp8vnkkQU0A')
    bot.send_location(chat_id=chat_id, latitude=user_location.latitude, longitude=user_location.longitude)


def about_order(update: Update, context: CallbackContext):

    update.message.reply_html(
                "🇮🇹 Italiyani yetkazib berish!\n"
                "🍝 Italiyancha pasta korobochkalarda!\n"
                "⏰ С 11:00 до 01:00\n "
                "🛵 Hoziroq buyurtma bering!\n "
                "*Ob havo va yo'l tirbandliklar sababli yetkazish narxi o'zgarishi mumkin",

                reply_markup=ReplyKeyboardMarkup(
                    MAIN_KEYBOARD,
                    one_time_keyboard=False,
                    input_field_placeholder="Quyidagilardan birini tanlang",
                    resize_keyboard=True
                    )
                    )


def basket(update: Update, context: CallbackContext):

    update.message.reply_text(
        """Sizning savatingiz bo'sh""",
        reply_markup=ReplyKeyboardMarkup(
            MAIN_KEYBOARD,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",
            resize_keyboard=True
        ),
    )


def contact(update: Update, context: CallbackContext):

    update.message.reply_html(
                    "Buyurtma va boshqa savollar bo'yicha javob olish uchun \n@sakhibdev ga"
                    "murojaat qiling, barchasiga javob beramiz :)",

                    reply_markup=ReplyKeyboardMarkup(
                        MAIN_KEYBOARD,
                        one_time_keyboard=False,
                        resize_keyboard=True
                        ),
                            )


def fikr_bildirish(update: Update, context: CallbackContext) -> int:

    update.message.reply_html(
                    "✅ PASTA-PASTA ni tanlaganingiz uchun rahmat.\n"
                    "Agar Siz bizning xizmatlarimiz sifatini yaxhshilashga yordam\n"
                    " bersangiz benihoyat hursand bo’lamiz.\n"
                    "Buning uchun 5 ballik tizim asosida bizni baholang",

                    reply_markup=ReplyKeyboardMarkup(
                        MARKS,
                        one_time_keyboard=False,
                        resize_keyboard=True
                        ),
                            )

    return FIKR_BILDIRISH


def marking5(update: Update, context: CallbackContext) -> int:

    update.message.reply_html(
        "Yoqganidan hursandmiz 😊. Nima deb o'ylaysiz, xizmatimizni\n"
        " yanada qulay va yaxshiroq qilishimiz uchun yana \n"
        "nima qilishimiz kerak?\nTaklif va shikoyatlar uchun @sakhibdev ga murojaat qiling",
        reply_markup=ReplyKeyboardMarkup(
            MAIN_KEYBOARD,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",
        ),
    )
    return ConversationHandler.END


def marking4(update: Update, context: CallbackContext) -> int:

    update.message.reply_text(
        """Bahoyingiz uchun rahmat""",
        reply_markup=ReplyKeyboardMarkup(
            MAIN_KEYBOARD,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",
        ),
    )
    return ConversationHandler.END


def marking3(update: Update, context: CallbackContext) -> int:

    update.message.reply_html("Xizmatimiz sizni mamnun qoldirmaganidan afsusdamiz 😔. "
                              "Iltimos,\no'z izohlaringizni yozib qoldiring va biz albatta ularni "
                              "inobatga olib,\nto'g'irlanishga harakat qilamiz 🙏🏻",
        reply_markup=ReplyKeyboardMarkup(
            MAIN_KEYBOARD,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",
        ),
    )
    return ConversationHandler.END


def location(update, context):
    bot = Bot(token='6435050827:AAGIu4VhD3WpWXkHnCXPM9mmdp8vnkkQU0A')
    chat_id = update.message.from_user.id
    latitude = 39.56132070386396
    longitude = 67.25590567787043
    bot.send_location(chat_id=chat_id, latitude=latitude, longitude=longitude)

    update.message.reply_html(
        "🤩 Pastani kafeimizga kelib to'g'ridan-to'g'ri skovorodkadan ta'tib\n"
        " ko'ring - aynan shu uchun ham shaharning"
        "markazida joy ochdik,\n manzil Ц-1'da Ecopark va 64 maktab yonida\n"
        "\n📌 Ish tartibi: du - pa 11:00 - 23:00 / ju 14:00 - 23:00 / sha - yak 11:00 - 23:00"
        "\n\nOperator bilan aloqa 👉 @sakhibdev "
    )


FIKR_BILDIRISH = range(1)


def main() -> None:
    updater = Updater("6435050827:AAGIu4VhD3WpWXkHnCXPM9mmdp8vnkkQU0A")

    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text(ABOUT_ORDER), about_order))
    dispatcher.add_handler(MessageHandler(Filters.text(BASKET), basket))
    dispatcher.add_handler(MessageHandler(Filters.text(MENU), menu_list))

    dispatcher.add_handler(MessageHandler(Filters.text(REQUEST_LOCATION), start))
    dispatcher.add_handler(MessageHandler(Filters.text(CONTACT), contact))

    dispatcher.add_handler(MessageHandler(Filters.text(LOCATION), location))

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", start),
            MessageHandler(Filters.text(ADVICE), fikr_bildirish),
            # MessageHandler(Filters.text(MENU), menu),
        ],
        states={
            FIKR_BILDIRISH: [
                MessageHandler(Filters.text(ZOR_5), marking5),
                MessageHandler(Filters.text(ZOR_4), marking5),
                MessageHandler(Filters.text(ZOR_4), marking5),
                MessageHandler(Filters.regex("^(😐 Yoqmadi ⭐️⭐️⭐️|☹️ Yomon ⭐️⭐️|😤 Juda yomon👎🏻)$"), marking3),
            ],

            # MENUS:
            # [
            #     MessageHandler(Filters.text(REQUEST_LOCATION), start)
            # ]
        },
        fallbacks=[
            CommandHandler("start", start),
            MessageHandler(Filters.text(ADVICE), fikr_bildirish),
        ],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()


