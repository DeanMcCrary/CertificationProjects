def number_pattern(n):
    full_list = []
    if not isinstance(n,int) or isinstance(n,bool):
        return "Argument must be an integer value."
    elif isinstance(n,int) and n > 0:
        for number in range(1, n + 1):
            full_list += [str(number)]
        return " ".join(full_list)
    elif isinstance(n,int) and n <= 0:
        return "Argument must be an integer greater than 0."

print(number_pattern(4))           # 1 2 3 4 
print(number_pattern(12))          # 1 2 3 4 5 6 7 8 9 10 11 12
print(number_pattern("beans"))     # Argument must be an integer value.
print(number_pattern(True))        # Argument must be an integer value.
print(number_pattern(0))           # Argument must be an integer greater than 0.
print(number_pattern(-3))          # Argument must be an integer greater than 0.
