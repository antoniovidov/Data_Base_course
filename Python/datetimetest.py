import datetime

d=input("When is your B'day? (in YYYY-MM-DD) ") 
d=datetime.datetime.strptime(d,'%Y-%m-%d').date()  
print("Your B'day is : "+d.strftime('%Y-%m-%d'))