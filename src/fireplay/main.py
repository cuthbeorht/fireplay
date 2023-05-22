import asyncio
import logging

from fireplay import media_libary_service
from fireplay.services import configure_logging

configure_logging()


async def main():
    mp3 = media_libary_service()

    logging.info("Starting media building process")
    await mp3.build_music_list(search_path="/Volumes/DropboxData/Music")
    logging.info("Build in progress...")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
