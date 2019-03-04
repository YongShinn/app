# -*- coding: utf-8 -*-
# 788731481:AAF30CxdR5WM5uZGTCKzAAzpySlTTPZN4CY

import time
import sql_create

import telebot
from telebot import types
import scrape

TOKEN = '788731481:AAF30CxdR5WM5uZGTCKzAAzpySlTTPZN4CY'


Customeritem = ['name', 'brand', 'link1', 'qty1', 'size1', 'color1',
                'link2', 'qty2', 'size2', 'color2', 'link3', 'qty3', 'size3', 'color3']


commands = {  # command description used in the "help" command
    'start': 'Welcome to Buyn',
    'create': 'Create new CART',
    'join': 'Join an existing CART',
    'edit': 'Edit order',
    'faq': 'Frequently Asked Question',
    'help': 'help',
    'recommendbrand': 'Recommend us some brands!',
    'brandlist': 'View current brands on Buyn',
    'return': 'Return',
}


# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) +
                  " [" + str(m.chat.id) + "]: " + m.text)


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  # register listener


# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    sql_create.insert_users(m.chat.first_name)
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('/create')
    itembtn2 = types.KeyboardButton('/join')
    itembtn3 = types.KeyboardButton('/edit')
    itembtn4 = types.KeyboardButton('/help')
    itembtn5 = types.KeyboardButton('/brandlist')
    itembtn6 = types.KeyboardButton('/recommendbrand')
    itembtn7 = types.KeyboardButton('/return')
    itembtn8 = types.KeyboardButton('/faq')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4,
               itembtn5, itembtn6, itembtn7, itembtn8)
    bot.send_message(cid, "Welcome to Buyn", reply_markup=markup)


# chat_action example (not a good one...)
@bot.message_handler(commands=['create'])
def command_create(m):
    cid = m.chat.id
    Customeritem[0] = cid
    print(Customeritem[0])
    bot.send_chat_action(cid, 'typing')  # show the bot "typing" (max. 5 secs)
    time.sleep(2)
    markup2 = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Colorpop: [$50]💄')
    itembtn2 = types.KeyboardButton('Sephora: [$40]💄')
    itembtn3 = types.KeyboardButton('Sephora: [$110]💄')
    itembtn4 = types.KeyboardButton('Uniqlo: [$60]👚')
    itembtn5 = types.KeyboardButton('Zara: [$79]👚')
    itembtn6 = types.KeyboardButton("The Editor's Market: [$60]👚")
    itembtn7 = types.KeyboardButton("The Editor's Market: [$60]👚")
    itembtn8 = types.KeyboardButton('The Tinsel Rack: [$100]👚')
    itembtn9 = types.KeyboardButton('Abercrombie & Fitch: [$160]👚')
    itembtn10 = types.KeyboardButton('Gardenpicks: [$50]🥜')
    itembtn11 = types.KeyboardButton('MyProtein: [$100]💊')
    markup2.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5,
                itembtn6, itembtn7, itembtn8, itembtn9, itembtn10, itembtn11)
    msg = bot.reply_to(m, """Hello there! 😊 Seems like you’re creating a new cart to share.

This is a list of all minimum basket size to qualify for free shipping by retailers. Take a look!:

Colorpop: $50 💄 https://colourpop.com/

Sephora: $40 [FREE SHIPPING] $110 [FREE NEXT DAY] 💄 https://www.sephora.sg/

Uniqlo: $60 👚 https://www.uniqlo.com/sg/store/#undefined

Zara: $79 👚 https://www.zara.com/sg/ 

The Editor’s Market: Free Shipping, discount starts at 3 pieces and more, discounts up to 6 pieces. We are offering two options for you at $60 and $120 👚 https://www.theeditorsmarket.com/

The Tinsel Rack: $100 👚 https://www.thetinselrack.com/

Abercrombie & Fitch: $160 👚 https://www.abercrombie.sg/en_SG/home

Gardenpicks: $50 🥜 http://gardenpicks.com.sg/

MyProtein: $100 💊 http://gardenpicks.com.sg/

Can you please give us the name of the brand that you will be shopping from? 📥""", reply_markup=markup2)
    bot.register_next_step_handler(msg, create_chooseBrand)


