#๐๐๐๐๐๐ค๐ฃ ยฎ
#ุงููููู ุญูููู ููุชุงุจูุฉ ุฒููุฒุงู ุงูููุจูู โคถ @zzzzl1l ุฎุงุต ุจุณููุฑุณ โคถ ๐๐๐๐๐๐ค๐ฃ
#ุงูููู ูู ุจุงูุซูู ููููุง ุฎูุทุช ุฑุงุญ ุชุทูุน ุญููููููููู ุจุณูููุฑุณูููู

#ูููููููููููููููููู


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import sudo_cmd

from . import reply_id


@bot.on(admin_cmd(pattern="ููุฏ ?(.*)"))
@bot.on(sudo_cmd(pattern="ููุฏ ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**โฎ . ุงูุซูุฑ ููู 1000 ุงูุชูุงุฑุงุช ุงูููู ุดุจูุงุจ ููุทูุฑูููู.. ุงุฑุณูู .ููุฏ ุงููู ๐ซโฐ**"
        )
    chat = "@ZelTrbot"
    catevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุงูุชูุงุฑ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1354728480)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @ZelTrbot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)



import os
from faker import Faker
import datetime
from telethon import functions, types, events
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest

from ..utils import admin_cmd, sudo_cmd


@bot.on(admin_cmd("ููุฒุง$"))
@bot.on(sudo_cmd("ููุฒุง$", allow_sudo=True))
async def _(ZEDDevent):
    if ZEDDevent.fwd_from:
        return
    ZEDDcc = Faker()
    ZEDDname = ZEDDcc.name()
    ZEDDadre = ZEDDcc.address()
    ZEDDcard = ZEDDcc.credit_card_full()
    
    await edit_or_reply(ZEDDevent, f"๐ฐ ๐๐๐๐๐พ๐ ๐๐๐ฟ - ๐๐๐๐ผ_๐พ๐ผ๐๐ฟ  ๐ณ๐ช\n\n\n__**๐ค ุงูุงุณูู :- **__\n ูดโโโโโโโโโโโโโโ\n`{ZEDDname}`\n\n__**๐ก ุงูุนูููุงู :- **__\n ูดโโโโโโโโโโโโโโ\n`{ZEDDadre}`\n\n__**๐ธ ุงููููุฒุง :- **__\n ูดโโโโโโโโโโโโโโ\n`{ZEDDcard}`\n\nโ๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ โง @ZedThonโ ")
    


CMD_HELP.update(
    {
        "ุงููู ุดุจุงุจ": "**ุงุณู ุงูุงุถุงููู : **`ุงููู ุดุจุงุจ`\
    \n\n**โฎโขโ ุงูุงููุฑ โฆ **`.ููุฏ ุงููู`  \
    \n**ุงูุดูุฑุญ โขโข **ุงูุซูุฑ ููู 1000 ุงูุชูุงุฑุงุช ุงูููู ุดุจูุงุจ ููุทูุฑูููู .. ุงุฑุณูู .ููุฏ ุงููู"
    }
)
