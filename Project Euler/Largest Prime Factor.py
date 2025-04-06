

def primeFactor():
    num = 600851475143
    i = 2
    factors = []
    while i * i <= num:
        if num % i == 0:
            factors.append(i)
            num = num// i
            i += 1
        else:
            i += 1
    if num > 1:
        factors.append(num)
    print(factors[-1])

def main():
    primeFactor()

if __name__ == '__main__':
    main()