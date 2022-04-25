import telebot
import sqlite3
from telebot import types
from config import Token

bot=telebot.TeleBot(Token)

con = sqlite3.connect('example.db')
cur = con.cursor()

@bot.message_handler(commands="start")
def func(message):
    markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True )
    russkiy = types.KeyboardButton("Русский язык")
    angl = types.KeyboardButton("English")
    uzb = types.KeyboardButton("Ozbek tili")
    markup.add(russkiy , angl , uzb)
    bot.send_message(message.chat.id , "Hello! , this bot belong to Qushbegi Plaza Hotel and created to help to Dear Guests \n\n\nЗдравствуйте! , этот бот принадлежит Отелю Qushbegi Plaza и был создан для помощи Много-уважаемым Гостям \n \n \n Assalomu Aleykum! , Bu bot Qushbegi Plaza Mehmonhonaga tegishli bolib Qadirli mehmonlsrimizga yordam berish uchun Yaratilgan" , reply_markup=markup)
    con.execute(message.from_user.id)
'''
@bot.message_handler(commands="secret_code_01234567")
def rassilka_func(message):
    bot.send_message( message.chat.id , "Здравствуйте вы ввели секретный код для массовой рассылки пользователям")
    bot.register_next_step_handler(message , rassilka)
    '''
#________________________________________________ANGLIYSKIY____________________________________________________
@bot.message_handler(content_types=("text"))
def Major_function(message):
    if message.text == 'English':
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True )
        rooms = types.KeyboardButton("Rooms") # +
        rest = types.KeyboardButton("Restaurant")
        conference = types.KeyboardButton("Conference halls")
        complain = types.KeyboardButton("Complains book")# +
        info = types.KeyboardButton("Extra information")
        lang = types.KeyboardButton("Change language")
        markup.add(complain , rest , rooms , conference , info , lang )
        bot.send_message(message.chat.id , "Hello , How can i help you" , reply_markup=markup)
    #RESTARAUNT_________________________________________________________________________________________________________________________________

    elif message.text == 'Menu':
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True )
        rooms = types.KeyboardButton("Rooms") # +
        rest = types.KeyboardButton("Restaurant")
        conference = types.KeyboardButton("Conference halls")
        complain = types.KeyboardButton("Complains book")# +
        info = types.KeyboardButton("Information")
        lang = types.KeyboardButton("Change language")
        markup.add(complain , rest , rooms , conference , info , lang )
        bot.send_message(message.chat.id , "You came back to the Menu" , reply_markup=markup)

    elif message.text == "Change language":
        func(message)


    elif message.text == "Restaurant":
        bot.send_media_group(message.chat.id , restoraunt_media_angl)
            
    #CONFERENCE HALLS________________________________________________________________________________________________________________

    elif message.text == "Conference halls":
        bot.send_media_group(message.chat.id , big_conference_angl )
        bot.send_media_group(message.chat.id , little_conference_angl )

    #INFORMATION_______________________________________________________________________________________________________________________________

    elif message.text == "Extra information":
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
        website = types.KeyboardButton("Website")
        phone = types.KeyboardButton("Phone numbers")
        geo = types.KeyboardButton("Geolocation")
        back = types.KeyboardButton("Menu")
        markup.add(phone , website , geo , back)
        bot.send_message(message.chat.id , "Choose button to get information which you want" , reply_markup=markup)

    elif message.text == "Website":
        bot.send_message(message.chat.id , "https://www.qushbegiplaza.uz")


    elif message.text == "Phone numbers":
        bot.send_message(message.chat.id , " Our phone numbers are +998(78)113-00-77\n+998(78)113-00-70 ")


    elif message.text == "Geolocation":
        bot.send_location(message.chat.id ,41.272453, 69.24515)
    # Rooms _______________________________________________________________________________________________________________________

    elif message.text == "Rooms":
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
        standart=types.KeyboardButton("Standart Room")
        deluxe = types.KeyboardButton("Delux Room")
        lux = types.KeyboardButton("Lux Room")
        menu = types.KeyboardButton("Menu")
        markup.add(standart , deluxe , lux , menu)
        bot.send_message(message.chat.id , "Our Rooms" , reply_markup=markup)

    elif message.text == "Standart Room":
            bot.send_media_group(message.chat.id , standart_medias_angl )
            

    elif message.text == "Delux Room":
        bot.send_media_group(message.chat.id ,delux_medias_angl)

    elif message.text == "Lux Room":
        bot.send_media_group(message.chat.id , lux_medias_angl)


    #COMPLAINS_________________________________________________________________________________________________

    elif message.text == "Complains book":
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
        complain = types.KeyboardButton("Complain")
        offer = types.KeyboardButton("Offer")
        menu = types.KeyboardButton("Menu")
        markup.add(complain , offer , menu)
        bot.send_message(message.chat.id , "Choose one of them to report offer or complain" , reply_markup=markup)


    elif message.text == "Complain":
        bot.send_message(message.chat.id , "Please write down your complain")
        bot.register_next_step_handler(message , all_func)

    elif message.text == "Offer" :
        bot.send_message(message.chat.id , "Please write down your offer")
        bot.register_next_step_handler(message , all_func)