def create_chooseBrand(message):
    try:
        chat_id = message.chat.id
        Customeritem[1] = message.text
        print(Customeritem[1])
        markup3 = types.ReplyKeyboardMarkup(row_width=1)
        itembtn1 = types.KeyboardButton('Done')
        itembtn2 = types.KeyboardButton('Cancel')
        markup3.add(itembtn1, itembtn2)
        msg = bot.reply_to(
            message, """Send Link1""", reply_markup=markup3)
        bot.register_next_step_handler(msg, create_screenshot)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def create_screenshot(message):
    try:
        chat_id = message.chat.id
        if message.text == 'Done':
            markup4 = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton('UTown')
            itembtn2 = types.KeyboardButton('Sheares')
            itembtn3 = types.KeyboardButton('Kent Ridge')
            markup4.add(itembtn1, itembtn2, itembtn3)
            msg = bot.reply_to(message, """Aweasome, can we know where you want your items delivered to? 
Utown: Delivery will be done to cheers 
Sheares: SH Lobby
KR: KR Lobby""", reply_markup=markup4)
            bot.register_next_step_handler(msg, create_location)

        else:
            link1 = message.text
            Customeritem[2] = link1
            print(Customeritem[2])
            # print(scrape.scraping(Customeritem[1], Customeritem[2], 'NA'))
            markup5 = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton('1')
            itembtn2 = types.KeyboardButton('2')
            itembtn3 = types.KeyboardButton('3')
            markup5.add(itembtn1, itembtn2, itembtn3)
            msg = bot.reply_to(message, """Qty?""", reply_markup=markup5)
            bot.register_next_step_handler(msg, create_screenshot_qty)
    except Exception as e:
        bot.reply_to(message, 'oooops')
#           #
# QUANTITY  #
#           #


def create_screenshot_qty(message):
    try:
        chat_id = message.chat.id
        if message.text == 'Done':
            markup4 = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton('UTown')
            itembtn2 = types.KeyboardButton('Sheares')
            itembtn3 = types.KeyboardButton('Kent Ridge')
            markup4.add(itembtn1, itembtn2, itembtn3)
            msg = bot.reply_to(message, """Aweasome, can we know where you want your items delivered to? 
Utown: Delivery will be done to cheers 
Sheares: SH Lobby
KR: KR Lobby""", reply_markup=markup4)
            bot.register_next_step_handler(msg, create_location)

        else:
            qty1 = message.text
            Customeritem[3] = qty1
            print(Customeritem[3])
            # print(scrape.scraping(Customeritem[1], Customeritem[2], 'NA'))
            msg = bot.reply_to(message, """Size?""")
            bot.register_next_step_handler(msg, create_screenshot_Size)
    except Exception as e:
        bot.reply_to(message, 'oooops')

#           #
#   SIZE    #
#           #


def create_screenshot_Size(message):
    try:
        chat_id = message.chat.id
        if message.text == 'Done':
            markup4 = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton('UTown')
            itembtn2 = types.KeyboardButton('Sheares')
            itembtn3 = types.KeyboardButton('Kent Ridge')
            markup4.add(itembtn1, itembtn2, itembtn3)
            msg = bot.reply_to(message, """Aweasome, can we know where you want your items delivered to? 
Utown: Delivery will be done to cheers 
Sheares: SH Lobby
KR: KR Lobby""", reply_markup=markup4)
            bot.register_next_step_handler(msg, create_location)

        else:
            size1 = message.text
            Customeritem[4] = size1
            print(Customeritem[4])
            # print(scrape.scraping(Customeritem[1], Customeritem[2], 'NA'))
            msg = bot.reply_to(message, """Color?""")
            bot.register_next_step_handler(msg, create_screenshot_Color)
    except Exception as e:
        bot.reply_to(message, 'oooops')

#           #
#   COLOR   #
#           #


