from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout

class WidgetExample(GridLayout):
    my_text = StringProperty("Hello !")
    count = StringProperty('0')
    state = BooleanProperty(False)
    #percentage = StringProperty("0")
    
    def on_press_event(self):
        self.my_text = "You Clicked!"
    
    def increment(self):
        if self.state:
            self.count = str(int(self.count)+1)
    
    def toggle_on(self, toggle_button):  
        if toggle_button.state == "down":
            toggle_button.text = "ON"
            self.state = True
        else:
            self.state = False
            toggle_button.text = "OFF"

    # def switch_on(self, switch_button):
    #     print(switch_button.active)
    
    # def slider_value(self, slider):
    #     self.percentage = str(int(slider.value))
    

class Widgets(App):
    pass

def mainRun():
    Widgets().run()