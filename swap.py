string_1 = input("Input the first string : ")
string_2 = input("Input the second string : ")

n = int(input())

new_string_1 = string_1.replace(string_1[:n], string_2[:n])
new_string_2 = string_2.replace(string_2[:n], string_1[:n])
print(new_string_1)
print(new_string_2)

