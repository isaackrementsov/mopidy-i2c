import asyncio
from display import draw_text
from mopidy_async_client import MopidyClient

# Display track & artists on I2C OLED
async def display_track(data):
    tltrack = data['tl_track']
    track = tltrack.track

    draw_text('Playing ' + track.name + ' by ' + ', '.join([a.name for a in track.artists]))

# Initialize Mopidy listener
async def main():
    try:
        # Connect to Mopidy server
        mopidy = await MopidyClient(parse_results=True).connect()
        # Bind display_track to playback start events
        mopidy.listener.bind('track_playback_started', display_track)

        # Run program loop until KeyboardInterrupt or other exception causes an exit
        try:
            while True:
                await asyncio.sleep(0.2)
        except Exception:
            pass

        # Disconnect from Mopidy server
        await mopidy.disconnect()

    # Handle failure to connect
    except Exception:
        print("Failed to connect to Mopidy server. Run `sudo systemctl status mopidy` to check whether it's actually running")

# Run async event loop
asyncio.run(main())
