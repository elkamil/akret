l="9"
m=0

try:
    lf=float(l)
    mf=float(m)
    d=lf/mf
    print(d)
except ValueError:
    print("Error")
except ZeroDivisionError:
    print("Dzielenie przez zero")
