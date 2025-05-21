from kivy.uix.accordion import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from .cart_com import CommentaireCard
from kivy.properties import ListProperty,ObjectProperty
from database.crud   import get_discussions_for_user
from database.models import Message, User



class ConversationScreen(Screen):
    user = ObjectProperty(None)
    selected_discussion_id = ObjectProperty(None)
    discussions = ListProperty([])

    def on_enter(self):
        self.discussions = []
        deja_ajoutes = set()

        # Récupère tous les messages où l'utilisateur est impliqué, triés par date descendante
        messages = (
            Message.select()
            .where((Message.sender == self.user) | (Message.receiver == self.user))
            .order_by(Message.id.desc())
        )

        for msg in messages:
            if msg.sender == self.user:
                other_user = msg.receiver
                sob = "vous"
            else:
                other_user = msg.sender
                sob = other_user.username

            # Ne pas ajouter deux fois la même personne
            if other_user.id in deja_ajoutes:
                continue
            deja_ajoutes.add(other_user.id)

            last_date = msg.created_at.strftime("%d/%m/%Y %H:%M") if msg.created_at else ""

            self.discussions.append({
                "discussion_id": other_user.id,
                "user": self.user,
                "user_receiver": other_user,
                "username": self.user.username,
                "avatar": other_user.photo,
                "last_message": msg.content,
                "last_date": last_date,
                "sob": sob,
            })

        print("Discussions formatées :", self.discussions)
        self.ids.rv_conversations.data = self.discussions


            

    def on_conversation_click(self, discussion_id):
        self.selected_discussion_id = discussion_id 
        app = MDApp.get_running_app()
        app.root.current = "discussion"
        app.root.get_screen("discussion").user = self.user
        app.root.get_screen("discussion").discussion_id = discussion_id
        app.root.get_screen("discussion").user_receiver = self.user_receiver
        
        
        self.parent.transition.direction = "left"

    def retour(self):
        self.manager.current = "home"
        self.manager.transition.direction = "right"