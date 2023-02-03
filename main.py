from telegram.ext import (
    Updater, 
    CallbackContext, 
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler
)
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
import os
import db

TOKEN = os.environ['TOKEN']



def start(update: Update, context: CallbackContext):
    keyboart = ReplyKeyboardMarkup([
        ['🛍 Shop','🛒 Cart'],
        ['📞 Contact','📝 About']
    ])
    update.message.reply_html(
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboart
    )

def brands(update: Update, context: CallbackContext):
    all_brands = db.get_tables()
    keyboart = []
    for brand in all_brands:
        keyboart.append([InlineKeyboardButton(text=brand, callback_data=f'brand:{brand}')])
    update.message.reply_text(
    text='all brands',
    reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboart)
    )


def products(update: Update, context: CallbackContext):
    brand = update.callback_query.data.split(':')[1]
    all_products = db.get_products(brand)
    
    for product in all_products:
        update.callback_query.answer(product['name'])


def contact(update: Update, context: CallbackContext):
    update.message.reply_html("connact us")

def about(update: Update, context: CallbackContext):
    update.message.reply_html("adout us")



'''
# def about(update: Update, context: CallbackContext):
#     chat_id = update.message.chat.id

#     keyboar = ReplyKeyboardMarkup([
#         ['📝 About Us','📝 About the bot'],
#         ['Main menu']
#     ])
#     bot = context.bot
#     bot.sendMessage(
#     chat_id=chat_id,
#     text='Assalom alaykum xush kelibsiz botimizga 👍',
#     reply_markup=keyboar
#     )

# def contact(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = InlineKeyboardMarkup([
        [InlineKeyboardButton(text='📞 Phone number',callback_data='number'),InlineKeyboardButton(text='📧 Email',callback_data='email')],
        [InlineKeyboardButton(text='📍 Location',callback_data='location'),InlineKeyboardButton(text='📌 Address',callback_data='address')],
        # [InlineKeyboardButton(text='📞 Phone number',url='txt')]
        
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )
'''

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(handler=CommandHandler(command=['start', 'boshlash'], callback=start))
    dp.add_handler(handler=MessageHandler(filters=filters.Filters.text('🛍 Shop'), callback=brands))
    dp.add_handler(handler=MessageHandler(filters=filters.Filters.text('📞 Contact'), callback=contact))
    dp.add_handler(handler=MessageHandler(filters=filters.Filters.text('📝 About'), callback=about))
    dp.add_handler(handler=CallbackQueryHandler(callback=products, pattern='brand'))
    # dp.add_handler(handler=CallbackQueryHandler(callback=products, pattern='product')

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()