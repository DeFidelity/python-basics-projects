#Function with output

# def formmatName(f_name, l_name):
#     formatedL = l_name.title()
#     formatedF = f_name.title()
#     return f"{formatedF}  {formatedL}"
# l_name = input("pls input your first name. ")
# f_name  = input("pls input your last name. ")
# print(formmatName( f_name, l_name))

# for more than one return
   






   #exercise

def is_leap(year):
    """ use to check if a year is leap or not"""
    if year < 1
    retun 'INVALID YEAR'
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return  False
        else:
            return True
    else:
        return  False
def days_in_month(year, month):
    """ used in calculating and getting the number of days in a month"""
    if month > 12 or < 1:
        return "invalid month"

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap and month == 2:
        return 29
    return month_days[month -1]
  

  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# docstring ( function explainer ) which must come up immediately after : in front of the function.
def formmatName(f_name, l_name):
    """ Take the first and the last name and returns them in there title case form"""
    formatedL = l_name.title()
    formatedF = f_name.title()
    return f"{formatedF}  {formatedL}"
l_name = input("pls input your first name. ")
f_name  = input("pls input your last name. ")
print(formmatName( f_name, l_name))
