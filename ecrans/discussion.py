from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty,ObjectProperty
from database.crud import recup_message_deux_user,envoi_message


from kivy.clock import Clock


class MessageBubble(MDBoxLayout):
    text = StringProperty()
    is_sender = BooleanProperty(False)
    last_date = StringProperty()
    avatar = StringProperty()
    
    
    
    
    
    
class DiscussionScreen(Screen):
    
    
    discussion_id = StringProperty()  # ID de la discussion
    user = ObjectProperty(None)  # Utilisateur connecté
    messages = ListProperty([])  # Liste des messages de la discussion
    user_receiver = ObjectProperty(None)  # Utilisateur avec qui on discute
    """
    Écran de discussion entre deux utilisateurs.
    """
    def on_enter(self):
        
        self.messages = []  # Réinitialiser la liste des messages
        # Récupérer les messages de la discussion
        messages = recup_message_deux_user(self.user, self.user_receiver)
        print("messages récupérés1", messages)
       
        
        for message in messages:
            print(f"message recupéré {message.content} de {message.sender} à {message.receiver} a été envoyé à {message.created_at}")
            if message.sender == self.user:
                is_sender = True
            else:
                is_sender = False
            # Format date for better display
            last_date = (
                message.created_at.strftime("%d/%m/%Y %H:%M")
                if message.created_at
                else ""
            )
            self.messages.append({
                "text": message.content,
                "is_sender": is_sender,
                "last_date": last_date,
                "avatar": self.user_receiver.photo,
            })
        print("messages formatés", self.messages)
        self.ids.rv_messages.data = self.messages
       
        """
        Méthode appelée lorsque l'écran est affiché.
        """
        print("DiscussionScreen: on_enter", self.user_receiver, self.user)
     
     
     
     
     
    # def load_messages(self):
    #     messages = get_messages_from_db(self.selected_discussion_id)
        
    #     self.ids.rv_messages.data = [{
    #         'text': msg.content,
    #         'is_sender': msg.sender == self.current_user,
    #         'timestamp': msg.created_at.strftime("%H:%M"),
    #         'sender_name': msg.sender.username if msg.sender != self.current_user else ""
    #     } for msg in messages]
        
  

    # Force le scroll vers le bas

    # def scroll_to_bottom(*args):
    #     scroll_view = self.ids.scroll_view
    #     scroll_view.scroll_y = 0  # 0 = bas, 1 = haut

    # Clock.schedule_once(scroll_to_bottom, 0.1)


    def send_message(self):
        text = self.ids.message_input.text
        if text.strip():
            envoi_message( self.user, self.user_receiver,text)
            self.ids.message_input.text = ""
            # Ajouter le message à la liste des messages
            self.messages.append({
                "text": text,
                "is_sender": True,
                "last_date": "",
                "avatar": self.user.photo,
            })
            # Mettre à jour l'affichage
            self.ids.rv_messages.data = self.messages
           
        else:
            print("Le message est vide, rien à envoyer.")
       
     
    
    def retour(self):
        self.manager.current = "conversations"
        self.manager.transition.direction = "right"