"""
from alive_progress import alive_bar
import time

items = list(range(100))
with alive_bar(total=100) as bar:
    for item in items:
        # print(f'обработка - {item}')
        time.sleep(0.05)
        bar()


import time
from alive_progress import alive_bar
from alive_progress.styles import showtime, Show

showtime(Show.BARS)
items = list(range(100))
with alive_bar(total=100) as bar:
    for item in items:
        time.sleep(0.05)
        bar()
"""

from tqdm.asyncio import tqdm
with tqdm(range(9)) as pbar:
    async for i in pbar:
        if i == 2:
            break