#________________________________Russian_____________________________________________________


    elif message.text == 'Русский язык':
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True )
        rooms = types.KeyboardButton("Комнаты") # +
        rest = types.KeyboardButton("Ресторан")
        conference = types.KeyboardButton("Конференц залы")
        complain = types.KeyboardButton("Книга жалоб")# +
        info = types.KeyboardButton("Доп. инфо")
        lang = types.KeyboardButton("Смена языка")
        markup.add(complain , rest , rooms , conference , info , lang)
        bot.send_message(message.chat.id , "Здравствуйте чем могу вам помочь?" , reply_markup=markup)
    #RESTARAUNT_________________________________________________________________________________________________________________________________

    elif message.text == 'Меню':
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True )
        rooms = types.KeyboardButton("Комнаты") # +
        rest = types.KeyboardButton("Ресторан")
        conference = types.KeyboardButton("Конференц залы")
        complain = types.KeyboardButton("Книга жалоб")# +
        info = types.KeyboardButton("Доп. инфо")
        lang = types.KeyboardButton("Смена языка")
        markup.add(complain , rest , rooms , conference , info , lang )
        bot.send_message(message.chat.id , "Вы вернулись в Меню" , reply_markup=markup)


    elif message.text == "Смена языка":
        func(message)


    elif message.text == "Ресторан":
        bot.send_media_group(message.chat.id , restoraunt_media_rus)
            
    #CONFERENCE HALLS________________________________________________________________________________________________________________

    elif message.text == "Конференц залы":
        bot.send_media_group(message.chat.id , big_conference_rus )
        bot.send_media_group(message.chat.id , little_conference_rus )

    #INFORMATION_______________________________________________________________________________________________________________________________

    elif message.text == "Доп. инфо":
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
        website = types.KeyboardButton("Вебсайт")
        phone = types.KeyboardButton("Номера телефонов")
        geo = types.KeyboardButton("Геолокация")
        back = types.KeyboardButton("Меню")
        markup.add(phone , website , geo , back)
        bot.send_message(message.chat.id , "Выберите один вариант из выше перечисленных" , reply_markup=markup)

    elif message.text == "Вебсайт":
        bot.send_message(message.chat.id , "https://www.qushbegiplaza.uz")


    elif message.text == "Номера телефонов":
        bot.send_message(message.chat.id , " Наш номер телефона +998(78)113-00-77\n+998(78)113-00-70 ")


    elif message.text == "Геолокация":
        bot.send_location(message.chat.id ,41.272453, 69.24515)
    # Rooms _______________________________________________________________________________________________________________________

    elif message.text == "Комнаты":
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
        standart=types.KeyboardButton("Стандартная комната")
        deluxe = types.KeyboardButton("Делюкс комната")
        lux = types.KeyboardButton("Люкс комната")
        menu = types.KeyboardButton("Меню")
        markup.add(standart , deluxe , lux , menu)
        bot.send_message(message.chat.id , "Наши Комнаты" , reply_markup=markup)

    elif message.text == "Стандартная комната":
            bot.send_media_group(message.chat.id , standart_medias_rus )
            

    elif message.text == "Делюкс комната":
        bot.send_media_group(message.chat.id ,delux_medias_rus)

    elif message.text == "Люкс комната":
        bot.send_media_group(message.chat.id , lux_medias_rus)


    #COMPLAINS_________________________________________________________________________________________________

    elif message.text == "Книга жалоб":
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
        complain = types.KeyboardButton("Жалоба")
        offer = types.KeyboardButton("Предложение")
        menu = types.KeyboardButton("Меню")
        markup.add(complain , offer , menu)
        bot.send_message(message.chat.id , "Выберите один вариант из вышеперечисленных" , reply_markup=markup)


    elif message.text == "Жалоба":
        bot.send_message(message.chat.id , "Пожалуйста впишите свою жалобу")
        bot.register_next_step_handler(message , all_func)

    elif message.text == "Предложение" :
        bot.send_message(message.chat.id , "Пожалуйста впишите свое предложение")
        bot.register_next_step_handler(message , all_func)

