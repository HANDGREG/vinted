from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty


class ProductDetailsScreen(Screen):
    product = ObjectProperty(None)  # Définir la propriété produc
    
    
    
    def retourhome(self):
        self.parent.current = "home"
        self.parent.transition.direction = "right"