from kivy.uix.accordion import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from .cart_com import CommentaireCard
from kivy.properties import ListProperty,ObjectProperty
from database.crud   import recup_commentaire,ajout_commentaire,nbre_commentaire


class CommentairesScreen(Screen):
    produit = ObjectProperty(None)
    user = ObjectProperty(None)  # Définir la propriété user
    commentaires = ListProperty([])  # Définir la propriété commentaire
    
    
    def on_enter(self):
       
        self.commentaires = list(recup_commentaire(self.produit))
        print(self.commentaires)       
        
        self.ids.rv_commentaires.data = [{"commentaire": commentaire, "user":self.user,  } for commentaire in self.commentaires ]  # Mise à jour dynamique
        
        
        app= MDApp.get_running_app()
        
        app.root.get_screen("commentaire").user = self.user
        self.parent.transition.direction = "left"
        
        
        
    def Ajout_commentaire(self):
        commentaire = self.ids.input_commentaire.text
        if commentaire:
            com=ajout_commentaire(self.user, self.produit, commentaire)
            self.commentaires.append({"commentaire": com, "user": self.user,  })
            self.ids.input_commentaire.text = ""
            
            self.on_enter()
            
        else:
            print("Veuillez écrire un commentaire.")
        
        
    def retour(self):
        self.parent.current="home"
        self.parent.transition.direction="right"