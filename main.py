from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from database.models import initialize_db 
from database.crud import *
from ecrans.accueil import HomeScreen
from ecrans.carte_prod import ReusableProductCard  # Importer la classe
from kivy.uix.screenmanager import Screen
from ecrans.details_prod import ProductDetailsScreen
from ecrans.details_user import UserDetailsScreen
from ecrans.login import Loginscreen
from ecrans.inscrire import Register
from ecrans.ajouter_prod import Ajouter
from ecrans.profile import Profile
from ecrans.commentaire import CommentairesScreen






class VintedApp(MDApp):
    def build(self):
        
        
        

        Builder.load_file("ecrans/carte_prod.kv")
        Builder.load_file("ecrans/cart_com.kv")
        # Charger les fichiers KV
        Builder.load_file("ecrans/acceuil.kv")

        Builder.load_file("ecrans/details_prod.kv")
        Builder.load_file("ecrans/details_user.kv")
        Builder.load_file("ecrans/login.kv")
        Builder.load_file("ecrans/inscrire.kv")
        Builder.load_file("ecrans/ajouter_prod.kv")
        Builder.load_file("ecrans/profile.kv")
        Builder.load_file("ecrans/commentaire.kv")
        # Initialiser la base de données
        initialize_db()
        
        
        # create_user(
        #     username="MouadNadif",
        #     email="mouad@vinted.com",
        #     password="secret",
           
        #     date_inscription="2021-01-01",
        #     adresse="123 rue de la paix",
        #     telephone="0612345678",
        #     role="Utilisateur",  # Utilisateur ou administrateur
        #     photo="photoproj/mouad-nadif-MdNtXJG462k-unsplash.jpg"  # Chemin relatif vers la photo de profil

        # )
        
        
        # create_product(
        #     name="Montre en or",
        #     description="Une magnifique montre en or 18 carats.",
        #     price=500.00,
        #     image="photoproj/mouad-nadif-MdNtXJG462k-unsplash.jpg",  # Chemin relatif vers l'image
        #     seller_id=2 # ID du vendeur (utilisateur)  
               
        # )
        
        
        
        
        # ajout_commentaire(

        #     utilisateur="1",
        #     produit="1",
           
        #     commentaire="C'était une belle montre"
            
            
        # )
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Pink"

        # Créer un gestionnaire d'écrans
        sm = ScreenManager()
        sm.add_widget(Loginscreen(name="login"))
        sm.add_widget(Register(name="inscrire"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ProductDetailsScreen(name="details_prod"))
        sm.add_widget(UserDetailsScreen(name="details_user"))
        sm.add_widget(Ajouter(name="ajouter"))
        sm.add_widget(Profile(name="profile"))
        sm.add_widget(CommentairesScreen(name="commentaire"))
        # sm.add_widget(Loginscreen(name="login"))
        # sm.add_widget(Register(name="inscrire"))
        return sm

if __name__ == "__main__":
    VintedApp().run()