from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, NumericProperty

class RecipePane(ScrollView):
	grid = ObjectProperty(None)

class RecipeOverview(RecipePane):
	
	name = StringProperty("Loading...")
	
	def loadRecipe(self,val):
		self.val = val
		self.name = "\n\n\n\n" + val['name']

class RecipeIngredients(RecipePane):
	
	name = StringProperty("Loading...")
	
	def loadRecipe(self,val):
		self.val = val
		self.name = '\n\nIngredients'
		for i in val['ingredients']:
			l = Label()
			l.text_size = 800, None
			l.size_hint_y = None
			l.height = 400
			l.text = str(i['quantity'])+i['units']+" "+i['ingredient']
			self.grid.add_widget(l)

class RecipeSteps(RecipePane):
	
	name = StringProperty("Loading...")
	width_p = NumericProperty(400)
	
	def loadRecipe(self,val):
		self.val = val
		self.name = '\n\nInstructions'
		for i in val['instructions']:
			l = Label(text=i)
			l.text_size = 800, None
			l.size_hint_y = None
			l.height = 400
			self.grid.add_widget(l)
