# Modified By @DARK-Devil 
from DarkDevil.bot import StreamBot
from DarkDevil.vars import Var
import logging
logger = logging.getLogger(__name__)
from DarkDevil.bot.plugins.stream import MY_PASS
from DarkDevil.utils.human_readable import humanbytes
from DarkDevil.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from DarkDevil.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
from pyrogram.types import ReplyKeyboardMarkup

                      
@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..**\n\n**ᴅᴀʀᴋ ᴅᴇᴠɪʟ ʙᴏᴛᴢ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴍᴇ..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("𝙹𝙾𝙸𝙽 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return
        await m.reply_photo(
            photo="https://telegra.ph/file/8f3a97a75e5510382f0f1.png",
            caption="**ʜᴇʟʟᴏ...⚡\n\nɪ ᴀᴍ ᴀ sɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ  ᴠɪᴅᴇᴏ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴀɴᴅ sᴛʀᴇᴀᴍ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.**\n\n**ᴜsᴇ /help ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛsɪʟs\n\nsᴇɴᴅ ᴍᴇ ᴀɴʏ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛᴏ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀᴢ...**\n\n**ᴄʀᴇᴀᴛᴇᴅ ʙʏ ᴍᴀʟɪɴᴅᴜ ɴɪᴍꜱᴀʀᴀ**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ ᴜᴘᴅᴀᴛᴇꜱ ⚡", url="https://t.me/DarkDevilBotz"), InlineKeyboardButton("⚡ sᴜᴘᴘᴏʀᴛ ⚡", url="https://t.me/DARKDevilV2")],
                    [InlineKeyboardButton("💞 ᴄᴏɴᴛᴀᴄᴛ 💞", url="https://wa.me/+94703892615"), InlineKeyboardButton("💻 ɢɪᴛʜᴜʙ 💻", url="https://github.com/malindunimsara")],
                    [InlineKeyboardButton("💌 ꜰᴏʟʟᴏᴡ ꜰʙ 💌", url="https://www.facebook.com/profile.php?id=100075309916172")],
                    [InlineKeyboardButton("🔎 ꜱᴇᴀʀᴄʜ 🔍", switch_inline_query_current_chat='')]
                ]
            ),
            
        )
    else:
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..**\n\n**ᴅᴀʀᴋ ᴅᴇᴠɪʟ ʙᴏᴛᴢ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴍᴇ..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]                           
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text = "**ᴛᴏᴜʀ ʟɪɴᴋ ɪs ɢᴇɴᴇʀᴀᴛᴇᴅ...⚡\n\n📧 ғɪʟᴇ ɴᴀᴍᴇ :-\n{}\n {}\n\n💌 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :- {}\n\n♻️ ᴛʜɪs ʟɪɴᴋ ɪs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴀɴᴅ ᴡᴏɴ'ᴛ ɢᴇᴛ ᴇxᴘɪʀᴇᴅ ♻️\n\n@DARKDevilV2**"
        await m.reply_photo(
            photo="https://telegra.ph/file/8f3a97a75e5510382f0f1.png",
            caption=msg_text.format(file_name, file_size, stream_link),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ⚡", url=stream_link)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "banned":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ...**\n\n**ᴏɴʟʏ ᴅᴀʀᴋ ᴅᴇᴠɪʟ ʙᴏᴛᴢ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴍᴇ..!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_photo(
            photo="https://telegra.ph/file/8f3a97a75e5510382f0f1.png",
            caption="**┣⪼ sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛʜᴇɴ ɪ ᴡɪʟʟ ʏᴏᴜ ᴘᴇʀᴍᴀɴᴇɴᴛ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ɪᴛ...\n\n┣⪼ ᴛʜɪs ʟɪɴᴋ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴏʀ ᴛᴏ sᴛʀᴇᴀᴍ ᴜsɪɴɢ ᴇxᴛᴇʀɴᴀʟ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀs (ꜱᴜɢ:-ᴍx ᴘʟᴀʏᴇʀ) ᴛʜʀᴏᴜɢʜ ᴍʏ sᴇʀᴠᴇʀs.\n\n┣⪼ ғᴏʀ sᴛʀᴇᴀᴍɪɴɢ ᴊᴜsᴛ ᴄᴏᴘʏ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ᴘᴀsᴛᴇ ɪᴛ ɪɴ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ᴛᴏ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ.\n\n┣⪼ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ ɪɴ ᴄʜᴀɴɴᴇʟ. ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ɢᴇᴛ ʀᴇᴀʟᴛɪᴍᴇ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ғᴏʀ ᴇᴠᴇʀʏ ғɪʟᴇs/ᴠɪᴅᴇᴏs ᴘᴏsʏ../\n\n┣⪼ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ :- /about\n\n\nᴘʟᴇᴀsᴇ sʜᴀʀᴇ**", 
  parse_mode="Markdown",
        
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⚡ ᴜᴘᴅᴀᴛᴇꜱ ⚡", url="https://t.me/DarkDevilBotz"), InlineKeyboardButton("⚡ sᴜᴘᴘᴏʀᴛ ⚡", url="https://t.me/DARKDevilV2")],
                [InlineKeyboardButton("💞 ᴄᴏɴᴛᴀᴄᴛ 💞", url="https://wa.me/+94703892615"), InlineKeyboardButton("💠 ɢɪᴛʜᴜʙ 💠", url="https://github.com/malindunimsara")],
                [InlineKeyboardButton("💌 ꜰᴏʟʟᴏᴡ ꜰʙ 💌", url="https://www.facebook.com/profile.php?id=100075309916172")]
            ]
        )
    )

