from fastapi import FastAPI

from stay_locator.foo import foo

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": foo("New msg")}
