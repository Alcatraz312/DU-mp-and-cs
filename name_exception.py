name = input("Your name : ")
spec_list = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]","|",";",":","'",'"',",","<",".",">","/","?"]
num_list = ["1","2","3","4","5","6","7","8","9","0"]

exception = False

for x in spec_list:
    if x in name:
        exception = True

for x in num_list:
    if x in name:
        exception = True

if exception == True:
    print("EXCEPTION!!!")
else:
    print("OK")
    
        

