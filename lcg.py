seed = 3
a = 5
b = 13
m = 32

values_gen = [seed]

## For keeping track of the index
c = 0

for i in range(1, m + 1):
	values_gen.append(((a * values_gen[c]) + b) % m)
	c+=1
	


print(values_gen)