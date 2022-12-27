def substr(string : str, substring : str):
    if substring not in string:
        return -1
    else:
        return string.index(substring)

string = input()
substring = input()

print(substr(string,substring))

