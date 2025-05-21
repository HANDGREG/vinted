from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from database.crud import get_user_by_id


class ProductDetailsScreen(Screen):
    user= ObjectProperty(None)  # Définir la propriété user
    product = ObjectProperty(None)  # Définir la propriété produc
    
    
    
    def retourhome(self):
        self.parent.current = "home"
        self.parent.transition.direction = "right"
        
    def contact_vendeur(self):
        user= get_user_by_id(self.product.seller_id)
        
        
        app= MDApp.get_running_app()
        app.root.get_screen("discussion").user= self.user
        
        app.root.get_screen("discussion").user_receiver= user
        app.root.get_screen("conversations").user= self.user
        app.root.current = "discussion"
    
        # self.parent.current = "discussion"
        # self.parent.transition.direction = "left"