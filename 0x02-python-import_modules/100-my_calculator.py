#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul
    
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b =int(sys.argv[3])
    if op == "+":
        result = add(a, b)
        op_str = "+"
    elif op == "-":
        result = sub(a, b)
        op_str = "-"
    elif op == "*":
        result = mul(a, b)
        op_str = "*"
    elif op == "/":
        result = div(a, b)
        op_str = "/"
    else:
        print("Unknown operator. Available operators: +, -, * and /\n")
        sys.exit(1)
    print("{} {} {} = {}\n".format(a, op_str, b, result))
    sys.exit(0)
