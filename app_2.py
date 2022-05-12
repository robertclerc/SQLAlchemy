from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



engine = create_engine('sqlite://')

# declaration d'une base SQLAlchemy ORM
Base = declarative_base()

# Définition de la classe Message, abrstration ORM ?
class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True)
    message = Column(String)

# utilisation du registre MetaData pour créer la base
Base.metadata.create_all(engine)

#creation de l'objet message à partir de la classe Message

message = Message(message="Hello World!")
print(message.message) # 'Hello World!


# creation de session de gestionnaire de base de données
Session = sessionmaker(bind=engine)
session = Session()

#ajout du message à la session
session.add(message)
#validation des modifications dans la base de données
session.commit()

#extraction des données dans la base de données
query = session.query(Message)
instance = query.first()
print (instance.message) # Hello World!







