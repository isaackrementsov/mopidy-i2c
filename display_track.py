import asyncio
from mopidy_json_async import MopidyClient

def print_track(data):
    print('Title changed', data)

def main():
    mopidy = await MopidyClient().connect()
    mopidy.listener.bind('track_playback_started', print_track)

    try:
        while(True):
            sleep(0.2)
    except Exception:
        pass

    await mopidy.disconnect()

asyncio.run(main())
