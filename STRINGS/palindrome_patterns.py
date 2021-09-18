# #Check the palindromic patterns exists in a string
# #example: "YYYABBBA" gives "YY", "YYY", "ABBA", "BB"
#
# #---------METHOD 1---------------#
# def palindrome_patterns(string):
# 	out = []
# 	for i in range(0, len(string)):
# 		end_idx = len(string)-1
# 		while end_idx > i:
# 			if string[i] == string[end_idx]:
# 				print i, end_idx, string[i], string[end_idx]
# 				if check_palindrome(string[i:end_idx+1]):
# 					out.append(string[i:end_idx+1])
# 			end_idx -= 1
# 	return set(out)
#
#
# def check_palindrome(string):
# 	print "String to check", string
# 	start = 0
# 	end = len(string)-1
# 	match = False
# 	while start <= end:
# 		if string[start] == string[end]:
# 			match = True
# 			end -= 1
# 			start += 1
# 		else:
# 			match = False
# 			break
# 	return match
#
#
#
# #---------METHOD 2---------------#
#
# def palindrome_patterns2(string):
# 	pal = []
# 	for i in range(0, len(string)):
# 		left = i
# 		right = i+1
# 		while left != -1 and right < len(string):
# 			if string[left] == string[right]:
# 				pal.append(string[left:right+1])
# 			if left-1 == -1:
# 				break
# 			if string[left-1] == string[right]:
# 				pal.append(string[left-1:right+1])
# 				left -= 1
# 				right +=1
# 			elif string[left-1] != string[right]:
# 				right +=1
# 			else:
# 				break
# 	return list(set(pal))
#
#
#
# print palindrome_patterns2('YYY')
# print palindrome_patterns2('YYYY')
# print palindrome_patterns2('ABCBA')
#
#
# #print palindrome_patterns("YYY")

class Solution:
	def swap(self, a, b):
		temp = a
		a = b
		b = temp
		return a, b

	# Function to reverse words in a given string.
	def reverseWords(self, S):
		stack = []
		for i in S:
			stack.append(i)
			print(stack)
		S = ''
		while stack:
			S += stack[-1]
			stack.pop()

		return S

	# code here

sol = Solution()
print(sol.reverseWords("racecase"))
