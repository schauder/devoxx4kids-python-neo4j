import requests
from neo4j.v1 import GraphDatabase

print("hallo")

def create_event(tx, id, type):
    result = tx.run("CREATE (e:Event) "
                    "SET e.id = $id, "
                    " e.type = $type "
                    "RETURN e", id=id, type=type)
    return result.single()[0]


r = requests.get('https://api.github.com/events')
json = r.json()

driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'neo'))

with driver.session() as session:
    for e in json:
        session.write_transaction(create_event, e['id'], e['type'])

driver.close()
