


def fib_me(num, acc):
	if num > 11:
		return True
	print num
	temp = num
	num += acc
	acc = temp
	fib_me(num, acc)

fib_me(1,0)