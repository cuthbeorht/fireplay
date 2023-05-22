import asyncio
import logging

from fireplay.services import configure_logging, media_libary_service

configure_logging()


async def main():
    mp3 = media_libary_service()

    logging.info("Starting media building process")
    task = asyncio.create_task(mp3.build_music_list(search_path="/Volumes/DropboxData/Music"))
    logging.info("Build in progress...")


asyncio.run(main())

