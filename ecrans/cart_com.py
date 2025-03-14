from kivy.uix.accordion import BooleanProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty , NumericProperty
from kivymd.uix.card import MDCard
from kivymd.app import MDApp





class CommentaireCard(MDCard):
    commentaire = ObjectProperty(None)  # Définir la propriété product
    user=ObjectProperty(None)
    
    