#___________________________UZBEK TILI_________________________________________________________________________

    elif message.text == 'Ozbek tili':
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True )
        rooms = types.KeyboardButton("Honalar") # +
        rest = types.KeyboardButton("Restoran")
        conference = types.KeyboardButton("Konferentsiya xonalari")
        complain = types.KeyboardButton("Taklif va shikoyatlar kitobi")# +
        info = types.KeyboardButton("Qoshimcha malumot")
        lang = types.KeyboardButton("Tilni ozgartirish")
        markup.add(complain , rest , rooms , conference , info , lang)
        bot.send_message(message.chat.id , "Assalomu Aleykum , sizga qanday yordam bera olaman?" , reply_markup=markup)
    #RESTARAUNT_________________________________________________________________________________________________________________________________

    elif message.text == 'Mеnu':
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True )
        rooms = types.KeyboardButton("Honalar") # +
        rest = types.KeyboardButton("Restoran")
        conference = types.KeyboardButton("Konferentsiya xonalari")
        complain = types.KeyboardButton("Taklif va shikoyatlar kitobi")# +
        info = types.KeyboardButton("Qoshimcha malumot")
        lang = types.KeyboardButton("Tilni ozgartirish")
        markup.add(complain , rest , rooms , conference , info , lang )
        bot.send_message(message.chat.id , "Siz menuga qaytidngiz" , reply_markup=markup)

    elif message.text == "Tilni ozgartirish":
        func(message)


    elif message.text == "Restoran":
        bot.send_media_group(message.chat.id , restoraunt_media_uzb)
            
    #CONFERENCE HALLS________________________________________________________________________________________________________________

    elif message.text == "Konferentsiya xonalari":
        bot.send_media_group(message.chat.id , big_conference_uzb )
        bot.send_media_group(message.chat.id , little_conference_uzb )

    #INFORMATION_______________________________________________________________________________________________________________________________

    elif message.text == "Qoshimcha malumot":
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
        website = types.KeyboardButton("Websayt")
        phone = types.KeyboardButton("Telefon Raqamlar")
        geo = types.KeyboardButton("Geolokatsiya")
        back = types.KeyboardButton("Mеnu")
        markup.add(phone , website , geo , back)
        bot.send_message(message.chat.id , "Yuqoridagilardan birini tanlang" , reply_markup=markup)

    elif message.text == "Websayt":
        bot.send_message(message.chat.id , "https://www.qushbegiplaza.uz")


    elif message.text == "Telefon Raqamlar":
        bot.send_message(message.chat.id , "Bizning telefon raqamlarimiz +998(78)113-00-77\n+998(78)113-00-70 ")


    elif message.text == "Geolokatsiya":
        bot.send_location(message.chat.id ,41.272453, 69.24515)
    # Rooms _______________________________________________________________________________________________________________________

    elif message.text == "Honalar":
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
        standart=types.KeyboardButton("Standart hona")
        deluxe = types.KeyboardButton("Delux hona")
        lux = types.KeyboardButton("Lux hona")
        menu = types.KeyboardButton("Mеnu")
        markup.add(standart , deluxe , lux , menu)
        bot.send_message(message.chat.id , "Bizning honalar" , reply_markup=markup)

    elif message.text == "Standart hona":
            bot.send_media_group(message.chat.id , standart_medias_uzb )
            

    elif message.text == "Delux hona":
        bot.send_media_group(message.chat.id ,delux_medias_uzb)

    elif message.text == "Lux hona":
        bot.send_media_group(message.chat.id , lux_medias_uzb)


    #COMPLAINS_________________________________________________________________________________________________

    elif message.text == "Taklif va shikoyatlar kitobi":
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
        complain = types.KeyboardButton("Shikoyat")
        offer = types.KeyboardButton("Taklif")
        menu = types.KeyboardButton("Mеnu")
        markup.add(complain , offer , menu)
        bot.send_message(message.chat.id , "Yuqoridagilardan birini tanlang" , reply_markup=markup)

        


    elif message.text == "Shikoyat":
        bot.send_message(message.chat.id , "Iltimos shikoyatingizni kiriting")
        bot.register_next_step_handler(message , all_func )

    elif message.text == "Taklif" :
        bot.send_message(message.chat.id , "Iltimos taklifingizni kiriting")
        bot.register_next_step_handler(message , all_func)
        markup = types.ReplyKeyboardRemove()
    else:
        bot.send_message(message.chat.id , "Sorry i do not understand you \n\nИзвините я вас не понял \n\nUzur sizni Tushunmadim")


