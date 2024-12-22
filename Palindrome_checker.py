def its_palindrome(shit):
    shit = shit.replace(" ", "")
    return shit == shit[::-1]

user_input = input("Enter your phrase here: ")

if its_palindrome(user_input):
    print("It's palindrome!")
else:
    print("It's not palindrome")


