#๐๐๐๐๐๐ค๐ฃ ยฎ
#ุงููููู ุญูููู ููุชุงุจูุฉ ุฒููุฒุงู ุงูููุจูู โคถ @zzzzl1l ุฎุงุต ุจุณููุฑุณ โคถ ๐๐๐๐๐๐ค๐ฃ


#ุตุฏููุฉ ุฌูุงุฑููู ููุฑูุญ ุงููุฑุญูููุฉ ุฃููู ูุฑูุญ ุงููุฑุญูููุฉ ุฃู ูููุงุฐ


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import sudo_cmd

from . import reply_id


@bot.on(admin_cmd(pattern="ุตููุงุช ?(.*)"))
@bot.on(sudo_cmd(pattern="ุตููุงุช ?(.*)", allow_sudo=True))
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
            event, "**โฎ .ุจูุงุถุงูุฉ ุงุณูู ุงูุฏูููุฉ ููุงููุฑ ููุจุญุซ ูุซูุงู :  .ุตููุงุช ุงูููู ...๐ซโฐ**"
        )
    chat = "@Zelovbot"
    catevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุฌููุจ ููุงูููุช ุงูุตููุงุฉ ... ๐งธ๐**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=900155491)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @Zelovbot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "ููุงููุช ุงูุตูุงุฉ": "**ุงุณู ุงูุงุถุงููู : **`ููุงููุช ุงูุตูุงุฉ`\
    \n\n**โฎโขโ ุงูุงููุฑ โฆ **`.ุตููุงุช` + ุงุณูู ุงูุฏูููุฉ \
    \n**ุงูุดูุฑุญ โขโข **ุฌููุจ ููุงูููุช ุงูุตููุงุฉ ูู ุงู ุฏูููุฉ"
    }
)
