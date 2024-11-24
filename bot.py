import requests
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('urllib3').setLevel(logging.WARNING)

from errors import AuthError
from watch import *

URL = "https://api.telegram.org/bot"

class BaseUser:
    def __init__(self):
        self.id: int = None
        self.isBot: bool = None
        self.firstName: str = None
        self.lastName: str = None
        self.username: str = None
        self.languageCode: str = None
        self.isPremium: bool = None
        self.addedToAttachmentMenu: bool = None
        self.canJoinGroups: bool = None
        self.canReadAllGroupMessages: bool = None
        self.supportsInline_queries: bool = None
        self.canConnectToBusiness: bool = None
        self.hasMainWebApp: bool = None
    
    def fromData(self, data: dict):
        self.id = data.get("id")
        self.isBot = data.get("is_bot")
        self.firstName = data.get("first_name")
        self.username = data.get("username")
        self.canJoinGroups = data.get("can_join_groups")
        self.canReadAllGroupMessages = data.get("can_read_all_group_messages")
        self.supportsInline_queries = data.get("supports_inline_queries")
        self.canConnectToBusiness = data.get("can_connect_to_business")
        self.hasMainWebApp = data.get("has_main_web_app")
        return self

class BaseChat:
    def __init__(self):
        self.id: int = None
        self.firstName: str = None
        self.lastName: str = None
        self.username: str = None
        self.type: str = None

class BaseMessage:
    def __init__(self):
        self.id: int = None
        self.sender: BaseUser = None
        self.chat: BaseChat = None
        self.date: int = None
        self.text: str = None
        self.entities: list = None

    def fromData(self, data: dict):
        self.id = data.get("message_id")
        
        self.sender = User()
        self.sender.fromData(data.get("from", {}))
        
        chat = Chat()
        chat.id = data.get("chat", {}).get("id")
        chat.firstName = data.get("chat", {}).get("firstName")
        chat.lastName = data.get("chat", {}).get("lastName")
        chat.username = data.get("chat", {}).get("username")
        chat.type = data.get("chat", {}).get("type")
        
        self.text = data.get("text")
        self.chat = chat
        return self

class Message(BaseMessage):
    def __init__(self):
        super().__init__()
    def answer(self): pass
class Update:
    def __init__(self):
        self.id: int = None
        self.message: BaseMessage = None

class User(BaseUser):
    def __init__(self):
        super().__init__()
        self.status: str = None

class Chat(BaseChat):
    def __init__(self):
        super().__init__()

class Bot(BaseUser):
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
            self.fromData(data.get("result"))
        return response.json().get("ok")

    def getUpdates(self):
        data = {}
        if self.offset: data["offset"] = self.offset
        response = requests.post(f"https://api.telegram.org/bot{self.token}/getUpdates", data=data).json()
        if response.get("result"):
            tasks = response["result"]
            for task in tasks:
                update = Update()
                update.id = task.get("update_id")
                message = Message()
                message.fromData(task.get("message"))
                update.message = message

                if message.text.startswith('/'):
                    command = message.text.split(' ')[0][1:]
                    if command in self.commands:
                        self.commands[command](self, message)
                    else:
                        self.sendMessage(message.chat.id, f"Неизвестная команда: {command}")
                    self.offset = update.id + 1

    def command(self, name):
        def wrapper(func):
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

@bot.command(name="start")
def startCommand(bot, message: Message):
    print(message.text)

bot.run(debug=True)