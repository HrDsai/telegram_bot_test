import asyncio
import telegram


async def main():
    bot = telegram.Bot("6342526970:AAHTtagecOxNTB0zWC-SbS8sQGA2GANOd3g")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())