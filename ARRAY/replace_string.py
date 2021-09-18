def make_replace_extra_space(S):
	i = 0
	n = len(S)
	S_new = ''
	while i < n:
		if S[i] == "b":
			pass
		elif S[i] == "a":
			S_new += "dd"
		else:
			S_new += S[i]
		i+=1
	print(S_new)


def make_replace_no_space(S):
	# print "the old string ", S
	i = 0
	n = len(S)
	while i < n or i+1 < n:
		if S[i] == "b":
			S = S[0:i] + S[i+1:]
		elif S[i] == "a":
			S = S[0:i] + "bb" + S[i+1:]
			i+=2
		else:
			i+=1
		n = len(S)
	print("the new string ", S)



if __name__ == '__main__':
	#make_replace_extra_space(A)
	make_replace_no_space('ab')
	make_replace_no_space('black')
	make_replace_no_space('zbbbbc')
	make_replace_no_space('cbbaxaxaxaxaxll')
	make_replace_no_space('blast')
