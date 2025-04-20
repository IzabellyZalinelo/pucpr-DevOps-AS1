from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}


@app.get("/funcaoteste1")
async def funcaoteste():
    return {"teste": "deu certo"}

@app.get("/funcaoteste002")
async def funcaoteste():
    return {"teste": " não deu certo"}