@StreamBot.on_message(filters.command('about') & filters.private & ~filters.edited)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "banned":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..**\n\n**ᴅᴀʀᴋ ᴅᴇᴠɪʟ ʙᴏᴛᴢ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴘʟᴇᴀꜱᴇ ꜱᴜʙꜱᴄʀɪʙᴇ @DarkDevilBotz**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_photo(
            photo="https://telegra.ph/file/8f3a97a75e5510382f0f1.png",
            caption="""<b>😎sᴏᴍᴇ ʜɪᴅᴅᴇɴ ᴅᴇᴛᴀɪʟs😎</b>

<b>➬〔𝙳𝙰𝚁𝙺 𝙳𝙴𝚅𝙸𝙻 𝙵𝙸𝙻𝙴 𝚃𝙾 𝚄𝚁𝙻 𝙱𝙾𝚃〕⚍</b>
╓
╟⪼<b>ʙᴏᴛ ɴᴀᴍᴇ : <a href='https://t.me/devil_filetourl_bot'>ғɪʟᴇ ᴛᴏ ᴜʀʟ</a></b>
╟⪼<b>ᴜᴘᴅᴀᴛᴇꜱ : <a href='https://t.me/DarkDevilBotz'>ᴅᴅ ᴜᴘᴅᴀᴛᴇꜱ</a></b>
╟⪼<b>sᴜᴘᴘᴏʀᴛ : <a href='https://t.me/DARKDevilV2'>ᴅᴀʀᴋ ᴅᴇᴠɪʟ</a></b>
╟⪼<b>sᴇʀᴠᴇʀ : ʜᴇʀᴏᴋᴜ</b>
╟⪼<b>ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ</b>
╟⪼<b>ʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ 3</b>
╟⪼<b>sᴏᴜʀᴄᴇ-ᴄᴏᴅᴇ : <a href='https://github.com/malindunimsara/File-To-Url'>ғɪʟᴇ ᴛᴏ ᴜʀʟ</a></b>
╟⪼<b>ꜰᴀᴄᴇʙᴏᴏᴋ : <a href='https://www.facebook.com/profile.php?id=100075309916172'>ᴅᴀʀᴋ ᴅᴇᴠɪʟ</a></b>
╙
<b>➵⦁〔✗𝗗𝗔𝗥𝗞 𝗗𝗘𝗩𝗜𝗟✗〕➸⦁</b>""",
  parse_mode="html",
        
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⚡ ᴜᴘᴅᴀᴛᴇꜱ ⚡", url="https://t.me/DarkDevilBotz"), InlineKeyboardButton("💞 ᴄᴏɴᴛᴀᴄᴛ 💞", url="https://wa.me/94703892615")],
                [InlineKeyboardButton("💌 ꜰᴏʟʟᴏᴡ ꜰʙ 💌", url="https://www.facebook.com/profile.php?id=100075309916172")]
            ]
        )
    )
