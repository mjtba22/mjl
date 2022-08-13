## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuxSmZaN7s8cRLAm-7xJSJLWrULEOKAXlNQwlc25N03ipRTQyGdVEfu6l2FZa1qFqV_xUbC9ghcWgPK21Q1L7WQvHqlpUssNubY_Z0cyCngZadDo8IghK4URVlx60jv7IRF4nrfaqzdi5RcXl1N2PkVu3XlxQA9FF_cv5ndifb7lA7bnTsxbJPwMx_F0OnylyDJ-0VpC9NSpNz279U323g6Nn2Bh6d4Rqf7ehe9rK1Jom6NHj7Fx6D3BzdDz202MfUpnpIylzLWMiViYqymoYGFqsjf6-GB7Ao_ynVBinCkUkUAV2D3I0YIwfkuyoNuPKOhuSHOJYOUialOMvaSyHgp4=l")
BOT_TOKEN = getenv("BOT_TOKEN", "5526455890:AAFwa6cqE_TGHdvsBFEXvM-8k1JGwEoiy1s")
BOT_NAME = getenv("BOT_NAME", "ميوزك القـــᬼـ⍣⃟ـᬼــائد 👑⃝⃡ᬼ꙰")
API_ID = int(getenv("API_ID", "13568396"))
API_HASH = getenv("API_HASH", "736866f3245fcd8d0e6a81038790670c")
OWNER_NAME = getenv("OWNER_NAME", "O_Q_C")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ZzZzZ5")
ALIVE_NAME = getenv("ALIVE_NAME", "القـــᬼـ⍣⃟ـᬼـائد اَࠗاَْࠗب߬ـنۨۨۨۨۨۨۨ شۨـغٌؒـاَْࠗتٍيަِ👑⃝⃡ᬼ꙰")
BOT_USERNAME = getenv("BOT_USERNAME", "V_X_Vbot")
OWNER_ID = getenv("OWNER_ID", "5284259786")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "V6_BV")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "e_e_g_e")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Q_0_U")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5270972093").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
