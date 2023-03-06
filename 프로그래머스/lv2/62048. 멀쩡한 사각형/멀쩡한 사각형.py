def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b % a, a)

def solution(w,h):
    return (w * h) - (w + h - gcd(w, h))