'''
def rassilka(message):
    if message.text == "нет" :
        bot.send_message(message.chat.id , "Рассылка была прервана")

    else :      
        bot.send_photo, "https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi.jpg" , caption=message.text)
        bot.send_message(message.chat.id )
        bot.send_message(message.chat.id , "рассылка была успешно отправлена")
            

@bot.message_handler(content_types="photo")
def kartinka(message):
    kartinka = message
    '''

def all_func(message):
    username = message.from_user.username
    bot.send_message(-1001776542436," Поступило сообщение от пользователя : " + message.from_user.first_name + "\n\nСообщение : \n " +  message.text)
    bot.send_message(message.chat.id ,  "your application has been successfully received \n \n \n Ваша заявка была успешно принята \n \n \n Sizning arizangiz muvafaqqiyatli qabul qilindi" )


standart_medias_angl= [ types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/06/abu.photographer-44-min-scaled-1000x1000.jpg" , caption="standart room bla bla bla") , types.InputMediaPhoto( "https://qushbegiplaza.uz/wp-content/uploads/2020/06/abu.photographer-10-min-scaled-1000x1000.jpg") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/11/qushbegi-plaza-15-1000x1000.jpg")]
delux_medias_angl = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/abu.photographer-11-min-1000x1000.jpg" , caption="delux room bla bla bla") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/abu.photographer-16-min-scaled-1000x1000.jpg") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/delyuks7-1000x1000.jpg")]
lux_medias_angl = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/11/img_4132-1000x1000.jpg" , caption="lux room bla bl bla") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/abu.photographer-18-min-1-scaled-1000x1000.jpg") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/11/qushbegi-plaza-16-1000x1000.jpg")]


big_conference_angl = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi5-1024x683.jpg" , caption="big conference hall include 50 persons") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi4-1024x683.jpg")]
little_conference_angl = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi2-1024x683.jpg" , caption="little conference hall include 20 persons") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi3-1024x683.jpg") ]


restoraunt_media_angl = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi6-1024x683.jpg" , caption="Our restoraunt can include 90 persons and we can provide all kinds of measures ") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi8-1024x683.jpg") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2021/06/img_1284-hdr-2-min-2-1024x683.jpg")]

