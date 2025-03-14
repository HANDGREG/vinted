from kivy.uix.accordion import BooleanProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty , NumericProperty
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from database.crud import ajout_like,sup_like,nbre_like
from ecrans.accueil import HomeScreen



# class ProductCard(MDCard):
#     product = ObjectProperty(None)  # Définir la propriété product
#     user=ObjectProperty(None)
#     like=BooleanProperty(False)  # Propriété pour l'état du like
#     nbre_like = NumericProperty(0)  # Propriété pour le nombre de likes
    


class ReusableProductCard(MDCard): 
    product = ObjectProperty(None)  # Définir la propriété product
    user=ObjectProperty(None)
    like=BooleanProperty(False)  # Propriété pour l'état du like
    nbre_like = NumericProperty(0)  # Propriété pour le nombre de likes
    nbre_commentaire=NumericProperty(0) # Propriété pour
    

    def open_product_details(self):
        """
        Ouvre la page des détails du produit.
        """
        if self.product:
            print(f"Ouvrir les détails du produit : {self.product.name}")
            # Naviguer vers la page des détails du produit
            app = MDApp.get_running_app()
            app.root.current = "details_prod"  # Remplacez par le nom de votre écran de détails
            
            # Passer les données du produit à l'écran de détails
            app.root.get_screen("details_prod").product = self.product
            
    def open_user_details(self):
        """
        Ouvre la page des détails de l'utilisateur (vendeur).
        """
        if self.product and self.product.seller:
            print(f"Ouvrir les détails de l'utilisateur : {self.product.seller.username}")
            # Naviguer vers la page des détails de l'utilisateur
            app = MDApp.get_running_app()
            app.root.current = "details_user"  # Remplacez par le nom de votre écran de détails
            # Passer les données de l'utilisateur à l'écran de détails
            app.root.get_screen("details_user").user = self.product.seller
            
            
            
    def toggle_like(self):

        if self.product and self.user:
            if self.ids.like_button.icon == "heart-outline":
                # Si l'icône est vide, créer un like
                ajout_like(utilisateur=self.user.id, produit=self.product.id)
                self.ids.like_button.icon = "heart"  # Mettre à jour l'icône
            else:
               
                sup_like(utilisateur=self.user.id, produit=self.product.id)
                self.ids.like_button.icon = "heart-outline"  # Mettre à jour l'icône
            
           
            self.ids.like_count.text = str(nbre_like(self.product.id))
           

    def commentaire(self):
       
        if self.product and self.user:
            print(f"Afficher les commentaires du produit : {self.product.name}")
          
            app = MDApp.get_running_app()
            app.root.current = "commentaire"  
            
            
            app.root.get_screen("commentaire").produit = self.product
            app.root.get_screen("commentaire").user = self.user
            
        else :
            print("Veuillez vous connecter pour voir les commentaires.")
            
            
            
            
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.fitimage import FitImage

class ClickableFitImage(ButtonBehavior, FitImage):
    pass


from kivymd.uix.boxlayout import MDBoxLayout

class ClickableBoxLayout(ButtonBehavior, MDBoxLayout):
    pass