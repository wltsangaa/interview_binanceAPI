from numpy.testing._private.utils import clear_and_catch_warnings
from binance.client import Client
import asyncio
import json
import logging 





logging.basicConfig(filename="positionMode.log", 
					format='%(asctime)s %(message)s', 
					filemode='w')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 

async def while_loop():
    while True:
        await asyncio.sleep(5)
        f = open('test.json',)
        data = json.load(f)
        client = Client(data['test-monitor']['apiKey'], data['test-monitor']['apiSecretKey'])
        msg = client.futures_get_position_mode()
        print(msg)
        logger.debug(msg)
        
        

loop=asyncio.get_event_loop()
try:
    asyncio.ensure_future(while_loop())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("program stop")
    loop.close()

