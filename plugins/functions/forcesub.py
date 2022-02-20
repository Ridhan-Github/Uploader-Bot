import asyncio
from plugins.config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def handle_force_subscribe(bot, message):
    try:
        invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return 400
    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), message.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=message.from_user.id,
                text="Sorry Sir, You are Banned. Contact My [Support Group](https://t.me/tellybots_4u).",
                parse_mode="markdown",
                disable_web_page_preview=True,
                reply_to_message_id=message.message_id,
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="👋 Hᴇʟʟᴏ, {} \n\nJᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ 🔐!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(" Jᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 ᴛʀʏ ᴀɢᴀɪɴ", callback_data=f"checksub#{file_id}")
                    ]
                ]
            ),
            parse_mode="markdown",
            reply_to_message_id=message.message_id,
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Something Went Wrong. Contact My [Support Group](https://t.me/Tellybots_4u).",
            parse_mode="markdown",
            disable_web_page_preview=True,
            reply_to_message_id=message.message_id,
        )
        return 400


