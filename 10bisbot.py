import telegram 
import asyncio


async def main():
    bot = telegram.Bot("5757017167:AAGvkM6Sow6IKdQsf4ZHWvlATGVCwQiEZrE")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())