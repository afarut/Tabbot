from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, Dispatcher, types
import config
import logging


file_log = logging.FileHandler(config.BASE_DIR/'sample.log')
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out), format='[%(asctime)s]|%(levelname)s|%(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())