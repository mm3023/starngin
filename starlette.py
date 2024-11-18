#fast ngin starlellte
import starlette
import uvicorn


from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, Router

print("light on inside")

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
