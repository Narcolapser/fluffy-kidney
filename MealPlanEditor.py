from os.path import join
import os
import json

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
		grid = self.ids['info_grid']
		mpe = MealPlanEditor(self)
		self.mpe = mpe
		grid.clear_widgets()
		grid.add_widget(mpe)
	
class MealPlanEditor(BoxLayout):
	def __init__(self, par_screen, **kwargs):
		super(MealPlanEditor, self).__init__(**kwargs)
		self.par_screen = par_screen
	
	def rename(self,val):
		print(val)
