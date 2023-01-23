def mortgage(rate, borrowed, years):
    r = rate / 100 / 12
    n = years * 12
    return((r*borrowed)/(1-(1+r)**-n))

print (mortgage(5,200000,30))