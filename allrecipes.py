import requests
from HTMLParser import HTMLParser
import json

def getRecipe(url):
	resp = requests.get(url)
	parser = AllRecipesParser()
	val = parser.feed(resp.text)
	return parser.getJson()


class AllRecipesParser(HTMLParser):
	saving = False
	title = ""
	ingredients = []
	instructions = []
	step = False
	ingred = False
	def handle_starttag(self, tag, attrs):
		ingred = False
		itemprop = False
		direction = False
		title = False
		try:
			for i in attrs:
				if "recipe-ingred_txt" in i[1]:
					ingred = True
				if "ingredients" in i[1]:
					itemprop = True
				if "recipe-directions__list--item" in i[1]:
					direction = True
				if "og:title" in i[1]:
					for j in attrs:
						if 'content' in j[0]:
#							print(j[1])
							self.title = j[1]
					
		except:
			pass
		
		if ingred and itemprop:
			self.ingred = ingred
			self.direction = False
			self.saving = True
		if direction:
			self.step = direction
			self.ingred = False
			self.saving = True
#		if title:
#			self.saving = True

#		if self.saving:
#		print(self.saving,"Encountered a start tag:", tag, attrs)

	def handle_endtag(self, tag):
#		print(self.saving,"Encountered an end tag :", tag)
		if self.saving:
			self.saving = False

	def handle_data(self, data):
#		print(self.saving,"Encountered some data  :", data)
		if self.saving:
#			print("Direction: {0} or Ingrediant: {1}".format(self.direction,self.ingred))
			if self.ingred:
				self.ingredients.append(self.handle_ingredient(data))
			if self.step:
				self.instructions.append('"'+data+'"')
	
	def getJson(self):
		ingred_string = ','.join([json.dumps(x) for x in self.ingredients])
		step_string = ','.join(self.instructions)
		ret =  '''
{
	"name":"''' + self.title + '''",
	"ingredients":['''+ingred_string+'''],
	"instructions":['''+step_string+'''],
	"misc": []
}'''
		jret = json.loads(ret)
		return jret

#		{"ingredient":"sugar","quantity":"5","units":"g"}
	def handle_ingredient(self, datum):
		data = datum.split(' ') 
		val = {}
		val['ingredient'] = ' '.join(data[2:])
		val['quantity'] = data[0]
		val['units'] = data[1]
		return val

if __name__ == '__main__':
	recipe = '''http://allrecipes.com/recipe/6925/monkey-bread-v/'''
	resp = requests.get(recipe)
	parser = AllRecipesParser()
	val = parser.feed(resp.text)
	print(parser.getJson())

#	soup = BeautifulSoup(resp.text)
#	print(getIngredients(soup))
#	print(getInstructions(soup))
#	print(getName(soup))
#	print(getJson(soup))
