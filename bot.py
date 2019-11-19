import telebot
from jsonData import JSONDocument
import apiai, json
import re

def getSettingFromDb(key):
    return JSONDocument.getDataByKey(key)

def getAnswerFromDialogflow(messageText):
    request = apiai.ApiAI(getSettingFromDb('DialogflowApi')).text_request()
    request.lang = getSettingFromDb("language")
    request.session_id = getSettingFromDb('sessionId')
    request.query = messageText
    responseJson = json.loads(request.getresponse().read().decode("utf-8"))
    response = responseJson["result"]["fulfillment"]["speech"]
    return response

bot = telebot.TeleBot(getSettingFromDb("api_key"))

@bot.message_handler(regexp="\/(bot|бот).*")
def echo_all(message):
    msg = re.sub(r'\/(bot|бот)', "", message.text).strip()
    bot.send_message(message.chat.id, getAnswerFromDialogflow(msg))

if __name__ == '__main__':
  bot.polling()