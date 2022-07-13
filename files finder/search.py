import os

def check_dir(name:str = None, search: str=None):
	ans = []
	for obj in os.listdir(name):
		if '.' in obj:
			if obj == search:
				ans.append(os.path.join(name, obj))
		else:
			if name == None:
				res = check_dir(obj, search)
			else:
				res = check_dir(os.path.join(name, obj), search)
			if len(res) != 0:
				ans += res
	return ans

locations = check_dir(search='text1.txt')
print(locations)