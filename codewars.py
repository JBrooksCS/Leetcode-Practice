"""
Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.

You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb) will be an integer m and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

Examples:
findNb(1071225) --> 45
findNb(91716553919377) --> -1
"""
def find_nb(m):
    
    if 1**3 == m:
        return 1
    else:
        n = 2
        v = 1
        #while we havent reached our given total volume
        while v < m:
            v = v + n ** 3
            if v == m:
                return n
            else:
                n = n + 1
                continue
        return -1
"""
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""
"""

def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]


"""
In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

You have to write a function printer_error which given a string will output the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ato z.

#Examples:

s="aaabbbbhaijjjm"
error_printer(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
error_printer(s) => "8/22"
"""

def printer_error(s):

    errorCount = 0

    # 97 (a) -> 109 (m)
    #Apparently range() excludes the top value, thus 110 is used
    r = range(97, 110)

    for l in s:
        if ord(l) not in r:
            errorCount = errorCount + 1
    return str(errorCount) + '/' + str(len(s))
            

"""
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
"""
def is_triangle(a, b, c):

    l = sorted([a , b, c])
    a,b,c = l[0],l[1],l[2]
    
    if a + b > c and a + c > b and b + c > a:
        return True
    else: 
        return False
    
"""
You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

Note
consecutive strings : follow one after another without an interruption
"""
def longest_consec(strarr, k):
    
#     print(strarr, k)
    i = 0
    longestCharCount = 0
    longestCombinedString = ""
    
    if k <= 0:
        return ""
    else:
        for i in range(len(strarr) - k + 1):
#             print("Round ", i)
            stringHolder = ""
            
            for j in range(k):
                stringHolder = stringHolder + strarr[i + j]
                
            if len(stringHolder) > longestCharCount:
                longestCombinedString = stringHolder
                longestCharCount = len(longestCombinedString)

#         print("Answer ", longestCombinedString)      
        return longestCombinedString

"""
Your objective is to complete a function createSpiral(N) that receives an integer N and returns an NxN two-dimensional array with numbers 1 through NxN represented as a clockwise spiral.

Return an empty array if N < 1 or N is not int / number

Examples:

N = 3 Output: [[1,2,3],[8,9,4],[7,6,5]]

1    2    3    
8    9    4    
7    6    5    
"""
def create_spiral(n):

    if(isinstance(n, int) != True):
        return []

    counter = 1
    print(n)

    #build the grid
    rows, cols = (n, n) 
    arr = [[0 for i in range(cols)] for j in range(rows)] 
    
    startRow = 0
    endRow = n-1
    startCol = 0
    endCol = n-1
    
    while counter <= n*n:
        ######RIGHT
        for i in range (startCol, endCol + 1):
            arr[startRow][i] = counter
            counter += 1
        startRow += 1
        
        ######DOWN
        for i in range(startRow, endRow + 1):
            arr[i][endCol] = counter
            counter += 1
        endCol -= 1
        
        ######LEFT
        for i in range(endCol, startCol - 1, -1):
            arr[endRow][i] = counter
            counter += 1
        endRow -= 1
        
        ######UP
        for i in range (endRow, startRow - 1, -1):
            arr[i][startCol] = counter
            counter += 1
        startCol += 1
    
    return arr

"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

Test.assert_equals(make_readable(0), "00:00:00")
Test.assert_equals(make_readable(5), "00:00:05")
Test.assert_equals(make_readable(60), "00:01:00")
Test.assert_equals(make_readable(86399), "23:59:59")
Test.assert_equals(make_readable(359999), "99:59:59")
"""

def make_readable(seconds):
    # Do something
    minutes = (seconds // 60) % 60
    hours = (seconds // (60*60)) 
    seconds = seconds - (hours * 60 * 60) - (minutes * 60)
    
    # print("HOURS - ", hours)
    # print("MINUTES - ", minutes)
    # print("MINUTES - ", seconds)
    # print((str(f'{hours:02n}') + ":" + str(f'{minutes:02n}') + ":" + str(f'{seconds:02n}')))
    
    return ((str(f'{hours:02n}') + ":" + str(f'{minutes:02n}') + ":" + str(f'{seconds:02n}')))

"""
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""
def validBraces(string):
  
  closingStack = []

  for c in string:
      #                 PARENS
      if c == "(":
          closingStack.insert(0, ")")
          
      elif c == ")":
          if len(closingStack) == 0:
              return False
              
          elif closingStack[0] == ")":
              closingStack.pop(0)
          else:
              return False
      #                 BRACKETS
      elif c == "[":
          closingStack.insert(0, "]")
          
      elif c == "]":
          if len(closingStack) == 0:
                  return False
          elif closingStack[0] == "]":
              closingStack.pop(0)
          else:
              return False
      #                 BRACES
      elif c == "{":
          closingStack.insert(0, "}")
          
      elif c == "}":
          if len(closingStack) == 0:
              return False
          elif closingStack[0] == "}":
              closingStack.pop(0)
          else:
              return False
  if len(closingStack) == 0 :
      return True
  else :
      return False
      
      
