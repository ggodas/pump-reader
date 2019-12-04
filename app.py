import asyncio
import logging
import os
import time

from resources import helper
from src.devicereader import RFIDReaderImpl
from src.service.interactor import RefuellingProcessInteractor

logger = logging.getLogger("FleetControl")
rfid_detector_interactor = RefuellingProcessInteractor()

count = 0

async def rfid_worker(loop):
    rfid_reader = RFIDReaderImpl("localhost", 8888, 1, loop)
    await rfid_reader.read_forever(rfid_detector_interactor.on_rfid_detect)


async def encoder_worker(loop):
    while True:
        await asyncio.sleep(0.01)
        global count
        count += 1
        print("Second Worker Executed {}".format(count))


async def pump_handle(loop):
    while True:
        await asyncio.sleep(0.01)
        global count
        count += 1
        print("Thirdy Worker Executed {}".format(count))

def main():
    log_path = config_path = os.environ["CONFIG_PATH"]
    if "LOG_PATH" in os.environ:
        log_path = os.environ["LOG_PATH"]

    helper.config_logger(log_path, "fleet-control-service")

    conf = helper.read_json_from_file_as_dictionary(config_path)

    rfid_host = None
    rfid_port = None

    if "http" in conf:
        host = conf["rfid"]["host"]
        port = conf["rfid"]["port"]

    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(rfid_worker(loop))
        asyncio.ensure_future(encoder_worker(loop))
        asyncio.ensure_future(pump_handle(loop))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()

if __name__ == "__main__":
    main()




