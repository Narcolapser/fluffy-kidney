from os.path import join
import os
import json

import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.storage.jsonstore import JsonStore

class FluffyRecipe(PageLayout):
	pass
	
	def loadRecipe(self,val):
		self.over = RecipeOverview()
		self.over.loadRecipe(val)
		self.ing = RecipeIngredients()
		self.ing.loadRecipe(val)
		self.steps = RecipeSteps()
		self.steps.loadRecipe(val)
		self.add_widget(self.over)
		self.add_widget(self.ing)
		self.add_widget(self.steps)

class RecipePane(BoxLayout):
	pass

class RecipeOverview(RecipePane):
	
	name = StringProperty("Loading...")
	
	def loadRecipe(self,val):
		self.val = val
		self.name = val['name']

class RecipeIngredients(RecipePane):
	
	name = StringProperty("Loading...")
	
	def loadRecipe(self,val):
		self.val = val
		self.name = 'ingredients'

class RecipeSteps(RecipePane):
	
	name = StringProperty("Loading...")
	
	def loadRecipe(self,val):
		self.val = val
		self.name = 'instructions'

class FluffyKidney(GridLayout):
	
	def loadRecipes(self,data_dir):
		files = os.listdir(data_dir)
		grid = self.ids['info_grid']
		for i in files:
			if i[-5:] != ".json":
				continue
			with open(join(data_dir,i)) as f:
				try:
					val = json.load(f)
				except Exception as e:
					continue
			print(val.keys())
			if 'ingredients' in val.keys():
				recipe = FluffyRecipe()
				recipe.loadRecipe(val)
				grid.add_widget(recipe)

class FluffyKidneyApp(App):

	def build(self):
		data_dir = getattr(self, 'user_data_dir')
		self.data_dir = data_dir
		self.store = JsonStore(join(data_dir, 'user.json'))
		self.FK = FluffyKidney()
		self.FK.loadRecipes(data_dir)
		return self.FK

if __name__ == '__main__':
	FluffyKidneyApp().run()

