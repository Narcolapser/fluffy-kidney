import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

from kivy.storage.jsonstore import JsonStore
from os.path import join

class FluffyKidneyMain(GridLayout):
	pass

class FluffyKidneyApp(App):

    def build(self):
        data_dir = getattr(self, 'user_data_dir')
        self.store = JsonStore(join(data_dir, 'user.json'))
        self.FK = FluffyKidneyMain()
        return self.FK


if __name__ == '__main__':
    FluffyKidneyApp().run()
