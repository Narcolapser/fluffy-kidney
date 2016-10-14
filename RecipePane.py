from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from kivy.properties import ObjectProperty, StringProperty, BooleanProperty

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
		self.name = 'Ingredients'
		for i in val['ingredients']:
			l = Label()
			l.text = str(i['quantity'])+i['units']+"     of "+i['ingredient']
			self.add_widget(l)

class RecipeSteps(RecipePane):
	
	name = StringProperty("Loading...")
	
	def loadRecipe(self,val):
		self.val = val
		self.name = 'Instructions'
		for i in val['instructions']:
			l = Label(text=i)
			self.add_widget(l)
