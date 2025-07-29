from fastapi import FastAPI

app = FastAPI()

@app.post("/User")
def create_user():
    return "User Created"