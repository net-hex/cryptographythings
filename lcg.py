## This program is a linear congruency generator, or LCG
## This will generate a series of pseudo-random numbers
## This is not made to be cryptographically secure, it is more of a practical test
## That being said, use it if you like


## A hardcoded start value
seed = 3
## The multiplier. This changes how previous values influence the next in sequence
a = 5
## The increment, for added "randomness"
b = 13
## The modulus, which defines the range of possible values
m = 32

values_gen = [seed]

## For keeping track of the index
c = 0

for i in range(1, m + 1):
	values_gen.append(((a * values_gen[c]) + b) % m)
	c+=1
	


print(values_gen)
