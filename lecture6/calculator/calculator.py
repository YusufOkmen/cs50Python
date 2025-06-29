def main():
    x = getInt()
    y = getInt()

    print(x + y)


def getInt():
    while True:
        try: 
            return int(input("Enter integer value: "))
        except ValueError:
            print("Not an Integer")
main()