
ager = input("whats your age?: ")

def age_sub_two(input):
    agers = int(input)-2
    return agers

def age_div_two(input):
    agerss = float(input)/2
    return agerss



b = age_div_two(age_sub_two(ager))
    
print(age_sub_two(ager))
print(b)