import argparse
from exercise_2.src.Calculator import Calculator


def main():
    parser = argparse.ArgumentParser(description="Calculator CLI")
    parser.add_argument("a", type=int, help="first number")
    parser.add_argument("op", choices=["+", "-", "*", "/"], help="operation")
    parser.add_argument("b", type=int, help="second number")

    args = parser.parse_args()
    obj = Calculator(args.a, args.b)

    if args.op == "+":
        print(obj.add())
    elif args.op == "-":
        print(obj.subtract())
    elif args.op == "*":
        print(obj.multiply_whole_nums())
    elif args.op == "/":
        print(obj.divide())


if __name__ == "__main__":
    main()
