from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty


class Profile(Screen):
    user = ObjectProperty(None)  # Définir la propriété user
    
    
    
    def retourhome(self):
        self.parent.current = "home"
        self.parent.transition.direction = "right"