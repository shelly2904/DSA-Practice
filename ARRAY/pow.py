#Compute power of number, solutions O(n) and O(log n) where n is the power


def power(x, n):
	if n==0:
		return 1
	return x*power(x, n-1)


def power_rec(x, y):
	temp = 0
	if y == 0:
		return 1
	temp = power_rec(x, y/2);
	if y%2 == 0:
		return temp*temp;
	else:
		return x*temp*temp;


if __name__=="__main__":
	print power(3, 2)
	print power_rec(3, 2)