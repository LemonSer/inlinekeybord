from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard_inline.keyboard import start_game, scene_1, scene_2

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description= 'Команда запуска бота'),
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Добро пожаловать на ДНД', reply_markup=start_game())

@dp.callback_query_handler(lambda c: c.data == 'start_story')
async def start_story(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'В далёком королевстве, где магия и приключения были неотъемлемой частью жизни, группа отважных героев решила отправиться в опасное путешествие вглубь тёмного подземелья. Их цель была проста — раскрыть тайну древнего артефакта, который, по слухам, обладал невероятной силой и мог изменить ход истории.', reply_markup=scene_1())


@dp.callback_query_handler(lambda c: c.data == 'continue_scene_1')
async def continue_scene_1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Но никто из них не предполагал, какие испытания и опасности ждут их на пути к цели. Подземелье было полно ловушек, монстров и загадок, которые требовали смекалки, ловкости и командной работы.', reply_markup=scene_2())

@dp.callback_query_handler(lambda c: c.data == 'continue_scene_2')
async def continue_scene_2(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Вступая в этот опасный мир, герои понимали, что им придётся преодолеть свои страхи, научиться доверять друг другу и стать настоящей командой, способной справиться с любыми трудностями.', reply_markup=start_game())


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)