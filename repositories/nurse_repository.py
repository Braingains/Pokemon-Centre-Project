from db.run_sql import run_sql

from models.nurse import Nurse

def save(nurse):
    sql = "INSERT INTO nurses (name) VALUES (%s) RETURNING id"
    values = [nurse.name]
    results = run_sql( sql, values )
    nurse.id = results[0]['id']
    return nurse

def select_all():
    nurses = []
    sql = "SELECT * FROM nurses"
    results = run_sql(sql)
    for result in results:
        nurse = Nurse(result["name"], result["id"])
        nurses.append(nurse)
    return nurses
