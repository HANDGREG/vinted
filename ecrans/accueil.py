from kivy.uix.accordion import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.properties import ListProperty,ObjectProperty
from database.crud   import get_all_products, deja_like , nbre_like, nbre_commentaire




from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout


class HomeScreen(Screen):
    products = ListProperty([])
    user = ObjectProperty(None)  # Définir la propriété user
    def on_enter(self):
        # Charger les produits depuis la base de données
        self.products = list(get_all_products())
        
        
        
        
        
        
        
        self.ids.rv.data = [{"product": product, "user":self.user, "like": deja_like(self.user, product), "nbre_like":nbre_like(product), 'nbre_commentaire':nbre_commentaire(product) } for product in self.products ]  # Mise à jour dynamique
        app= MDApp.get_running_app()
        
        app.root.get_screen("commentaire").user = self.user
        
      
        
        
        
    def logout(self):
        self.parent.current = "login"
        self.parent.transition.direction = "left"
        
        
    def home(self):
        self.parent.current = "home"
        self.parent.transition.direction = "left"
        
        
        
    def ajouter(self):
        app=MDApp.get_running_app()
       
        app.root.current = "ajouter"
        
        app.root.get_screen("ajouter").user = self.user
        self.parent.transition.direction = "up"
        
        
    def profile(self):
        app= MDApp.get_running_app()
        app.root.current = "profile"
        app.root.get_screen("profile").user = self.user
        self.parent.transition.direction = "left"
        
        
    def conversation(self):    
        app= MDApp.get_running_app()
        app.root.get_screen("conversations").user= self.user
        app.root.current = "conversations"
        
        self.parent.transition.direction = "left"


class ClickableBox(ButtonBehavior, MDBoxLayout):
    pass
