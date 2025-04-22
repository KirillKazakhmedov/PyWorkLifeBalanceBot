import random
from telegram.ext import Updater, CallbackContext
import logging, schedule, time

CHAT_ID='-4698180911'
#CHAT_ID='-1001546423285'
TOKEN='5715366690:AAG-ehvnmIintQwM5INB6oEZSFMu_cVswYs'
updater = Updater(token=TOKEN, use_context=True)
is_first_monday = False
is_first_friday = True
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

work_life_balance_msgs = ["Коллеги, обновляем статусы задач в jira и соблюдаем work-life баланс", 
                          "Рабочий день подошел к концу, поэтому двигаем таски в jira и соблюдаем work-life баланс",
                          "Псс, тут это, пора обновлять статусы задачек в jira и блюсти work-life баланс",
                          "Сворачивай свою бурную деятельность, стахановец, обновляй таски в jira и бегом на сеновал",
                          "Не все могут работать. Вернее работать могут не только лишь все, мало кто может не обновить таски в jira и соблюсти work-life баланс",
                          "Покажи мне свои таски в jira, а я покажу тебе как соблюдать work-life баланс",
                          "Котики, обновляйте статусы задач в jira и следуйте заветам великого Конфуция по соблюдению work-life баланса"]

dev_demo_msgs = ["Пора готовить презентацию к демо",
                 "Демо не проворонь да презенташку заготовь",
                 "А ты подготовил(a) презентацию к Dev.Demo?",
                 "Много встреч? Задач? Поди и презентациaя к демо не готова..."]

friday_msgs = ["Всем хороших выходных!",
               "Всем безудержного чилла на выходных!",
               "Работу завершил(а), в выходные согрешил(а)"]

retro_msg = "Котики, скоро ретро, а значит, я скоро выдам в этот чатик все плюсы и минусы, что вы подготовили"

retro_notification_msgs = ["Ретро не проворонь да тезисы подготовь",
                           "Плюсы и минусы к предстоящему ретро в студию!",
                           "Я часть той силы, что желает зла, но вечно собирает ваши текста к ретро"]

morning_meeting_msgs = ["А вас, Штирлиц, я попрошу на дейлик!",
			"На дейлик, товарищи, на дейлик!",
			"Тайм ту дейлик!",
			"Погнали дейлиться!"]

def morning_meeting_callback(context: CallbackContext):
    message = random.choice(morning_meeting_msgs)
    context.bot.send_message(chat_id=CHAT_ID, text=message)

def work_life_balance_callback(context: CallbackContext):
    message = random.choice(work_life_balance_msgs)
    context.bot.send_message(chat_id=CHAT_ID, text=message)

def friday_schedule_callback(context: CallbackContext):
    message = random.choice(friday_msgs)
    context.bot.send_message(chat_id=CHAT_ID, text=message)

def demo_retro_schedule_callback(context: CallbackContext):
    global is_first_friday
    if is_first_friday == False:
        message = random.choice(dev_demo_msgs)
        context.bot.send_message(chat_id=CHAT_ID, text=message)
        message = random.choice(retro_notification_msgs)
        context.bot.send_message(chat_id=CHAT_ID, text=message)
        is_first_friday = True
    else:
        is_first_friday = False

def retro_monday_schedule_callback(context: CallbackContext):
    global is_first_monday
    if is_first_monday == True:
        context.bot.send_message(chat_id=CHAT_ID, text=retro_msg)
        is_first_monday = False
    else:
        is_first_monday = True


def morning_meeting_schedule_creator():
    pass
    #schedule.every().monday.at("11:00").do(morning_meeting_callback, updater)
    #schedule.every().tuesday.at("11:00").do(morning_meeting_callback, updater)
    #schedule.every().wednesday.at("11:00").do(morning_meeting_callback, updater)
    #schedule.every().thursday.at("11:00").do(morning_meeting_callback, updater)
    #schedule.every().friday.at("11:00").do(morning_meeting_callback, updater)

def work_life_balance_schedule_creator():
    schedule.every().monday.at("19:30").do(work_life_balance_callback, updater)
    schedule.every().tuesday.at("15:55").do(work_life_balance_callback, updater)
    schedule.every().wednesday.at("19:30").do(work_life_balance_callback, updater)
    schedule.every().thursday.at("19:30").do(work_life_balance_callback, updater)
    schedule.every().friday.at("19:00").do(work_life_balance_callback, updater)
    schedule.every().friday.at("19:01").do(friday_schedule_callback, updater)

def demo_retro_schedule_creator():
    schedule.every().friday.at("12:00").do(demo_retro_schedule_callback, updater)

def retro_monday_schedule_creator():
    schedule.every().monday.at("15:00").do(retro_monday_schedule_callback, updater)

def hello_to_chat(context: CallbackContext):
    message = "Привет, комрады! Я ваш командный помощник по координации наиболее важных мероприятий и соблюдению work-life баланса. Здесь я буду оставлять свой след в виде напоминалок"
    context.bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == '__main__':
    work_life_balance_schedule_creator()
    #demo_retro_schedule_creator()
    #retro_monday_schedule_creator()
    morning_meeting_schedule_creator()
    #hello_to_chat(updater)
    while True:
        schedule.run_pending()
        time.sleep(30)
