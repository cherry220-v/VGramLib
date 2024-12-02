import requests
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('urllib3').setLevel(logging.WARNING)

from errors import AuthError
from watch import *
from base import *

URL = "https://api.telegram.org/bot"

class Bot(User):
    def __init__(self, token: str | None = None):
        super().__init__()
        self.token = token
        self.commands = {}
        self.offset: int = None
        self.id = None
        self.isBot = True
        del self.lastName, self.languageCode, self.isPremium, self.addedToAttachmentMenu

    def run(self, debug=False):
        logging.log(logging.INFO, f" Bot running with token {self.token}")
        if not self.token:
            raise AuthError("'Bot.token' not found")
        self.getMe()
        if debug:
            dir = "."
            start_watchdog(dir, self)
        else:
            while True:
                bot.getUpdates()

    def getMe(self):
        response = requests.post(f"https://api.telegram.org/bot{self.token}/getMe")
        data = response.json()
        if data.get("result") and response.json().get("ok"):
            self = self.obj(Bot, data.get("result"))
        return response.json().get("ok")

    def getUpdates(self):
        data = {}
        if self.offset: data["offset"] = self.offset
        response = requests.post(f"https://api.telegram.org/bot{self.token}/getUpdates", data=data).json()
        if response.get("result"):
            tasks = response["result"]
            for task in tasks:
                update: Update = self.obj(Update, task)
                update.message = self.obj(Message, task.get("message"))
                update.message.chat = self.obj(Chat, task.get("message").get("chat"))
                update.message.sender = self.obj(Chat, task.get("message").get("from"))
                if update.message.entities:
                    for entity in update.message.entities:
                        if entity.get("type") == "bot_command":
                            command = update.message.text.split(' ')[0][1:]
                            if command in self.commands:
                                self.commands[command](self, update.message)
                            else:
                                self.sendMessage(update.message.chat.id, f"Неизвестная команда: {command}")
                self.offset = update.id + 1

    def command(self, name, description):
        def wrapper(func,):
            self.commands[name] = func
            return func
        return wrapper

    def addCommand(self, func, name):
        self.commands[name] = func

    def sendMessage(self, chatId, text):
        message_data = {
            'chat_id': chatId,
            'text': text
        }
        response = requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", data=message_data)
        return response.json().get("ok")
    
    def getChatMember(self, chatId: int, userId: int) -> User:
        response = requests.post(f"https://api.telegram.org/bot{bot.token}/getChatMember", data={"user_id": userId, "chat_id": chatId})
        data = response.json()
        if data.get("result") and response.json().get("ok"):
            user = User()
            user.id = data["id"]
            user.isBot = data["is_bot"]
            user.firstName = data["first_name"]
            user.lastName = data["last_name"]
            user.username = data["username"]
            user.languageCode = data["language_code"]
            user.status = data["status"]
            return user

    def setName(self, name, languageCode):
        "Use this method to change the bot's name. Returns True on success."
        response = requests.post(f"https://api.telegram.org/bot{self.token}/setName").json()
        return response.json().get("ok")

    def setDescription(self, shortDescription, languageCode):
        "Use this method to change the bot's short description, which is shown on the bot's profile page and is sent together with the link when users share the bot. Returns True on success."
        response = requests.post(f"https://api.telegram.org/bot{self.token}/setDescription").json()
        return response.json().get("ok")

bot = Bot()
bot.token = "7871112958:AAHLVE8nxJAUR987VVTnSXbfg5t93EZ9a0c"

@bot.command(name="start", description="Standart description")
def startCommand(bot: Bot, message: Message):
    bot.sendMessage(message.chat.id, message.text)

def anotherStartCommand(bot: Bot, message: Message):
    bot.sendMessage(message.chat.id, str(message.chat.id))

bot.addCommand(anotherStartCommand, "chat")

bot.run(debug=True)