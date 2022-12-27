char = input()

string_list = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]

spec_list = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]","|",";",":","'",'"',",","<",".",">","/","?"]

num_dict = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}


if char in string_list:
    if char.isupper() == True:
        print("Upper case")
    else:
        print("Lower case")

if char in spec_list:
    print("The character is a special character")

if char in num_dict:
    for key in num_dict:
        if char == key:
            print(num_dict[char])



