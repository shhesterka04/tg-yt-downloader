from utils import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("audio", "Скачать аудио"),
            types.BotCommand("video", "Скачать видео"),
            #types.BotCommand("playlist", "Скачать плейлист")
        ]
    )