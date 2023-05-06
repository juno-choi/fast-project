from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from question import question_router 

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello/{name}")
def hello(name: str):
    return {
        "message" : name
    }

app.include_router(question_router.router)