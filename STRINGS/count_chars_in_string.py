#Counting characters in string
#for ex: aabbb => a2b3
#for ex: aber => a1b1e1r1

def count_char(string):
	res = ''
	for i in range(0, len(string)):
		j = len(string) - 1
		count = 1
		if string[i] not in res:
			while j > i:
				if string[j] == string[i]:
					count+=1
				j -= 1
			res += string[i]+str(count)

	return res



if __name__=="__main__":
	print count_char("abababbcdfsda")

