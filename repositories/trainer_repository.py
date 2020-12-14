# from db.run_sql import run_sql

# from models.trainer import Trainer

# def save(trainer):
#     sql = "INSERT INTO trainers (name, address, pokenav) VALUES (%s, %s, %s) RETURNING id"
#     values = [trainer.name, trainer.address, trainer.pokenav]
#     results = run_sql( sql, values )
#     trainer.id = results[0]['id']
#     return trainer

# def select_all():
#     trainers = []

#     sql = "SELECT * FROM trainers"
#     results = run_sql(sql)
#     for row in results:
#         trainer = Trainer(row['name'], row['address'], row['pokenav'], row['id'])
#         trainers.append(trainer)
#     return trainers

# def select(id):
#     trainer = None
#     sql = "SELECT * FROM trainers WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         trainer = Trainer(result['name'], result['address'], result['pokenav'], result['id'])
#     return trainer 

# def update(trainer):
#     sql = "UPDATE trainers SET (name, address, pokenav) = (%s, %s, %s) WHERE id = %s"
#     values = [trainer.name, trainer.address, trainer.pokenav]
#     run_sql(sql, values)

# def delete(id):
#     sql = "DELETE FROM trainers WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)

# def delete_all():
#     sql = "DELETE FROM trainers"
#     run_sql(sql)