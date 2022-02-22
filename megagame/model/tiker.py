import asyncio
import time

TIK_TIME = 0.5


class Tiker:
    async def start(self, method_on_tic):
        prev_time = time.time()
        while True:
            current_time = time.time()
            delta_time = current_time - prev_time
            prev_time = current_time
            count = int(delta_time / TIK_TIME)
            prev_time -= delta_time % TIK_TIME

            await method_on_tic(count)
            await asyncio.sleep(TIK_TIME)
