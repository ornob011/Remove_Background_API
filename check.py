from fastapi import FastAPI, File
from rembg import remove
import uvicorn
from starlette.responses import Response
from asyncer import asyncify
app = FastAPI()

def im_without_bg(content: bytes) -> Response:
        return Response(remove(content),media_type="image/png")
@app.get('/')
async def hello():
    return "Hello, user"


@app.post('/api/remove_bg')
async def post_index(file: bytes = File(default=..., description="Image file (byte stream) that has to be processed.")):
    return await asyncify(im_without_bg)(file)


# async def remove_bg(file: bytes = File(...)):

#     output = remove(file)

#     return "success"


#if __name__=='__main__':
#    uvicorn.run("check:app", port=8000, host='0.0.0.0', reload=True)
