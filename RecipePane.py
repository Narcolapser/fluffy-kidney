from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.image import AsyncImage

from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, NumericProperty

class RecipePane(ScrollView):
	grid = ObjectProperty(None)

class RecipeOverview(RecipePane):
	
	name = StringProperty("Loading...")
	
	def loadRecipe(self,val):
		self.val = val
		self.name = "\n\n\n\n" + val['name']

#AsyncImage(source='http://mywebsite.com/logo.png')
class RecipePicture(AsyncImage):
	pass

class RecipeIngredients(RecipePane):
	
	name = StringProperty("Loading...")
	
	def loadRecipe(self,val):
		self.val = val
		self.name = '\n\nIngredients'
		for i in val['ingredients']:
			l = RecipeIngredient(i)
			self.grid.add_widget(l)

class RecipeIngredient(BoxLayout):
	name = StringProperty("Loading...")
	quantity = StringProperty("Loading...")
	units = StringProperty("Loading...")
	def __init__(self, ingredient, **kwargs):
		self.ingred = ingredient
		self.quantity = ingredient['quantity']
		self.units = ingredient['units']
		self.name = ingredient['ingredient']
		super(RecipeIngredient, self).__init__(**kwargs)

class RecipeSteps(RecipePane):
	
	name = StringProperty("Loading...")
	width_p = NumericProperty(0)
	
	def loadRecipe(self,val):
		self.val = val
		self.name = '\n\nInstructions\n\n'
		for i in val['instructions']:
			l = RecipeStep(text=i)
			self.grid.add_widget(l)

class RecipeStep(Label):
	pass

