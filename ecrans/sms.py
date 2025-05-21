from kivy.uix.accordion import BooleanProperty

from kivy.properties import ObjectProperty , NumericProperty


from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, BooleanProperty

class MessageBubble(MDBoxLayout):
    text = StringProperty()
    is_sender = BooleanProperty(False)