import uvicorn
from fastapi import FastAPI
from database import Base, engine
from user.routers import user_router
from post.routes import post_router

app = FastAPI()

app.include_router(user_router, prefix='/user')
app.include_router(post_router, prefix='')

Base.metadata.create_all(engine)


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run('main:app', host='localhost', port=8081)
