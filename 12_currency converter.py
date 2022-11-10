def main():
    print("This program convert the US dollars to Pounds sterling")
    print()

    dollars=eval(input("enter amount in dollars:"))
    pounds= convert_to_pounds(dollars)

    print("that is",pounds, "pounds.")


convert_to_pounds = lambda dollars: dollars * 0.82

main()