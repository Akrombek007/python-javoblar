from telegram import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup
from telegram.ext import Updater,CommandHandler,CallbackQueryHandler,ConversationHandler,MessageHandler,Filters

BUGUN,ERTA,OY,REGION,DUO=('🔊 Bugun','📢 Ertaga','📆 To\'liq taqvim','🇸🇱 Mintaqa','👐 Duo')

#pastdan chiquvchi buttonlar uchun
main_button = ReplyKeyboardMarkup(
    [
        [BUGUN],[ERTA,OY],[REGION],[DUO]
    ],resize_keyboard= True
)

Token = '1815942501:AAHH59S_UvWgyQVrS2hxiVdK_Wg4SYqvO0A'

#inline buttonlar
buttons = [
    [
        InlineKeyboardButton('Toshkent',callback_data='Toshkent'),
        InlineKeyboardButton('Andijon', callback_data='Andijon'),
    ]
]
STATE_REGION = 1
STATE_CALENDAR = 2
#Kiruvchi malumotlarni ushlab qolish funksiyasi
def inline_callback(update,context):
    query = update.callback_query#qanaqa malumot kirotganini aniqlovchi
    query.message.delete()
    query.message.reply_html(text='<b>Ramozon taqvimi</b> 2️⃣0️⃣2️⃣1️⃣ \n \n Quyidagilardan birini tanlang 👇',reply_markup = main_button)
    #query.edit_message_text(text='<b>Ramozon taqvimi</b> 2️⃣0️⃣2️⃣1️⃣ \n \n Quyidagilardan birini tanlang 👇',parse_mode='HTML',
    #                        reply_markup = main_button)

    print(query.data)
    return STATE_CALENDAR

def start(update,context):
    user = update.message.from_user
    update.message.reply_html('Assalomu alaykum <b>{}!</b>\n \n<b>Ramazon oyi muborak bo\'lsin</b>\n \nSizga qaysi joylashuv bo\'yicha malumot berayin?'
                              .format(user.first_name),reply_markup=InlineKeyboardMarkup(buttons))
    return STATE_REGION
def help(update,context):
    user = update.message.from_user
    update.message.reply_html('Assalomu alaykum <b>{}!</b>\n \n<b>Ramazon oyi muborak bo\'lsin</b>\n \nSizga qaysi joylashuv bo\'yicha malumot berayin?'
                              .format(user.first_name),reply_markup=InlineKeyboardMarkup(buttons))
def calendar_today(update,message):

    update.message.reply_text('Bugun belgilandi')

def calendar_erta(update,message):
    update.message.reply_text('Erta belgilandi')

def calendar_month(update,message):
    update.message.reply_text('Oy belgilandi')

def select_region(update,message):
    update.message.reply_text('Mintaqa belgilandi')

def select_duo(update,message):
    update.message.reply_text('Duoni ko\'rish belgilandi')

def main():
    updater = Updater(Token,use_context=True)
    #Dispatcher eventlarni aniqlab olish
    dispatcher = updater.dispatcher
    # start kommandasini ushlab olish
    dispatcher.add_handler(CommandHandler('start',start))
    dispatcher.add_handler(CommandHandler('help',help))
    # inline zaproslarni ushlab olish uchun
    dispatcher.add_handler(CallbackQueryHandler(inline_callback))


    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start',start)],
#        entry_points=[CommandHandler('help', help)],
        states = {
            STATE_REGION:[CallbackQueryHandler(inline_callback)],
            STATE_CALENDAR:[
                MessageHandler(Filters.regex('^('+BUGUN+')$'),calendar_today),
                MessageHandler(Filters.regex('^(' + ERTA + ')$'),calendar_erta),
                MessageHandler(Filters.regex('^(' + OY + ')$'), calendar_month),
                MessageHandler(Filters.regex('^(' + REGION + ')$'), select_region),
                MessageHandler(Filters.regex('^(' + DUO + ')$'), select_duo)
            ],
        },
        fallbacks=[CommandHandler('start',start)]
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

main()
