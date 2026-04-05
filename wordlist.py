word_list=["Deepak","apple","cricket","random","book","peckock"]

def is_leap_year(year):
    '''This is a leap year function '''
    # Write your code here. 
    # Don't change the function name.
    if year%4==0 and year%100==0 and year%400==0:
        return True
    else:
        return False
        
print(is_leap_year(1989))

