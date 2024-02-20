from ariadne import QueryType

hello_query = QueryType()

@hello_query.field("hello")
def resolve_hello(*_):
    return "Hello world!"