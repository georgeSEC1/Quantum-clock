from decimal import Decimal
while(True):
    n = input("Trips count: ")
    c = 299792458
    d = input("distance of wormhole:")
    t = int(d)/(c)
    x = ((int(n)*int(d))/(c*10000))
    print(Decimal(x-t),"time displacement in seconds")
    print()
    


