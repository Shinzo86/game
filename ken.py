



italian_dishes = {
        "spaghetti": True,
		"lasagna": False,
		"pizza": False
}

burgers = {
	    "classic": False,
	    "royale": False,
	    "double_whopper": True
}

steaks = {
	    "sirloin": True,
	    "ribeye": False,
	    "new_york_strip": False
}

appetizers = {
	    "mozz_sticks": False,
	    "queso": True
}

desserts = {
		"ice_cream": True,
		"cake": False,
		"pie": False
}

menu = {
	    "italian_dishes": italian_dishes,
	    "burgers": burgers,
	    "steaks": steaks,
	    "appetizers": appetizers,
	    "desserts": desserts
}

def get_items(dishes):
	#for key, value in dishes:
	for key, value in dishes.items():
		print(key)

get_items(menu["italian_dishes"])
print(menu["italian_dishes"]["lasagna"])

# print(italian_dishes["lasagna"])
# print(burgers["double_whopper"])