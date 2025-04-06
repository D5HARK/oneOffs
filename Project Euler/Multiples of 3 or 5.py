
def multipleCheck():
    i = 1
    multiplelist = []
    while i < 1000:
        if i % 3 == 0 or i % 5 == 0:
            multiplelist.append(i)
            i = i + 1
        else:
            i = i + 1
    print(sum(multiplelist))
def main():
    multipleCheck()

if __name__ == '__main__':
    main()