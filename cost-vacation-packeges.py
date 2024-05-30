from clases.vacation import Vacation


def main():
    """this are the inputs"""
    dist = "Paris"
    num = 5
    dur = 10

    """this are the outputs"""
    calculator = Vacation(dist, num, dur)
    cost = calculator.sum()

    """this will do some printing"""
    if cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")


if __name__ == "__main__":
    main()
