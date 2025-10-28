from fastapi import FastAPI

app = FastAPI()
    
from routes import router
from auth_routes import auth_router

app.include_router(router)
app.include_router(auth_router)

    




    
    

