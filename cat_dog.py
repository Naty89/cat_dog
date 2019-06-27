def cat_dog(str):
	for i in range(len(str)-1):
		if str[i:i+2] == "cat":
			if str[i:i+2] == "dog":
		return True
	return False

print(cat_dog("catdog"))
