class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 27776767
    API_HASH = "e7b0d8f7b037df9ff8b300816e90080b"

    CASH_API_KEY = "Y15QXI0LCZ4BZSYW"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://ztmhsmna:WgUKtX-9aYWK7mGVHUW7Ea0_66quCFrs@peanut.db.elephantsql.com/ztmhsmna"  # A sql database url from elephantsql.com

    EVENT_LOGS = -1001936153022  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://frolomose77:tt6kEAR5F8nQbJlp@elainacluster.riwve8c.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/a933fd2ec85183af0cf07.jpg"

    SUPPORT_CHAT = "hiraukichat"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6051821883:AAGfnVLAI9pdyoHJ--uTBS2Ammw_5BaGLhM"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6343385909  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
