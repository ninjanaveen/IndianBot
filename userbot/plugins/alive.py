"""Check if userbot alive."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
ALIVE_IMG = "https://telegra.ph/file/19161731ca00f82fd6e7d.jpg"
ALIVE_caption = "**Ninja Userbot is Alive!**\n\n\n"
ALIVE_caption += "**🧿 Bot Tier:** `Pro Like Ninja Naveen`\n\n"
ALIVE_caption += "**🧬 Telethon version:** `1.16.2`\n\n"
ALIVE_caption += "**🧿 Python:** `3.7.4`\n\n"
ALIVE_caption += "**🧬 Database Status:** : `All Set and are Working Flawlessly!`\n\n"
ALIVE_caption += "**🧿 Ninja Userbot Version:** `1.2`\n\n\n"
ALIVE_caption += "**💈 Join the Bot Creator's Channel** : [💠Royal Giveaways💠](https://t.me/joinchat/AAAAAEz2wFGuTfGQB1wc2g)\n\n"
ALIVE_caption += "**💈 Join Here too if you won't mind** : [💠Configs By Ninja💠](https://t.me/ConfigsByNinja)\n\n\n"
ALIVE_caption += "[🛡Deploy Ninja Userbot🛡](https://github.com/ninjanaveen/NinjaUserbot)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, ALIVE_IMG,caption=ALIVE_caption)