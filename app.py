from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from router import *

app=FastAPI()
app.include_router(router)

origins = [
 "http://localhost.tiangolo.com",
 "https://localhost.tiangolo.com",
 "http://localhost",
 "http://localhost:8080",
]

app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"],
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)