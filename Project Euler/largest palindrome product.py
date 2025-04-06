def palindrome():
    for a in range(999, 99, -1):
        for b in range(999, 99, -1):
            n = a * b
            if str(n) == str(n)[::-1]:
                print(n)
                return
def main():
    palindrome()

if __name__ == '__main__':
    main()