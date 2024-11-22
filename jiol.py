
#os.environ['PYTHONPATH'] = '/zenviroment/bin'

import sys
import os
print(sys.path);
os.environ['PYTHONPATH'] = '/zenviroment/bin'
#os.environ['PYTHONPATH'] = '/zenviroment/bin'
print(sys.path);

#import sys

import starlette
import uvicorn


from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, Router
from starlette.requests import Request
from starlette.responses import Response

print("light on inside")

async def homepage(request):
    return JSONResponse({'hello': 'world'})




#app = Starlette()

app = Starlette(debug=True, routes=[
    Route('/', homepage),
])






app = App()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")

'''



async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, world!',
    })


    import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    request = Request(scope, receive)
    content = '%s %s' % (request.method, request.url.path)
    response = Response(content, media_type='text/plain')
    await response(scope, receive, send)



app = Starlette()
router = Router()
@router.on_event("startup")
async def connect_to_database():
    # Perform database connection logic here
    print("Database connected on startup")



@router.get("/")
async def homepage(request):
    return JSONResponse({"message": "Hello World!"})


app.add_routes(router)
'''






