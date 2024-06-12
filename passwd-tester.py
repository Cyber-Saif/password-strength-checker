#python password strength checker                 
#january 13, 2022
import string
digt = list(string.digits)
lwr_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)
punc = list(string.punctuation)


def password_checker(string):
    strg = len(string)
    string = list(string)
    points = 0
    if strg<8:
        print(f'Your password only have {strg} characters which is not good')
    #this if statment is checking if paswword is grater than 7 or not if it is it will give a point
    if strg>7:
        points+=1
    #this stament will for to is password have capital, numbers and digits
    if string:
        for i in range(strg):
            if string[i] in upper_case:
                points+=1
                break
        else:
            print("!Capital letter missing")
            
        
        for j in range(strg):
            if string[j] in punc:
                points+=1
                break
        else:
            print("!No Punctuations found")


        for s in range(strg):
            if string[s] in digt:
                points+=1
                break
        else:
            print("!Digits missing")
    
    if points == 4:
        print(f'{points}\nGood password')
    else:
        print("password is not secure, use a different password")


def main():
    psd = input("type your password here: ")
    check = password_checker(psd)

main()
        
