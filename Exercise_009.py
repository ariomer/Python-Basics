# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014
date = (11, 12, 2014)
print(str(date[0]) + '/' + str(date[1]) + '/' + str(date[2]))
print( "The examination will start from : %i / %i / %i"%date)