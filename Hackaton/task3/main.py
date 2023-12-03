from telethon import TelegramClient
import asyncio

APP_API = ['26699332', '52434635d6fd1c48b1d9d43c67ca93d2']
class TG:
    def __init__(self, api_id=APP_API[0], api_hash=APP_API[1]):
        self.__api_id = api_id
        self.__api_hash = api_hash

    async def parse_dialogs(self, channel):
        r = self.__client.iter_messages(channel)
        # pprint(r)
        return r

    async def main(self, channel):
        r = await self.parse_dialogs(channel)
        dialog = ''
        k = 0
        async for item in r:
            dialog = (f'Время отправки: {item.date.strftime("%m/%d/%Y, %H:%M:%S")}\n'
                      f'ID отправителя: {item.from_id}\n'
                      f'Текст сообщения: {item.message}\n' +
                      (f'Медиа: {item.media}\n\n' if item.media else '\n\n')) + dialog
            k += 1
            if k >= 100: break
        return dialog

    async def run(self, channel):
        try:
            async with TelegramClient('tgparse', int(self.__api_id), self.__api_hash) as self.__client:
                return await self.main(channel)
        except Exception as e:
            return f'Ошибка: {e}'


if __name__ == '__main__':
    tg = TG()

    a = asyncio.run(tg.run('myfavoritejumoreski'))
    print(a)
