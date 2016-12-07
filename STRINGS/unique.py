from collections import defaultdict

def unique(string):
	isUnique = True
	hashmap = defaultdict(int)
	for i in range(0, len(string)):
		for j in range(i+1, len(string)):
			if string[i] == string[j]:
				hashmap[string[i]] += 1
			else:
				hashmap[string[i]] = 1
	for k,v in hashmap.items():
		if v > 1:
			isUnique = False
			break
	return isUnique



if __name__ == '__main__':
	print unique('abcdefghijklmnopqrstuvwxyzABCD')

