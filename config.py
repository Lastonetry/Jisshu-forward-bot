from os import environ 

class Config:
    API_ID = environ.get("API_ID", "18996089")
    API_HASH = environ.get("API_HASH", "9320db7656ad27d7839290383be00c91")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7360899365:AAG5PF3VpqCY5cOq6USO79AIUYgJYdD_VBA") 
    BOT_SESSION = environ.get("BOT_SESSION", "botzxD") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://tewem57544:LkAPl5h9kpy4sYUS@cluster0.2g2emyt.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6970918221').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
