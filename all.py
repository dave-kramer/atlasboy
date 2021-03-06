import json


with open('json/islands.json') as f:
	data = json.load(f)
grid_list = []
for length in data:
	grid = data[length]['grid']
	if grid in grid_list:
		continue
	else:
		grid_list.append(grid)


gridinfo_list = []
for length in data:
	for i in grid_list:
		if data[length]['grid'] == i:
			if not data[length]['discoveries']:
				continue
			else:
				gridinfo_list.append(dict({data[length]['grid']:[data[length]['discoveries'][0]['name'], data[length]['name']]}))


islandinfo_list = []
for length in data:
	for i in grid_list:
		if data[length]['grid'] == i:
			if not data[length]['discoveries']:
				continue
			else:
				islandinfo_list.append(dict({data[length]['discoveries'][0]['name']:[data[length]['name'], data[length]['region'], data[length]['grid'], ', '.join(data[length]['biomeTags']), ', '.join(data[length]['animals']), ', '.join(data[length]['resources'])]}))


with open('json/craftables.json') as f:
	data = json.load(f)
craft_list = []
for length in data:
	craft_list.append(data[length])


with open('json/foods.json') as f:
	data = json.load(f)
food_list = []
for length in data:
	food_list.append(data[length])


with open('json/items.json') as f:
	data = json.load(f)
item_list = []
item_list = data


with open('json/animals.json') as f:
	data = json.load(f)
animal_list = []
animal_list = data['Animals']
