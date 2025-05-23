from database.models import *
from peewee import fn 
import bcrypt




def create_user(username, email, password,adresse,telephone,photo):
    
    # Hacher le mot de passe
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    user = User.create(
        username=username, 
        email=email, password=hashed_password.decode('utf-8'),  # Convertir en chaîne pour stockage, 
       
        adresse=adresse,
        telephone=telephone,
        
        photo=photo
        )
    return user


def verify_password(user, password):
    """
    Vérifie si le mot de passe fourni correspond au mot de passe haché de l'utilisateur.
    :param user: L'objet utilisateur récupéré de la base de données.
    :param password: Le mot de passe fourni par l'utilisateur.
    :return: True si le mot de passe est correct, False sinon.
    """
    return bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))

def get_user_by_username(username):
    """
    Récupère un utilisateur par son email.
    :param email: L'email de l'utilisateur.
    :return: L'objet utilisateur ou None si non trouvé.
    """
    try:
        return User.get(User.username == username)
    except User.DoesNotExist:
        return None


def get_user_by_id(user_id):
    return User.get(User.id == user_id)




def update_products():
    # Mettre à jour la liste des produits
    product = list(get_all_products())
    return product


def ajout_like(utilisateur,produit):
    like=Like.create(utilisateur=utilisateur,produit=produit)
    return like

def nbre_like(produit):
    """
    Retourne le nombre de likes pour un produit donné.
    """
    return Like.select().where(Like.produit == produit).count()

def sup_like(utilisateur,produit):
    like = Like.delete().where((Like.utilisateur == utilisateur) & (Like.produit == produit)).execute()
    return like


def deja_like(utilisateur,produit):
    like = Like.select().where((Like.utilisateur==utilisateur,) & (Like.produit==produit)).exists()
    return like


def create_product(name, description, price, image, seller_id):
    product = Produit.create(name=name, description=description, price=price, image=image, seller=seller_id)
    
    return product

def get_all_products():
    return Produit.select()

def get_products_by_seller(seller_id):
    return Produit.select().where(Produit.seller == seller_id)





def recup_commentaire(product):
    return Commentaire.select().where(Commentaire.produit == product)


def nbre_commentaire(produit):
    return Commentaire.select().where(Commentaire.produit == produit).count()


def ajout_commentaire(utilisateur,produit,commentaire):
    commentaire = Commentaire.create(utilisateur=utilisateur, produit=produit, commentaire=commentaire)
    return commentaire






# def get_or_create_discussion(user1, user2):
#     discussion, created = Discussion.get_or_create(
#         ((Discussion.user1 == user1) & (Discussion.user2 == user2)) |
#         ((Discussion.user1 == user2) & (Discussion.user2 == user1)),
#         defaults={'user1': user1, 'user2': user2}
#     )
#     return discussion


def get_or_create_discussion(user1, user2):
    discussion = (Discussion
                  .select()
                  .where(
                      ((Discussion.user1 == user1) & (Discussion.user2 == user2)) |
                      ((Discussion.user1 == user2) & (Discussion.user2 == user1))
                  )
                  .first())
    if discussion:
        return discussion
    else:
        return Discussion.create(user1=user1, user2=user2)

def envoi_message(sender, receiver, content):
    discussion = get_or_create_discussion(sender, receiver)
    message = Message.create(
        discussion=discussion,
        sender=sender,
        receiver=receiver,
        content=content
    )
    return message

def recup_message_deux_user(user1, user2):
    get_or_create_discussion(user1, user2)
    return list (Message.select().where(
                    ((Message.sender == user1) & (Message.receiver == user2)) |
                    ((Message.sender == user2) & (Message.receiver == user1))).order_by(Message.created_at))
# def get_discussions_for_user(user):
#     return Discussion.select().where((Discussion.user1 == user) | (Discussion.user2 == user))


def get_discussions_for_user(user):
    return list(
        Discussion.select().where(
            (Discussion.user1 == user) | (Discussion.user2 == user)
        )
    )