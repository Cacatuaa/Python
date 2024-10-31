# https://www.hackerrank.com/challenges/find-angle/problem
import math

ab = int(input(""))
bc = int(input(""))
hyp = math.sqrt(pow(ab, 2) + pow(bc, 2))
print(hyp)
angle = math.sin((hyp / 2) / bc)
print(math.degrees((math.asin(angle))))