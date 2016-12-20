from os.path import join
import os
import json
from threading import Event

import allrecipes

import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.core.clipboard import Clipboard

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.storage.jsonstore import JsonStore

from RecipePane import *

class ListRecipe(Button):
	name = StringProperty("Loading...")

	def loadRecipe(self,val,grid):
		self.config = val
		self.name = val['name']
		self.info_pane = grid
	
	def selected(self):
#		self.info_pane.replaceRecipe(self.config)
		self.info_pane.clear_widgets()
		r = FluffyRecipe()
		r.loadRecipe(self.config)
		self.info_pane.add_widget(r)

class FluffyRecipe(PageLayout):
	first = True
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
	
	def replaceRecipe(self,val):
		if not self.first:
			self.clear_widgets()
		self.first = False
		self.loadRecipe(val)

class MealPlanScreen(Screen):
	
	def loadRecipes(self,data_dir):
		files = os.listdir(data_dir)
		grid = self.ids['info_grid']
		rlist = self.ids['recipe_list']
		for i in files:
			print(i)
			if i[-5:] != ".json":
				continue
			with open(join(data_dir,i)) as f:
				try:
					val = json.load(f)
				except Exception as e:
					continue
#			print(val.keys())
			if 'ingredients' in val.keys():
				recipe = ListRecipe()
				recipe.loadRecipe(val,grid)
				rlist.add_widget(recipe)
		#rUrl = '''http://allrecipes.com/recipe/24352/easy-apple-cinnamon-muffins/'''
		#rUrl = '''http://allrecipes.com/recipe/6925/monkey-bread-v/'''
		rUrl = '''http://allrecipes.com/recipe/7324/angel-food-cake-i/'''
		recipe = ListRecipe()
		recipe.loadRecipe(allrecipes.getRecipe(rUrl),grid)
		rlist.add_widget(recipe)
	
	def openMainMenu(self):
		self.app.sm.current = 'main_menu'

class MealPlanEditorScreen(Screen):

	def loadPlans(self):
		files = os.listdir(self.app.data_dir)
		grid = self.ids['info_grid']
		plist = self.ids['plan_list']
		
		for i in files:
			if 'meal_plan' in i:
				print(i)
				with open(join(self.app.data_dir,i)) as f:
					try:
						val = json.load(f)
					except Exception as e:
						print(e)

	def openMainMenu(self):
		self.app.sm.current = 'main_menu'
		
	def newMealPlan(self):
		plist = self.ids['plan_list']
		gt = GetText()
		gt.ask()

class MainMenuScreen(Screen):
	
	def openMealPlan(self):
		if not self.app.sm.has_screen('meal_plan'):
			self.app.meal_plan_screen = MealPlanScreen(name='meal_plan')
			self.app.meal_plan_screen.loadRecipes(self.app.data_dir)
			self.app.meal_plan_screen.app = self.app
			self.app.sm.add_widget(app.meal_plan_screen)
		self.app.sm.current = 'meal_plan'
	
	def openMealPlanEditor(self):
		if not self.app.sm.has_screen('meal_plan_editor'):
			self.app.meal_plan_editor_screen = MealPlanEditorScreen(name='meal_plan_editor')
			self.app.meal_plan_editor_screen.app = self.app
			self.app.meal_plan_editor_screen.loadPlans()
			self.app.sm.add_widget(app.meal_plan_editor_screen)
		self.app.sm.current = 'meal_plan_editor'

class FKScreenManager(ScreenManager):
	pass

class GetText(Popup):
	def __init__(self,**kwargs):
		self.content = BoxLayout(orientation="vertical")
		self.content.add_widget(Label(text="Enter meal plan name:"))
		self.ins = TextInput(multiline=False)
		self.content.add_widget(self.ins)
		self.ok_button = Button(text="Ok")
		self.content.add_widget(self.ok_button)
		self.ok_button.bind(on_release=self.done)
		self.pevent = Event()
		
		super(GetText,self).__init__(content=self.content,**kwargs)
	
	def ask(self):
		self.open()
		print("popup opened. waiting...")
		print("Woken up!")
		print(self.val)
		return self.val
	
	def done(self,*args):
		print(self.ins.text)
		self.val = self.ins.text

class FluffyKidneyApp(App):

	def build(self):
		data_dir = getattr(self, 'user_data_dir')
		self.data_dir = data_dir
		self.store = JsonStore(join(data_dir, 'user.json'))
		self.sm = FKScreenManager()

		self.main_menu_screen = MainMenuScreen(name='main_menu')
		self.main_menu_screen.app = self
		self.sm.add_widget(self.main_menu_screen)

#	def on_pause(self):
#		return True

#	def on_resume(self):
#		pass

		return self.sm

app = None
if __name__ == '__main__':
	app = FluffyKidneyApp()
	app.run()
