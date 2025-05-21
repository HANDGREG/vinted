from datetime import date
from peewee import SqliteDatabase, Model, CharField, TextField, ForeignKeyField, DecimalField, DateField

# Initialiser la base de données SQLite
db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    date_inscription = DateField(default=date.today)  # Date automatique
    adresse = TextField()
    telephone = CharField()
    role = CharField(default='utilisateur')  # Utilisateur ou administrateur
    photo= CharField()

class Produit(BaseModel):
    name = CharField()
    description = TextField()
    price = DecimalField()
    image = CharField()  # Chemin vers l'image
    seller = ForeignKeyField(User, backref='produits')
    
    
class Like (BaseModel):
    utilisateur = ForeignKeyField(User, backref='utilisateur')
    produit = ForeignKeyField(Produit, backref='produit')
    date = DateField(default=date.today)
    
    
    
class Commentaire(BaseModel):
    utilisateur = ForeignKeyField(User, backref='utilisateur')
    produit = ForeignKeyField(Produit, backref='produit')
    commentaire = TextField()
    date = DateField(default=date.today)

# Créer les tables dans la base de données

class Discussion(BaseModel):
    user1 = ForeignKeyField(User, backref='discussions1')
    user2 = ForeignKeyField(User, backref='discussions2')

class Message(BaseModel):
    discussion = ForeignKeyField(Discussion, backref='messages')
    sender = ForeignKeyField(User, backref='sent_messages')
    receiver = ForeignKeyField(User, backref='received_messages')
    content = TextField()
    created_at = DateField(default=date.today)
    
    


def initialize_db():
    db.connect()
    db.create_tables([User, Produit,Commentaire,Like,Discussion,Message], safe=True)
    
    