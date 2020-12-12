from db.run_sql import run_sql

from models.trainer import Trainer

def save(trainer):
    sql = "INSERT INTO trainers (name, address, pokenav) VALUES (%s, %s, %s) RETURNING id"
    values = [trainer.name, trainer.address, trainer.pokenav]
    results = run_sql( sql, values )
    trainer.id = results[0]['id']
    return trainer