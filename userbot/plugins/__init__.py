from userbot import *
from userbot.Config import Config
from userbot.helpers.functions import *
from userbot.cmdhelp import CmdHelp
from AuraXBot.utils import *
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User



# =================== CONSTANT ===================

USERID = bot.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "AuraX User"
# mention user
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"
hmention = f"<a href = tg://user?id={USERID}>{DEFAULTUSER}</a>"