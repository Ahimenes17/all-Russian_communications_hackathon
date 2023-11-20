import settings
from telethon import TelegramClient


class TG:
    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash
        self.client = TelegramClient('tgparse', api_id, api_hash)

    async def parse_dialogs(self, channel, text=False):
        channel_id = channel
        ret = []
        if text:
            async for i in self.client.iter_messages(channel_id):
                if text in i.message:
                    # print(i)
                    ret.append(i)
            return ret
        # pprint(client.iter_messages(channel_id))
        return self.client.iter_messages(channel_id)

    async def main(self, channel):
        r = await self.parse_dialogs(channel)
        dialog = ''
        async for item in r:
            dialog += (f'ID отправителя: {item.from_id}\n'
                       f'Текст сообщения: {item.message}\n'
                       f'Медиа: {item.media}\n')
        print(dialog)

    async def run(self, channel):
        with self.client:
            try:
                self.client.loop.run_until_complete(self.main(channel))
            except Exception as e:
                print(e)
