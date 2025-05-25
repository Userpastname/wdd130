import math

starting = input("what was the starting odometer value?: ")
ending = input("what was the ending odometer value?:" )
fuel = input("what was the fuel in gallons?: ")

starting = float(starting)
ending = float(ending)
fuel = float(fuel)

def mpg(start,end,feul):
    answer = (float(end)-float(start))/float(feul)
    return answer

def lp_hund_k():
    answer = 235.215/float(mpg(starting,ending,fuel))
    return answer

print(str(mpg(starting,ending,fuel)))
print(str(lp_hund_k()))
