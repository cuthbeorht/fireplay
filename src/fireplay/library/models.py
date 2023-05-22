from typing import Optional

from pydantic import BaseModel


class MediaLibraryItem(BaseModel):
    id: Optional[str]
    title: str
    file_name: str
    size: int
    media_type: str
    full_file_and_path: str
