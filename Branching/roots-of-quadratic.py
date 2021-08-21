'''Roots of quadratic equation'''
#!/usr/bin/python3

import cmath

a = 1
b = 2
c = 3

d = (b**2)-(4*a*c)

ans1 = (-b-cmath.sqrt(d))/(2*a)
ans2 = (-b+cmath.sqrt(d))/(2*a)

print(f'THE ANSWER IS\n{ans1}\n{ans2}')