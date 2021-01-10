
def fib(x):
    nminus2 = 0
    nminus1 = 1
    terms = ['0', '1']
    for i in range(x-2):
        n = nminus1 + nminus2
        nminus2 = nminus1 
        nminus1 = n
        terms.append(str(n))
    return ','.join(terms)

print(fib(8))
print(fib(15))
print(fib(25))
