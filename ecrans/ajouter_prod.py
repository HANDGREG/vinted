from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from database.crud import create_product
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDTextButton


class Ajouter(Screen):
    
    user = ObjectProperty(None)  # Définir la propriété user
    
    
    def ajouter_prod(self):
        name=self.ids.name.text
        description=self.ids.description.text
        prix=self.ids.prix.text
        image=self.ids.image.text
        
        if self.user.id:
            create_product(name=name, description=description, price=prix, image=image,seller_id=self.user.id)
            self.parent.current="home"
        else :
            self.show_error_dialog("veuillez vous connecter pour pouvoir ajouter un article")
            self.parent.current="login"
            
            
            
            
    def show_error_dialog(self, message):
        """Affiche une boîte de dialogue d'erreur."""
        dialog = MDDialog(
            title="Erreur",
            text=message,
            buttons=[MDButton(text="OK", on_release=lambda x: dialog.dismiss())],
        )
        dialog.open()
        
    
    
    
    
    
    
    
    def retour(self):
        self.parent.current="home"
        self.parent.transition.direction="down"


    