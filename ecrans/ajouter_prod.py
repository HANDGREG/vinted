from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from database.crud import create_product
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDTextButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
import os


class Ajouter(Screen):
    
    user = ObjectProperty(None)  # Définir la propriété user
    
    
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path,
            ext=[".jpg", ".png", ".jpeg", ".webp"],
            preview=True
        )
        self.manager_open = False

    def open_file_manager(self):
        self.file_manager.show(os.path.expanduser("~"))  # ou "/" pour tout le système
        self.manager_open = True

    def select_path(self, path):
        self.ids.image_path.text = path
        toast("Image sélectionnée !")
        self.exit_file_manager()

    def exit_file_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
    
    
    def ajouter_prod(self):
        name=self.ids.name.text
        description=self.ids.description.text
        prix=self.ids.prix.text
        image=self.ids.image_path.text
        
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
            buttons=[MDRaisedButton(text="OK", on_release=lambda x: dialog.dismiss())],
        )
        dialog.open()
        
    
    
    
    
    
    
    
    def retour(self):
        self.parent.current="home"
        self.parent.transition.direction="down"


    