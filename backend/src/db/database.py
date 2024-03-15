from neo4j import GraphDatabase

URI = "neo4j://localhost:7474"
AUTH = ("", "")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
