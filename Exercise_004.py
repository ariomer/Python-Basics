# =============================================================================
# 4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
# =============================================================================

import math

pivalue = math.pi
def area():
    r = float(input('Please input a radius value :'))
    alan = r**2*pivalue
    print('Area : ' + str(alan))
    
area()
