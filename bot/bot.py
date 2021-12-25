from aiogram import Bot, Dispatcher, executor, types

TOKEN = '1915299580:AAFzbpNwFpvV5IoyVLtVEOY1Byf0CREZHM8'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
	await bot.send_message(message.from_user.id, "Бот запущен")

@dp.message_handler()
async def command_message(message: types.Message):
	await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True)
