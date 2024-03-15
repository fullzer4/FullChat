from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler
from fastapi import FastAPI, Depends, Request
from fastapi.websockets import WebSocket

type_defs = """
    type Query {
        docs: String!
    }
"""

query = QueryType()


@query.field("docs")
def resolve_docs(*_):
    return "See the docs on: https://github.com/fullzer4/FullChat"


def get_context_value(request_or_ws: Request | WebSocket, _data) -> dict:
    return {
        "request": request_or_ws,
        "db": request_or_ws.scope["db"],
    }

schema = make_executable_schema(type_defs, query)

graphql_app = GraphQL(
    schema,
    debug=True,
    context_value=get_context_value,
    websocket_handler=GraphQLTransportWSHandler(),
)

app = FastAPI()

# Botar conexao com banco de dados

@app.get("/graphql/")
@app.options("/graphql/")
async def handle_graphql_explorer(request: Request):
    return await graphql_app.handle_request(request)

@app.post("/graphql/")
async def handle_graphql_query(
    request: Request,
):
    return await graphql_app.handle_request(request)

@app.websocket("/graphql")
async def graphql_subscriptions(
    websocket: WebSocket,
):
    await graphql_app.handle_websocket(websocket)
