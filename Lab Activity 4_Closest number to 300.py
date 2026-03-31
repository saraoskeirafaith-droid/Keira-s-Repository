x = 300

def find_closest():
    print(f"Find the closest number to {x}")

    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    c = int(input("Enter your third number: "))

    diff_a = abs(x - a)
    diff_b = abs(x - b)
    diff_c = abs(x - c)

    if a == b == c:
        print(f"A is {a}, B is {b}, and C with the value of {c} are all equal, therefore all numbers are closest to {x}")
    else:
        closest_diff = min(diff_a, diff_b, diff_c)
        
        if closest_diff == diff_a:
            print(f"Letter A or {a} is the closest number to {x}")
        elif closest_diff == diff_b:
            print(f"Letter B or {b} is the closest number to {x}")
        else:
            print(f"Letter C or {c} is the closest number to {x}")

find_closest()
