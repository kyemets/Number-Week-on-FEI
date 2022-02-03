from tg_token import TOKEN
from aiogram import Bot, Dispatcher, executor, types, executor
from aiohttp.client import request
import aiogram.utils.markdown as fmt
import time
import datetime
from datetime import date
from datetime import time
from datetime import datetime
import asyncio


bot = Bot(token=TOKEN,  parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  buttons = ["week number"]
  keyboard.add(*buttons)  
  
  await message.answer("Hello 👋\n\nPress the button to find out the number of the week and the number of days that have passed since the start of the educational process", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "week number")
async def notes(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')

    semester_start = date(2021, 9, 20)
    semester_start_hours = time()

    date_now = date.today()
    date_now_hours = datetime.now() 
    current_time = date_now_hours.strftime('%H:%M:%S')

    current_week = (date_now - semester_start).days
    current_week_now = date(2021, 9, 20).isocalendar().week

    await message.answer(
      f"Days from the date of study: `{current_week}`\n"
      f"Current week: `{current_week_now}`"
    )



if __name__ == '__main__':
    # asyncio.run(main())
    executor.start_polling(dp, skip_updates=True)
    