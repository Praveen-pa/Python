def deleteChar(string,char):
    newstr = "" 
    for ch in string:
        if ch != char:
            newstr+=ch
    return newstr
string = input("Enter a string: ")
char = (input("Enter a character: "))[0]
print(deleteChar(string,char)) 
