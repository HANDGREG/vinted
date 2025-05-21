# from kivy.uix.screenmanager import Screen
# from database.crud import get_user_by_username, verify_password

# class Loginscreen(Screen):
#     def login(self):
#         username=self.root.ids.username.text
#         if get_user_by_username(username):
#             password = self.root.ids.password.text
#             if verify_password(get_user_by_username(username), password):
#                 self.parent.current = "home"
                
#                 self.parent.ids.screen_manager.transition.direction = "left"
#             else:from kivymd.uix.button.button import MDButton
#                 self.root.ids.error_label.text = "Mot de passe incorrect"
#                 self.root.ids.password.text = ""
#         else:
#             self.root.ids.error_label.text = "Utilisateur inconnu"
#             self.root.ids.password.text = ""
            


from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDTextButton
from kivymd.uix.dialog import MDDialog
from database.crud import get_user_by_username, verify_password
from kivymd.app import MDApp

class Loginscreen(Screen):
    def login(self):
        # Récupérer les valeurs des champs
        username = self.ids.username.text
        password = self.ids.password.text

        # Vérifier si l'utilisateur existe
        user = get_user_by_username(username)
        if user:
            # Vérifier le mot de passe
            if verify_password(user, password):
                
                 # Naviguer vers la page des détails du produit
                app = MDApp.get_running_app()
                app.root.current = "home"  # Remplacez par le nom de votre écran de détails
                
                 # Passer les données du produit à l'écran de détails
                app.root.get_screen("home").user = user

                
                # Connexion réussie : naviguer vers la page d'accueil
                
                self.parent.current = "home"
                self.parent.transition.direction = "left"
                self.ids.password.text = ""
                self.ids.username.text = ""  # Réinitialiser le champ du nom d'utilisateur
                
            else:
                # Mot de passe incorrect
                self.show_error_dialog("Mot de passe incorrect")
                self.ids.password.text = ""  # Réinitialiser le champ du mot de passe
        else:
            # Utilisateur inconnu
            self.show_error_dialog("Utilisateur inconnu")
            self.ids.password.text = ""  # Réinitialiser le champ du mot de passe

    def show_error_dialog(self, message):
        """Affiche une boîte de dialogue d'erreur."""
        dialog = MDDialog(
            title="Erreur",
            text=message,
            buttons=[MDRaisedButton(text="OK", on_release=lambda x: dialog.dismiss())],
        )
        dialog.open()
        
        
    def  jenaipasdecompte(self):
        self.parent.current = "inscrire"
        self.parent.transition.direction = "up"