def create_screenshot_Color(message):
    try:
        chat_id = message.chat.id
        if message.text == 'Done':
            markup4 = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton('UTown')
            itembtn2 = types.KeyboardButton('Sheares')
            itembtn3 = types.KeyboardButton('Kent Ridge')
            markup4.add(itembtn1, itembtn2, itembtn3)
            msg = bot.reply_to(message, """Aweasome, can we know where you want your items delivered to? 
Utown: Delivery will be done to cheers 
Sheares: SH Lobby
KR: KR Lobby""", reply_markup=markup4)
            bot.register_next_step_handler(msg, create_location)

        else:
            color1 = message.text
            Customeritem[5] = color1
            print(Customeritem[5])
            print("""Title: """ + scrape.scraping(Customeritem[1], Customeritem[2], "NA")[0] + '\nPrice: ' + scrape.scraping(
                Customeritem[1], Customeritem[2], "NA")[1] + '\nQty: ' + Customeritem[3] + '\nSize: ' + Customeritem[4] + '\nColor: ' + Customeritem[5])
            msg = bot.reply_to(message, """Title: """ + scrape.scraping(Customeritem[1], Customeritem[2], "NA")[0] + '\nPrice: ' + scrape.scraping(
                Customeritem[1], Customeritem[2], "NA")[1] + '\nQty: ' + Customeritem[3] + '\nSize: ' + Customeritem[4] + '\nColor: ' + Customeritem[5])
            bot.register_next_step_handler(msg, create_screenshot_Color)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def create_screenshot2(message):
    try:
        chat_id = message.chat.id
        if message.text == 'Done':

            markup3 = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton('UTown')
            itembtn2 = types.KeyboardButton('Sheares')
            itembtn3 = types.KeyboardButton('Kent Ridge')
            markup3.add(itembtn1, itembtn2, itembtn3)
            msg = bot.reply_to(message, """Aweasome, can we know where you want your items delivered to? 
Utown: Delivery will be done to cheers 
Sheares: SH Lobby
KR: KR Lobby""", reply_markup=markup3)
            bot.register_next_step_handler(msg, create_location)

        else:
            screenshot2 = message.photo[0].file_id
            print(screenshot2)
            customer_item = Customeritem(screenshot2)
            user_dict[chat_id] = Customeritem
            msg = bot.reply_to(message, """2""")
            bot.register_next_step_handler(msg, create_screenshot3)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def create_screenshot3(message):
    try:
        chat_id = message.chat.id
        if message.text == 'Done':

            markup3 = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton('UTown')
            itembtn2 = types.KeyboardButton('Sheares')
            itembtn3 = types.KeyboardButton('Kent Ridge')
            markup3.add(itembtn1, itembtn2, itembtn3)
            msg = bot.reply_to(message, """Aweasome, can we know where you want your items delivered to? 
Utown: Delivery will be done to cheers 
Sheares: SH Lobby
KR: KR Lobby""", reply_markup=markup3)
            bot.register_next_step_handler(msg, create_location)

        else:
            screenshot3 = message.photo[0].file_id
            print(screenshot3)
            customer_item = Customeritem(screenshot3)
            user_dict[chat_id] = Customeritem
            markup3 = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton('UTown')
            itembtn2 = types.KeyboardButton('Sheares')
            itembtn3 = types.KeyboardButton('Kent Ridge')
            markup3.add(itembtn1, itembtn2, itembtn3)
            msg = bot.reply_to(message, """Aweasome, can we know where you want your items delivered to? 
Utown: Delivery will be done to cheers 
Sheares: SH Lobby
KR: KR Lobby""", reply_markup=markup3)
            bot.register_next_step_handler(msg, create_location)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def create_location(message):
    try:
        chat_id = message.chat.id
        location = message.text
        customer_item = Customeritem(location)
        user_dict[chat_id] = Customeritem
        print(location)
    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.message_handler(commands=['join'])
