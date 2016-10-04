import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


from kivy.storage.jsonstore import JsonStore
from os.path import join

class FluffyRecipe(PageLayout):
	pass
	
	def LoadRecipe(self,path):
		self.over = RecipeOverview()
		self.ing = RecipeIngredients()
		self.steps = RecipeSteps()
		self.add_widget(self.over)
		self.add_widget(self.ing)
		self.add_widget(self.steps)

class RecipeOverview(Widget):
	pass

class RecipeIngredients(Widget):
	pass

class RecipeSteps(Widget):
	pass

class FluffyKidney(GridLayout):
	pass

class FluffyKidneyApp(App):

	def build(self):
		data_dir = getattr(self, 'user_data_dir')
		self.store = JsonStore(join(data_dir, 'user.json'))
		self.FK = FluffyKidney()
		return self.FK

if __name__ == '__main__':
	FluffyKidneyApp().run()

