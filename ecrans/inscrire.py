from kivy.uix.screenmanager import Screen
from database.crud import create_user
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDTextButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
import os


class Register(Screen):
    
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path,
            ext=[".jpg", ".png", ".jpeg", ".webp"],
            preview=True
        )
        self.manager_open = False
    def inscription(self):
        username=self.ids.username.text
        email=self.ids.mail.text
        password=self.ids.password.text
        adresse=self.ids.adresse.text
        telephone=self.ids.telephone.text
        photo=self.ids.photo_path.text
        
        create_user(
            username=username,
            email=email,
            password=password,
            
            adresse=adresse,
            telephone=telephone,
         
            photo=photo
        )
        self.show_error_dialog("inscription reuissi")
        self.parent.current = "login"
        self.parent.transition.direction = "right"

    
    
    def show_error_dialog(self, message):
        """Affiche une boîte de dialogue d'erreur."""
        dialog = MDDialog(
            title="succes",
            text=message,
            buttons=[MDRaisedButton(text="OK", on_release=lambda x: dialog.dismiss())],
        )
        dialog.open()    
    def compteexistant(self):
        self.parent.current = "login"
        self.parent.transition.direction = "down"
        
        
    def open_file_manager(self):
        self.file_manager.show(os.path.expanduser("~"))  # Ouvre sur le dossier utilisateur
        self.manager_open = True

    def select_path(self, path):
        self.ids.photo_path.text = path
        toast("Photo sélectionnée")
        self.exit_file_manager()

    def exit_file_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
        
    def on_back_button(self):
        if self.manager_open:
            self.exit_file_manager()
