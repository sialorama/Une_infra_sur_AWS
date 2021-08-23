from fastapi import FastAPI
import uvicorn
from starlette.responses import RedirectResponse
from data import Data

app = FastAPI()

@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse("/docs")

@app.get("/name")
def name():
    data = Data.name()
    return {'data' : data}

@app.get("/member_info")
def member():
    data = Data.member()
    return {'data' : data}

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)