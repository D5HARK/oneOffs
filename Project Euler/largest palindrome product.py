def palindrome():
    largest = 0
    for a in range(999, 99, -1):
        for b in range(999, 99, -1):
            n = a * b
            if str(n) == str(n)[::-1] and n > largest:
                largest = n
    print(largest)
def main():
    palindrome()

if __name__ == '__main__':
    main()