#๐๐๐๐๐๐ค๐ฃ ยฎ
#ุงููููู ุญูููู ุฒููุฒุงู ุงูููุจูู โคถ @zzzzl1l ุฎุงุต ุจุณููุฑุณ โคถ ๐๐๐๐๐๐ค๐ฃ
#ุงูููู ูุชุนูุจ ุนููู So ุชุฎูุท ููุงุชุฐููุฑ ุงููุตูุฏุฑ == ุงููููู

#ูู

from userbot.helpers import *
import base64
import io
import os
from pathlib import Path
from . import *
from telethon import types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url
from youtubesearchpython import Video
import json
import os
import time
import requests
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

try:

    from youtubesearchpython import *

except:
    os.system("pip install pip install youtube-search-python")
    from youtubesearchpython import SearchVideos

from userbot import bot
from ..helpers.utils import reply_id
from userbot.helpers.functions import deEmojify


#>>>>>>>>>>>>>>>>>>โโุญููู ุฒููุฒุงู ุงูููุจููู - @zzzzl1lโโ<<<<<<<<<<<<<<<<<<<

@bot.on(admin_cmd(pattern="ุจุญุซ ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="ุจุญุซ ?(.*)", allow_sudo=True))
async def FindMusicPleaseBot(zed):

    song = zed.pattern_match.group(1)

    chat = "@FindMusicPleaseBot"

    if not song:

        return await zed.edit("**โโูู ุจุงุถุงููุฉ ุงูุงุบูููู ููุงููุฑ .. ุจุญุซ + ุงุณูู ุงูุงุบูููู**")

    await zed.edit("**โฎ ุฌูุงุฑู ุงูุจุญุซ ุูู ุงูุงุบููููู... ๐งโฅ๏ธโฐ**")

    await asyncio.sleep(2)

    async with bot.conversation(chat) as conv:

        await zed.edit("**โฎ โ ุฌูุงุฑู ุชุญูููู ุงูุงุบููููู ุงูุชุธูุฑ ููููุงู  โฌโญ... ๐ซโฐ**")

        try:

            await conv.send_message(song)

            response = await conv.get_response()

            if response.text.startswith("ุนูุฐุฑุงู"):

                await bot.send_read_acknowledge(conv.chat_id)

                return await zed.edit(f"**โโุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ** {song}")

            await conv.get_response()

            lavde = await conv.get_response()

        except YouBlockedUserError:

            await zed.edit(
                "**โโุชุญููู ูู ุงููู ูู ุชููู ุจุญุธูุฑ ุงูุจูุช @FindMusicPleaseBot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )

            return

        await zed.edit("**โฎ โ ุฌูุงุฑู ุงุฑุณูุงู ุงูุงุบููููู ุงูุชุธูุฑ ููููุงู  โฌโญ... ๐ซโฐ**")

        await bot.send_file(zed.chat_id, lavde)

        await bot.send_read_acknowledge(conv.chat_id)

    await zed.delete()
