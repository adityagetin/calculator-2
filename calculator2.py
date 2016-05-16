import operator
op_dict = {"+" : operator.add,
           "-" : operator.sub,
           "*" : operator.mul,
           "/" : operator.floordiv}


status = "running"
while status == "running":
    x = input("Enter a number (or a letter to exit): ")
    if x.isdigit():
        op_input = input("Enter an operator: ")
        op_exec = op_dict[op_input]
        y = input("Enter another number: ")
        result = op_exec(eval(x), eval(y))
        print("Result:")
        print(result)
        print("\n")
    else:
        status == "finished"
        break
