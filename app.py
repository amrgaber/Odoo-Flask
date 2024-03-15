# import sys
# sys.path.append('/home/amr/PycharmProjects/Odoo17/odoo')
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.urls import router as router_urls

app = FastAPI(title="Odoo-Fastapi")

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_urls)
