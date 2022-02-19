#
# Name: Cristofer Jimenez
# Collaborator(s): N/A
#
s= input("How many seconds : ")
s= int(s)
days= s//86400
hours=(s%86400)//3600

minutes= (((s%86400))%3600)//60
seconds= (((s%86400))%3600)%60
print(f"That is {days} days, {hours} hours, {minutes} minutes and {seconds} seconds")


