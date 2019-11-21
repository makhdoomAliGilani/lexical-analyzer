Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@makhdoomAliGilani 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


1
00aqibjaved28/sc
 Code Issues 0 Pull requests 0 Actions Projects 0 Wiki Security Insights
sc/lexical.txt
@aqibjaved28 aqibjaved28 Add files via upload
e958b87 9 minutes ago
122 lines (108 sloc)  2.95 KB
  
import re

def identifier(user):
    rgx=r"^[a-zA-Z_]+(_)*[a-zA-Z0-9]*$"
    flg=re.match(rgx, user)
    if(flg):
        res="**It is Identifier**"
    else:
        res="NOT a Identifier."
    return res

def digit(user):
    rgx=r"^[0-9]+$"
    flg=re.match(rgx, user)
    if(flg):
        res="**It is Digit**"
    else:
        res="NOT a Digit."
    return res

def statement(user):
    rgx=r"^(int|float|string)\s+[a-zA-Z]+[0-9]*\s*(=|==|!=|<=|>=|<|>)\s*[a-zA-Z0-9]+;$"
    flg=re.match(rgx, user)
    if(flg):
        res="**It is Statement**"
    else:
        res="NOT a Statement."
    return res

def operator(user):
    rgx=r"(&&|\|\|)"
    flg=re.match(rgx, user)
    if(flg):
        res="**It is Operator**"
    else:
        res="NOT a Operator."
    return res

def dataType(user):
    rgx=r"int|double|float|String|boolean|char"
    flg=re.match(rgx, user)
    if(flg):
        res="**It is DataType**"
    else:
        res="NOT a DataType."
    return res

def forLoop(user):
    rgx=r"^for\s*\(\s*int\s*[a-zA-Z]+\s*=[0-9]+;\s*[a-zA-Z]+(<=|>=|<|>)[0-9]+;\s*[a-zA-Z++--]+\)$"
    flg=re.match(rgx, user)
    if(flg):
        res="**It is For Loop**"
    else:
        res="NOT a For Loop."
    return res

def foreachLoop(user):
    rgx=r"^for\s*\((int|char|string)\s*[a-zA-Z]+\s*(:)\s*[a-zA-Z]+\)$"
    flg=re.match(rgx, user)
    if(flg):
        res="**It is Foreach Loop**"
    else:
        res="NOT a Foreach Loop."
    return res

def whileLoop(user):
    rgx=r"^while\s*\([a-zA-Z]+(<=|>=|==|<|>|!=)*\s*[a-zA-Z0-9]*\)\{\s*\}$"
    flg=re.match(rgx, user)
    if(flg):
        res="**It is While Loop**"
    else:
        res="NOT a While Loop."
    return res

def doWhileLoop(user):
    rgx=r"^do\{\s*\}\s*while\s*\([a-zA-Z]+(<=|>=|==|<|>|!=)*\s*[a-zA-Z0-9]*\)$"
    flg=re.match(rgx, user)
    if(flg):
        res="**It is Do While Loop**"
    else:
        res="NOT a Do While Loop."
    return res

def ifStatement(user):
    rgx=r"^if\s*\([a-zA-Z]+(==|=|<=|>=|<|>)*[a-zA-Z0-9]*\s*(&&|\|\|)*\s*[a-zA-Z]*(==|=|<=|>=|<|>)*[a-zA-Z0-9]*\s*\)*$"
    flg=re.match(rgx, user)
    if(flg):
        res="**It is If Statement**"
    else:
        res="NOT a If Statement."
    return res

def result(user):
    print(identifier(user))
    print(digit(user))
    print(statement(user))
    print(operator(user))
    print(dataType(user))
    print(forLoop(user))
    print(foreachLoop(user))
    print(whileLoop(user))
    print(doWhileLoop(user))
    print(ifStatement(user))
    
        

x=1
print("***LEXICAL ANALYZER***")
print("......................")
while(x==1):
    user=input("Enter Input: ")
    print("......................")
    print("")
    result(user)
    print("............................")
    print("To enter another input press 1")
    print("Press any other digit to end")
    u=input("Enter Input: ")
    if(u==1):
        x=1
    else:
        x=2
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
