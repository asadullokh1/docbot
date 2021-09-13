from aiogram import bot, storage


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    from aiogram import executor
    from main import dp

    executor.start_polling(dp, on_shutdown=on_shutdown)
