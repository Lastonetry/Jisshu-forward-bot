from os import environ 

class Config:
    API_ID = environ.get("API_ID", "12417581")
    API_HASH = environ.get("API_HASH", "568d97425b4b1e898faa378e8490b10b")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7362521924:AAF4_VVkJst1XANr4YqqFhvtqJdGbeKQ9ew") 
    BOT_SESSION = environ.get("BOT_SESSION", "fwdxbot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://tewem57544:LkAPl5h9kpy4sYUS@cluster0.2g2emyt.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "fwd-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7462351545').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
