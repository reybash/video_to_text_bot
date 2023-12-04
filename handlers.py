from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, types
from stt import convert_video_to_text
from db import insert
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="My tg", url="https://t.me/VladRubash")]
    ]
)


@dp.message()
async def handle_video(message: types.VideoNote, bot):
    file_id = message.video_note.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    dest = r"G:\test_video_translate_bot\stt\test.mp4"
    await bot.download_file(file_path, destination=dest)

    transcription = f"Transcription for video: {convert_video_to_text(dest)}"

    await insert(
        "INSERT INTO videos (file_id, text_transcription) VALUES (%s, %s)",
        (file_id, transcription),
    )

    await message.reply(transcription, reply_markup=inline_kb)
