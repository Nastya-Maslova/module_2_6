def result(number):
    string_of_number = ""
    for i in range(1, 20):
        for j in range(1, 20):
            if number % (i + j) == 0 and i != j:
                if i < j:
                    a = str(i)
                    b = str(j)
                else:
                    b = str(i)
                    a = str(j)
                if a + b not in string_of_number:
                    string_of_number += a + b
                continue
    return string_of_number


n = result(int(input()))
print(n)
