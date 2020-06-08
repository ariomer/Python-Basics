# =============================================================================
# 16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
# =============================================================================


x = int(input('Please input a number : '))
if x < 17:
    print( 'Result : ', str(17-x))
else:
    print(str(abs(17-x)*2))
