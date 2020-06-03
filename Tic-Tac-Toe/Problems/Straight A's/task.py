# put your python code here
# A	4.00
# B	3.00
# C	2.00
# D
# (only applicable for
#     Undergraduate Programs)	1.00
# F	0.00

grads = {"A": 1, "B": 0, "C": 0, "D": 0, "F": 0}

total = [grads[x] for x in input().split()]
final = round(sum(total) / (len(total)), 2)
print("{}".format(final))
