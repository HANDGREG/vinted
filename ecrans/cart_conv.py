from kivy.uix.accordion import BooleanProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty , NumericProperty
from kivymd.uix.card import MDCard
from kivymd.app import MDApp




class ConversationCard(MDCard):
    discussion_id = ObjectProperty(None)  # ID de la discussion
    avatar = ObjectProperty(None)  # Avatar de l'utilisateur
    user = ObjectProperty(None)  # Utilisateur connecté
    user_receiver = ObjectProperty(None)  # Utilisateur avec qui on discute
    last_message = ObjectProperty(None)  # Dernier message de la discussion
    last_date = ObjectProperty(None)  # Date du dernier message
    sob = ObjectProperty(None)  # S'il s'agit de l'utilisateur connecté ou de l'autre utilisateur
    
    def on_conversation_click(self, discussion_id):
        self.discussion_id = discussion_id
        app = MDApp.get_running_app()
        app.root.current = "discussion"
        app.root.get_screen("discussion").user = self.user
        app.root.get_screen("discussion").user_receiver = self.user_receiver
        # app.root.get_screen("discussion").discussion_id = self.discussion_id
        
    