#______________________________________________________________RUSSIAN______________________________________________________

standart_medias_rus = [ types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/06/abu.photographer-44-min-scaled-1000x1000.jpg" , caption="Комната Стандарт и так далее  ") , types.InputMediaPhoto( "https://qushbegiplaza.uz/wp-content/uploads/2020/06/abu.photographer-10-min-scaled-1000x1000.jpg") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/11/qushbegi-plaza-15-1000x1000.jpg")]
delux_medias_rus = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/abu.photographer-11-min-1000x1000.jpg" , caption="Комната Делюкс и так далее  ") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/abu.photographer-16-min-scaled-1000x1000.jpg") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/delyuks7-1000x1000.jpg")]
lux_medias_rus = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/11/img_4132-1000x1000.jpg" , caption="Люкс комната и так далее   ") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/abu.photographer-18-min-1-scaled-1000x1000.jpg") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/11/qushbegi-plaza-16-1000x1000.jpg")]


big_conference_rus = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi5-1024x683.jpg" , caption="Большой конференц залл вмещает порядка 80 человек") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi4-1024x683.jpg")]
little_conference_rus = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi2-1024x683.jpg" , caption="Маленький конференц залл вмещает порядка 20 человек ") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi3-1024x683.jpg") ]


restoraunt_media_rus = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi6-1024x683.jpg" , caption="Наш ресторан вмещает порядка 90 человек а так же мы проводим все виды мероприятий под заказ") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi8-1024x683.jpg") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2021/06/img_1284-hdr-2-min-2-1024x683.jpg")]
    #_______________________________________________________________________________________________



standart_medias_uzb = [ types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/06/abu.photographer-44-min-scaled-1000x1000.jpg" , caption=" Standart honamiz bla bla bla  ") , types.InputMediaPhoto( "https://qushbegiplaza.uz/wp-content/uploads/2020/06/abu.photographer-10-min-scaled-1000x1000.jpg") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/11/qushbegi-plaza-15-1000x1000.jpg")]
delux_medias_uzb = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/abu.photographer-11-min-1000x1000.jpg" , caption=" Delux honamiz bla bla bla  ") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/abu.photographer-16-min-scaled-1000x1000.jpg") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/delyuks7-1000x1000.jpg")]
lux_medias_uzb = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/11/img_4132-1000x1000.jpg" , caption=" Lux Honamiz bla bla bla   ") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/abu.photographer-18-min-1-scaled-1000x1000.jpg") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/11/qushbegi-plaza-16-1000x1000.jpg")]


big_conference_uzb = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi5-1024x683.jpg" , caption="Kotta konferens zalimiz 80 ta odam sigdiradi") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi4-1024x683.jpg")]
little_conference_uzb = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi2-1024x683.jpg" , caption="Kichkina konferens zalimiz 20 ta odam sigdiradi ") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi3-1024x683.jpg") ]


restoraunt_media_uzb = [types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi6-1024x683.jpg" , caption="Bizning resroranimiz turli hildagi tadbirlani otkazib bera oladi") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2020/02/uslugi8-1024x683.jpg") , types.InputMediaPhoto("https://qushbegiplaza.uz/wp-content/uploads/2021/06/img_1284-hdr-2-min-2-1024x683.jpg")]



bot.polling(none_stop=True)


'''
@bot.message_handler(content_types=("new_complaint")
def complaint(message):
    markup=types.InlineKeyboardMarkup(row_width=2)
    cp=types.InlineKeyboardButton("Complaint", callback_data="cp")
    ofr=types.InlineKeyboardButton("Offer", callback_data="ofr")
    markup.add(cp , ofr)
    bot.send_message(message.chat.id , " . " , reply_markup=markup)
    
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cp":
        bot.send_message(call.id, "please write your complaint")
    elif call.data == "ofr":
        bot.send_message(call.id, "please write your offer")
c
bot.polling(none_stop=True)
'''