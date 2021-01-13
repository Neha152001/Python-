#defining the function
def char(n):
    return ord(n)

ch=str(input("Enter a character :"))

#calling the function
print('The ASCII value of',ch[0],'is',char(ch[0]))