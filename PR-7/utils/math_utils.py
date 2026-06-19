import math

def factorial(n):
    return math.factorial(n)

def compound_interest(p, r, t):
    return p * (1 + r/100) ** t

def trig_calculation(angle):
    rad = math.radians(angle)
    return {
        "sin": math.sin(rad),
        "cos": math.cos(rad),
        "tan": math.tan(rad)
    }

def area_circle(radius):
    return math.pi * radius * radius