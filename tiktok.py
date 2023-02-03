import os
import telebot
from TikTokApi import TikTokApi
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

API_KEY= os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY,threaded=True,num_threads=10)
telebot.apihelper.SESSION_TIME_TO_LIVE = 5 * 60

@bot.message_handler(commands=['mysnap','start'],)
def send_mysnap(message):
	bot.send_message(message.chat.id, "تابعنا على حسابنا في سناب شات: rashed \n"
            "https://www.snapchat.com/add/rashed") 


    

@bot.message_handler(commands=['tiktok'])
def send_mysnap(message):
	bot.send_message(message.chat.id, "ضع رابط فيديو التيك توك") 
    
           
@bot.message_handler()
def snap(message):
    request = message.text.split()
    
    if len(request) > 1 :
        bot.send_message(message.chat.id, "الرجاء التأكد من صحة الربط")
        return 

    bot.send_message(message.chat.id, "جاري التحميل يرجى إنتظار")    
    count=1
    while True:
        try:
            with TikTokApi(custom_verify_fp="verify_ldoj2rk1_tODwkp7b_5p3v_4fNk_Aj5M_kK8IpTznSzUH",use_test_endpoints=True) as api:  
                video=  api.video(url=message.text)
                logger.info("[+] {} has video with id {}, try number : {}".format(video.info()["author"]["nickname"],video.info()["id"],count))
                link = video.info()["video"]["playAddr"]
                if ".com/video" in link:
                    count+=1
                    continue
                bot.send_video(message.chat.id,link)
                bot.send_message(message.chat.id, "تم تحميل")   
                logger.info("[✔] {} video downloaded".format(video.info()["author"]["nickname"]))
        except:
            continue
        break         
   
        

    
    

# bot.polling(non_stop=True)
bot.infinity_polling(allowed_updates=telebot.util.update_types)



