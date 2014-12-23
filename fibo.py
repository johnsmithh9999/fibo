def fib(n):
	a = 0
	b = 1
	while a < n:
		print(a, end=' ')
		c = a+b
		a = b
		b = c
	print()
fib(1000000000)

x = 7
y = 8
x, y = y, x+y

print("x= ", x, " Y= ", y)