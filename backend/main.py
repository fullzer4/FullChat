from ariadne.asgi import GraphQL
from fastapi import FastAPI
from src.schema import schema

app = FastAPI()

app.mount("/graphql/", GraphQL(schema, debug=True))