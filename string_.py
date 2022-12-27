#counting the frequency of a character in a string
string = input("Input the string : ")
char = input("Input the character : ")
print(string.count(char))


#replacing a character with different character
char_2 = input("Character to be replaced : ")
char_3 = input("New character : ")
print(string.replace(char_2,char_3))


#removing the first occurance
char_4 = input("Input the character to delete its first occurence: ")
list_ = []
for char in string:
    list_.append(char)

list_.remove(char_4)
new_string = ""
for char in list_:
    new_string += char

print(new_string)

#to remove all occurences
char_5 = input("Input a character to remove its all occurances: ")
new_string_2 = ""
list_2 = []
for char in string:
    list_2.append(char)

n = string.count(char_5)
for i in range(n):
    list_2.remove(char_5)

for char in list_2:
    new_string_2 += char

print(new_string_2)





