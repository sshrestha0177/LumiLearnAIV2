from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "LumiLearn Twin is Awake"}
