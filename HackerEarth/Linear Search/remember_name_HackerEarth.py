from collections import defaultdict

if __name__== "__main__":
	n = int(raw_input())
	di = defaultdict(int)
	
	for i in range(0, n):
		weightage = 1
		mes = raw_input()

		if 'G:' in mes:
			weightage = 2

		all_digits = [int(s) for s in mes.split() if s.isdigit()]

		for num in all_digits:
			if 'G:' in mes:
				di[num] += 2
			else:
				di[num] += 1
			
	values = di.values()
	max_value = max(di.values())
	max_idx = values.index(max_value)
	max_key = di.keys()[max_idx]
	
	if max_key in [19, 20]:
		print "Date"
	elif len(list(set(values))) != len(values):
		print "No Date"
	else:
		print " No Date"