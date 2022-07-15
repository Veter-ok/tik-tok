## Add even numbers
a = [1, 4, 3, 2, 6, 7, 9, 11, 12]
b = []
for i in a:
	if i % 2 == 0:
		b.append(i)
# OR
a = [1, 4, 3, 2, 6, 7, 9, 11, 12]
b = [i for i in a if i % 2 == 0] 

## Change value
a = 5
b = 10
c = a
a = b
b = c
# OR
a, b = b, a

## Short IF
a = 20
if a > 10:
	b = True
else:
	b = False
# OR
b = True if a > 10 else False