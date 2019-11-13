import asyncio
import os
from asyncio import sleep
from typing import Callable
from src.service.model._RFIDReader import RFIDReader


class RFIDReaderImpl(RFIDReader):

    def __init__(self, reader_ip: str, reader_port: int, jumps_to_send_data: int, loop):
        self.reader_ip = reader_ip
        self.reader_port = reader_port
        self.jumps_to_send_data = jumps_to_send_data
        self.loop = loop

    async def read_forever(self, callback: Callable[[str], None]):
        while True:
            try:
                reader, writer = await asyncio.open_connection(self.reader_ip, self.reader_port, loop=self.loop)

                while True:
                    data = await reader.read(100)
                    if len(data) == 0:
                        await sleep(1)
                        break;
                    callback(data.decode())
            except Exception as ex:
                print(ex)
                await sleep(5)

