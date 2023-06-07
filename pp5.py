# Practice problem 5------------------->>>>>>>> Palindromify the list
def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    n1 = int(input("Enter the number of elements you want to add: "))
    num_list = []
    for i in range(n1):
        ele = int(input(f"Enter the element no.{i+1} here: "))
        num_list.append(ele)
    print(f"You have entered {num_list}")

    print(f"After palindromifying the list ,"
          f" the output list will be "
          f":{[num_list[i] if num_list[i] < 10 else next_palindrome(num_list[i]) for i in range(n1)]}")
