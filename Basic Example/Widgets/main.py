from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout

class WidgetExample(GridLayout):
    my_text = StringProperty("Hello !")
    count = StringProperty('0')
    
    def on_press_event(self):
        self.my_text = "You Clicked!"
    
    def increment(self):
        self.count = str(int(self.count)+1)
    

class Widgets(App):
    pass

def mainRun():
    Widgets().run()