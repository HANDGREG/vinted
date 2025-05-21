from kivy.uix.screenmanager import Screen
from database.crud import create_user
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDTextButton
from kivymd.uix.dialog import MDDialog



class Register(Screen):
    def inscription(self):
        username=self.ids.username.text
        email=self.ids.mail.text
        password=self.ids.password.text
        adresse=self.ids.adresse.text
        telephone=self.ids.telephone.text
        photo=self.ids.photo.text
        
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
            buttons=[MDButton(text="OK", on_release=lambda x: dialog.dismiss())],
        )
        dialog.open()    
    def compteexistant(self):
        self.parent.current = "login"
        self.parent.transition.direction = "down"