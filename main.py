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


@app.get("/funcaoteste003")
async def funcaoteste():
    return {"teste": " não deu certo, porém verificar item c "}

@app.get("/funcaoteste004")
async def funcaoteste():
    return {"teste": " não deu certo, porém verificar item a e b "}

@app.get("/funcaoteste005")
async def funcaoteste():
    return {"teste": " deu certo "}