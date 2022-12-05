# A simple Flask API to remove background from images

## Instructions:

1. git clone https://github.com/ornob011/Remove_Background_API.git
2. cd Remove_Background_API
3. pip install -r requirements.txt
4. gunicorn -b 0.0.0.0:8000 app:app
5. Open the link: https://0.0.0.0:8000
6. Input an image to the file submission form.
7. Open the link: https://0.0.0.0:8000/get_image/{ GET api Image ID } to find the background removed image. The {GET api Image ID} could be found from "result.json" file, it could also be found from the webpage. The resultant image is stored into the folder: "removed_bg_downloaded"