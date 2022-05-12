from sqlalchemy import create_engine, Column, Integer, Text, MetaData, Table, select

# Creation du moteur SQLAlchemy
engine = create_engine('sqlite://')


#Catalogue de tables
metadata = MetaData()

#Definition de la table
messages = Table(
    'messages', metadata,
    Column('id', Integer, primary_key=True),
    Column('message', Text),
)

#creation de la table
messages.create(bind=engine)

#insertion de données dana la table messages
insert_message = messages.insert().values(message='Hello, World!')
engine.execute(insert_message)

#insertion de données dana la table messages
insert_message = messages.insert().values(message='test second insert')
engine.execute(insert_message)

#interrogation dans la base de donnees
stmt = select([messages.c.message]) 
message, = engine.execute(stmt).fetchone()
print(message)
