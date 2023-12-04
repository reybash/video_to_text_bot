import logging
from db import loop
from handlers import dp, bot


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    loop.run_until_complete(main())
