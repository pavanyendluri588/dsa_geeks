def palindrome_number_check(num):
    if str(num)== str(num)[::-1]:
        print(str(num)," is a palindrome number")
    else:
        print(str(num)," is not a palindrome number")
palindrome_number_check(6789012)
palindrome_number_check(3456543)

