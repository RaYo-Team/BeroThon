#๐๐๐๐๐๐ค๐ฃ ยฎ
#ุงููููู ุญูููู ุฒููุฒุงู ุงูููุจูู โคถ @zzzzl1l ุฎุงุต ุจุณููุฑุณ โคถ ๐๐๐๐๐๐ค๐ฃ
#ุงูููู ูุชุนูุจ ุนููู So ุชุฎูุท ููุงุชุฐููุฑ ุงููุตูุฏุฑ == ุงููููู

#ูู

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


@bot.on(admin_cmd(pattern="ุชููุชูู$", outgoing=True))
@bot.on(sudo_cmd(pattern="ุชููุชูู$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**```ุจุงููุฑุฏ ุนูู ุงูุฑุงุจูุท ุญูุจูู ๐งธ๐```**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**```ุจุงููุฑุฏ ุนูู ุงูุฑุงุจูุท ุญูุจูู ๐งธ๐```**")
        return
    chat = "@downloader_tiktok_bot"
    catevent = await edit_or_reply(event, "**โฎ โ ุฌูุงุฑู ุงูุชุญูููู ูู ุชููู ุชููู ุงูุชุธูุฑ ููููุงู  โฌโญ... ๐ซโฐ**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1332941342)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**โโุชุญููู ูู ุงููู ูู ุชููู ุจุญุธูุฑ ุงูุจูุช @downloader_tiktok_bot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**๐คจ๐...ุ**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "ุชูู ุชูู": "**ุงุณู ุงูุงุถุงููู : **`ุชูู ุชูู`\
    \n\n**โฎโขโ ุงูุงููุฑ โฆ **`.ุชููุชูู` ุจุงูุฑุฏ ุนูู ุงูุฑุงุจุท\
    \n**ุงูุดูุฑุญ โขโข **ุชุญููู ููุงุทูุน ุงูููุฏููู ูู ุชููู ุชููู"
    }
)
