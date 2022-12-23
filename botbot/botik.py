import config
import telebot 
from random import choice, randint

bot = telebot.TeleBot(config.token)


def random_choise(some_list,i = 0):
    if i == 0:
        return choice(some_list)
    else: return some_list[i]

list_send_message = ["",'ну просто вафля, ясно','ну такое, видали и по лучше','ну чё осел',"валенок","ууу сука грешно смеяться над вами","ebat' ti anglichanin","охуетельный боксер","ой да не важно","следущий ..","красава почти конечно" ]
list_answ = ['https://miro.medium.com/max/1200/1*mGkhbvno0bALf5XXaW2dRA.jpeg', '2', '3']
list_dp = ['https://onstartup.ru/wp-content/uploads/2018/10/python3-nose-timer.png','https://sun9-12.userapi.com/impg/ut5J629K1EtcliBmwt-rmZPjwgEHBHTA0pEtqw/HHruiGkHK1o.jpg?size=604x491&quality=96&sign=70bb465a043f21c13d80c5803772c639&type=album','https://i.ytimg.com/vi/Vnm3J7JhFKk/maxresdefault.jpg']
audio_set = ['Lana_Del_Rey_-_Diet_Mtn_Dew_.mp3','Stromae_-_Bienvenue_chez_moi.mp3','ZHU_-_Faded_Original_Mix.mp3']

@bot.message_handler(commands=['start'])
def button(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3 = telebot.types.KeyboardButton("Pic")
    item4 = telebot.types.KeyboardButton("audio")
    markup.add(item3,item4)
    
    bot.send_message(message.chat.id,f'Привет  {message.from_user.username}  скинь фотку',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    if message.text == 'Pic':
            bot.send_photo(message.chat.id,choice(list_dp))
    elif message.text == 'audio':
            bot.send_audio(message.chat.id,audio=open(f'D:\\музыка\\{random_choise(audio_set)}','rb'))



@bot.message_handler(content_types=['photo'])
def callphoto(message):
        bot.reply_to(message, random_choise(list_send_message,randint(1,10)))


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'next':
            bot.send_message(call.message.chat.id, random_choise(list_answ))

# @bot.message_handler(func=lambda message:True)
# def all_messages(message):
#     if message.text:
        
#         bot.send_message(message.from_user.id,"Done with Keyboard",reply_markup=telebot.types.ReplyKeyboardRemove())

bot.infinity_polling()