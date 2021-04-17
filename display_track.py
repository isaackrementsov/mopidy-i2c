import asyncio

from mopidy_async_client import MopidyClient


async def display_track(data):
    tltrack = data['tl_track']
    track = tltrack.track
    print('Name:', track.name)
    print('Artists:', ', '.join([a.name for a in track.artists]))

async def main():
    mopidy = await MopidyClient(parse_results=True).connect()
    mopidy.listener.bind('track_playback_started', display_track)

    try:
        while True:
            await asyncio.sleep(0.2)
    except Exception:
        pass

    await mopidy.disconnect()


asyncio.run(main())
