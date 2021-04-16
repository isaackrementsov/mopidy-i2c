import asyncio
from mopidy_async_client import MopidyClient

def print_track(data):
    print('Title changed', data)

async def main():
    mopidy = await MopidyClient().connect()
    mopidy.listener.bind('track_playback_started', print_track)

    try:
        while(True):
            sleep(0.2)
    except Exception:
        print('Exiting...')
        pass

    await mopidy.disconnect()

main()
