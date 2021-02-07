"""Check if fridaybot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
import time
from telethon import __version__ as tv
import sys
import platform
from git import Repo
from uniborg.util import friday_on_cmd, sudo_cmd
from fridaybot import ALIVE_NAME, CMD_HELP, Lastupdate, friday_version
from fridaybot.Configs import Config
from fridaybot.modules import currentversion


# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = Config.ALIVE_IMAGE


@friday.on(friday_on_cmd(pattern=r"alive"))
@friday.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def friday(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    uptime = get_readable_time((time.time() - Lastupdate))
    repo = Repo()
    branch_name = repo.active_branch.name
    pm_caption = ("➥ **FRIDAY IS:** `ONLINE`\n\n"
                  "➥ **SYSTEMS STATS**\n"
                  f"➥ **Telethon Version:** `{tv}` \n"
                  f"➥ **Python:** `{platform.python_version()}` \n"
                  f"➥ **Uptime** : `{uptime}` \n"
                  "➥ **Database Status:**  `Functional`\n"
                  f"➥ **Current Branch** : `{branch_name}`\n"
                  f"➥ **Version** : `{friday_version}`\n"
                  f"➥ **My Boss** : {DEFAULTUSER} \n"
                  "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
                  "➥ **License** : [GNU General Public License v3.0](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n"
                  "➥ **Check Stats By Doing** `.stat`. \n\n"
    
    await borg.send_message(
        alive.chat_id,
        pm_caption,
        reply_to=alive.message.reply_to_msg_id,
        file=PM_IMG,
        force_document=False,
        silent=True,
    )
    await alive.delete()


CMD_HELP.update(
    {
        "alive": "**ALive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Check if UserBot is Alive"
    }
)
