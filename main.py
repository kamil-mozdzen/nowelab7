import logging as lg

def odejmowanie(a, b):
    return float(a - b)

def mnożenie(a, b):
    return float(a * b)

def dzielenie(a, b):
    if b != 0:
        return a/b
    print("gosciu nie mozna tak przez 0")
    return None

def sredniaNumpajowa():
    lg.warning('uwaga')