def command_join(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')  # show the bot "typing" (max. 5 secs)
    time.sleep(2)
    msg = bot.reply_to(
        m, """Hello there good looking 🤩, seems likes you’re joining a cart. Can we have the Unique Cart Number (UCN) please?""")
    bot.register_next_step_handler(msg, join_CartID)


def join_CartID(message):
    try:
        chat_id = message.chat.id
        CartID = message.text
        join_item = joinItem(CartID)
        join_dict[chat_id] = joinItem
        print(CartID)
        msg = bot.reply_to(message, """Nice, please send over a screenshot of your desired product! (Up to 3 pieces) 🛍🛍🛍

Remember to press 'Done' once you're ready!
""")
        bot.register_next_step_handler(msg, join_screenshot)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def join_screenshot(message):
    try:
        chat_id = message.chat.id
        if message.text == 'Done':
            msg = bot.reply_to(message, """Well received! Thank you for your purchase, a Buyn admin will be in contact to confirm your purchase very soon! In the meantime, check out our instagram page at instagram.com/buynofficial 

Cheers and good day to you! ☺️	
""")
        else:
            screenshot = message.photo[0].file_id
            print(screenshot)
            join_item = joinItem(screenshot)
            join_dict[chat_id] = joinItem
            markup3 = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton('Done')
            itembtn2 = types.KeyboardButton('Cancel')
            markup3.add(itembtn1, itembtn2)
            msg = bot.reply_to(message, """1""", reply_markup=markup3)
            bot.register_next_step_handler(msg, join_screenshot2)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def join_screenshot2(message):
    try:
        chat_id = message.chat.id
        if message.text == 'Done':
            msg = bot.reply_to(message, """Well received! Thank you for your purchase, a Buyn admin will be in contact to confirm your purchase very soon! In the meantime, check out our instagram page at instagram.com/buynofficial 

Cheers and good day to you! ☺️	
""")
        else:
            screenshot2 = message.photo[0].file_id
            print(screenshot2)
            join_item = joinItem(screenshot2)
            join_dict[chat_id] = joinItem
            msg = bot.reply_to(message, """2""")
            bot.register_next_step_handler(msg, join_screenshot3)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def join_screenshot3(message):
    try:
        if message.text == 'Done':
            msg = bot.reply_to(message, """Well received! Thank you for your purchase, a Buyn admin will be in contact to confirm your purchase very soon! In the meantime, check out our instagram page at instagram.com/buynofficial 

Cheers and good day to you! ☺️	
""")
        else:
            chat_id = message.chat.id
            screenshot3 = message.photo[0].file_id
            print(screenshot3)
            join_item = joinItem(screenshot3)
            join_dict[chat_id] = joinItem
            bot.send_message(chat_id, """Well received! Thank you for your purchase, a Buyn admin will be in contact to confirm your purchase very soon! In the meantime, check out our instagram page at instagram.com/buynofficial 

Cheers and good day to you! ☺️""")
    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.message_handler(commands=['edit'])
def command_edit(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')  # show the bot "typing" (max. 5 secs)
    time.sleep(2)
    msg = bot.reply_to(
        m, """Hey there, change of mind? No problem! Can we have your Personal Transaction Number (PTN) for your purchase please?""")
    bot.register_next_step_handler(msg, edit_message)


def edit_message(m):
    cid = m.chat.id
    cartID = m.text
    print(cartID)
    bot.send_message(
        cid, """Well received, let us connect you to a Buyn admin ASAP!""")


@bot.message_handler(commands=['faq'])
def command_faq(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')  # show the bot "typing" (max. 5 secs)
    time.sleep(2)
    bot.send_message(cid,
                     """Hello! Here is an exhaustive list of FAQ that our users have for us. Take a quick look!

Who are we?
Buyn is a social shopping platform working out of I3. We hope to connect shoppers together with a user-centric focused framework. Buyn is currently working with the support of NUS Enterprise. Check out our insta page for more details at @officialbuyn and leave us comments on how to be better. :-)

When do I make payments?
You will only be required to make payments when your Cart is filled and ready to go. Get your friends to help you with filling the Cart!

Which payment options are available?
We currently only accepts PayNow. So sorry for the inconvenience! 

How do I return my products?
For product returns, Buyn will follow the existing individual company policies that you are shopping out from. Please contact a Buyn admin via /return if you would like to return a product. :-)

I want to shop at a brand which is not here. What can I do?
Please tell us how to best expand our brand list here /recommendbrands. We look forward to hearing from you amigo! 

How long do I have to wait?
Each Cart lasts for 24hours, we will inform you once the Cart reaches 80% of its stipulated goal. Sit back and relax while your Cart fills :-)

What if my Cart doesnt fill?
You can have the option to extend your Cart’s waiting time or cancel your order. Although we do prefer the former!""")


@bot.message_handler(commands=['brandlist'])
def command_brandlist(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')  # show the bot "typing" (max. 5 secs)
    time.sleep(2)
    bot.send_message(cid,
                     """Current brands on Buyn and their minimum basket size to qualify for free shipping!
1.	Colorpop: $50 💄
2.	Sephora: $40 [FREE SHIPPING] $110 [FREE NEXT DAY] 💄
3.	Uniqlo: $60 👚
4.	Zara: $79 👚
5.	The Editor’s Market: 3 pieces and more, discounts up to 6 pieces. 👚
6.	The Tinsel Rack: $100 👚
7.	Abercrombie & Fitch: $160 👚
8.	Love, Bonito: Nil 👚
9.	Gardenpicks: $50 🥜
10.	MyProtein: $100 💊""")

# help page


@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')  # show the bot "typing" (max. 5 secs)
    time.sleep(2)
    bot.send_message(cid,
                     """Hey there! This is a list of commands you can use readily :-)

/create: Create a new Cart to share with your friends.

/join: Join an existing Cart :-)

/edit: To edit your order!

/brandlist: A list of existing brands that is working on Buyn right now!

/recommendbrand: Tell us who should be here! 

We hope this helps. If you have any further queries feel free to visit our /faq section!
""")


# filter on a specific message


@bot.message_handler(func=lambda message: message.text == "hi")
def command_text_hi(m):
    bot.send_message(m.chat.id, "I love you too!")


# default handler for every other text
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    # this is the standard reply to a normal message
    bot.send_message(m.chat.id, "I don't understand \"" +
                     m.text + "\"\nMaybe try the help page at /help")


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()


bot.polling()
