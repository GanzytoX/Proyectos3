import io
import os.path

from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from Google import Create_Service

if __name__ != "__main__":
    def uploadImage(*directions: str):
        CLIENT_SECRET_FILE = "chatbot.json"
        API_NAME = "drive"
        API_VERSION = "v3"
        SCOPES = ["https://www.googleapis.com/auth/drive"]

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        folder_id = "18Eot8d9DQUjzFKQzQui85lmR-ukOPVxN"
        file_names = directions
        mime_types = ["image/png", "image/jpeg"]

        for file_name, mime_type in zip(file_names, mime_types):
            file_metadata = {
                "name": file_name,
                "parents": [folder_id]
            }

            media = MediaFileUpload(file_name, mimetype=mime_type)

            id = service.files().create(
                body=file_metadata,
                media_body=media,
                fields="id"
            ).execute()
            return id

    def downloadImage(id, route):
        CLIENT_SECRET_FILE = "chatbot.json"
        API_NAME = "drive"
        API_VERSION = "v3"
        SCOPES = ["https://www.googleapis.com/auth/drive"]
        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


        request = service.files().get_media(fileId = id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd= fh, request=request)

        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(status)

        fh.seek(0)
        with open(route, "wb") as f:
            f.write(fh.read())
            f.close()




