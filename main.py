import asyncio
from display import draw_text
from mopidy_async_client import MopidyClient

display = I2C_LCD_Driver.lcd()

async def display_track(data):
    tltrack = data['tl_track']
    track = tltrack.track

    draw_text('Playing ' + track.name + ' by ' + ', '.join([a.name for a in track.artists]))

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
