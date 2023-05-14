import re

def arithmetic_arranger(problems, ansSwitch=False):
    arranged_problems = ""
    prob_json = []
    error=""
    line1=""
    line2=""
    line3=""
    line4=""
    if checkCount(problems) == False:
        error = "Error: Too many problems."
    for problem in problems:
        parts = re.split(' ', problem)
        #Check if valid
        if checkOperator(parts[1]) == False:
            error = "Error: Operator must be '+' or '-'."
        if checkLength(parts[0]) == False:
            error = "Error: Numbers cannot be more than four digits."
        if checkLength(parts[2]) == False:
            error = "Error: Numbers cannot be more than four digits."
        if checkDigits(parts[0])==False or checkDigits(parts[2])==False:
            error = "Error: Numbers must only contain digits."
        if error!="":
            return error
        else:
            #Calculate answer
            answer = calculate(parts)
            #Format each value...
            #Find maximum length of characters
            charLength = maxLength(parts)+2
            #Format each number with spaces and dashes
            test = whiteSpace(charLength, parts, answer)
            #Add each line and whitespace at the end
            line1 = line1+test["l1"]+"    "
            line2 = line2+test["l2"]+"    "
            line3 = line3+test["l3"]+"    "
            line4 = line4+test["l4"]+"    "
            prob_json.append({"num1": parts[0], "op": parts[1], "num2": parts[2], "ans": answer})
    #Strip final whitespace
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()
    line4 = line4.rstrip()
    if ansSwitch==True:
        arranged_problems = line1+"\n"+line2+"\n"+line3+"\n"+line4
    else:
        arranged_problems = line1+"\n"+line2+"\n"+line3
    
    return arranged_problems

def checkOperator(str):
    if str=="+" or str=="-":
        return True
    else:
        return False

def checkCount(prob):
    c = len(prob)
    if c>5:
        return False
    else:
        return True

def checkLength(str):
    if len(str)>4:
        return False
    else:
        return True

def checkDigits(str):
    ret = re.search('[^0-9]', str)
    if ret==None:
        return True
    else:
        return False
    
def calculate(calc):
    num1 = int(calc[0])
    num2 = int(calc[2])
    if calc[1]=="+":
        ans = num1+num2
    elif calc[1]=="-":
        ans = num1-num2
    return ans

def maxLength(calc):
    num1 = str(calc[0])
    num2 = str(calc[2])
    length=0
    if len(num1)>length:
        length=len(num1)
    if len(num2)>length:
        length=len(num2)
    return length

def whiteSpace(max, val, ans):
    st1 = str(val[0])
    st2 = str(val[2])
    ans = str(ans)
    ws1 = max - len(val[0])
    ws2 = max - len(val[2])
    ws3 = max - len(ans)
    #Sort first line
    i=0
    text1 = ""
    while i<ws1:
        text1 = text1+" "
        i=i+1
    text1 = text1+st1
    #Sort second line
    i=1
    text2 = val[1]
    while i<ws2:
        text2 = text2+" "
        i=i+1
    text2 = text2+st2
    #Sort break line
    i=0
    text3=""
    while i<max:
        text3=text3+"-"
        i=i+1
    #Sort answer line
    i=0
    text4=""
    while i<ws3:
        text4 = text4+" "
        i=i+1
    text4 = text4+ans
    retval = {"l1": text1, "l2": text2, "l3": text3, "l4": text4}
    return retval