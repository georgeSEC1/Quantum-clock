from decimal import Decimal
while(True):
    n = input("Trips count: ")
    c = 299792458
    d = input("distance of wormhole:")
    t = ((int(n)*int(d))/(c))
    print(Decimal(t),"time displacement in seconds")
    print()