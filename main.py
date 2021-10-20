# some basic needs
ansTag = 'ans>> '
infoText = '''
1). Add
2). Subtract
3). Multiply
4). Divide1  (decimal)
5). Divide2  (quotient and remainder)
6). Multiplication Table  (multab)
7). LCM
8). HCF
0). exit
?). ---help for help
>>  '''

# functions for the operations
def sum():
    num1 = float(input('First Num >>  '))
    num2 = float(input('Second Num >>  '))
    ans = input(ansTag + str(num1+num2))

def sub():
    num1 = float(input('First Num >>  '))
    num2 = float(input('Second Num >>  '))
    ans = input(ansTag + str(num1-num2))

def mul():
    num1 = float(input('First Num >>  '))
    num2 = float(input('Second Num >>  '))
    ans = input(ansTag + str(num1*num2))

def div1():
    num1 = float(input('First Num >>  '))
    num2 = float(input('Second Num >>  '))
    if num2 == 0:
        input("Can't divide by 0")
    else:
        ans = input(ansTag + str(num1/num2))

def div2():
    num1 = float(input('First Num >>  '))
    num2 = float(input('Second Num >>  '))
    ans = input(ansTag + 'Quotient: ' + str(int(num1/num2)) + '\n' + ansTag + 'Remainder: ' + str(int(num1%num2)))

def mulTab():
    i = 1
    num = float(input('Number >>  '))
    print("Multiplication table for ==> ",int(num) )
    while(not i > 10):
        print('>>  ', int(num), ' * ' , i , ' = ', int(num)*i)
        i = i+1
    buffer = input()

def lcm():
    num1 = float(input('Num1 >>  '))
    num2 = float(input('Num2 >>  '))
    if num2<num1:
        num=int(num1)
    else:
        num=int(num2)
    
    while(True):
        if((num % int(num1) == 0) & (num % int(num2) == 0)):
            ans = input(ansTag + str(num))
            break
        else:
            num = num+1

def hcf():
    nums = input("> ").replace(" ", "")
    # print(nums)
    nums = nums.split(',')
    nums = list(map(int,nums))
    # print(nums)
    # nums = [3,24]
    arr = list()
    maxnum = list()

    for num in nums:
        for i in range(8):
            i += 1
            if num%i == 0:
                arr.append(i)
            else:
                continue
            #
        #
        # print(f"factor of {num} - {arr}")
    #
    # print(arr)
    for i in arr:
        if i in maxnum:
            continue
        elif arr.count(i) == len(nums):
            maxnum.append(i)
            continue
        else:
            continue
        #
    #

    ans = input(f"{ansTag} {max(maxnum)}")
    
    

# ----------------------------------------------------------------------------

def main():
    print('\n ******* Paculator *******')
    while(True):
        inputDATA = str(input(infoText)).upper().replace(' ', '')

# <----------------------------- DANGER  ---------------------------------->
        if (inputDATA == 'EXIT' or inputDATA == '0'):
            input(
f'''
{'*'*30}
Thanks For using Paculator!!!
{'*'*30}
''')
            break
        elif (inputDATA == '---HELP' or inputDATA == '?'):
            input(
'''
Nothing's Available Here for Now....
'''
            )
# <------------------------------------------------------------------------>


# conditons for the operations to be called

        elif(inputDATA == 'ADD' or inputDATA == '1' or inputDATA == '+'):
            sum()
        elif(inputDATA == 'SUBTRACT' or inputDATA == 'SUB' or inputDATA == '2' or inputDATA == '-' or inputDATA == '_'):
            sub()
        elif(inputDATA == 'MULTIPLY' or inputDATA == 'MUL' or inputDATA == '3' or inputDATA == '*'):
            mul()
        elif(inputDATA == 'DIVIDE' or inputDATA == 'DIVIDE1' or inputDATA == 'DIV' or inputDATA == 'DIV1' or inputDATA == '4' or inputDATA == '/'):
            div1()
        elif(inputDATA == 'DIVIDE1' or inputDATA == 'DIV1' or inputDATA == '5' or inputDATA == '!/' or inputDATA == '/1'):
            div2()
        elif(inputDATA == '6'or inputDATA == 'MULTAB' or inputDATA == 'MULTIPLICATIONTABLE' or inputDATA == 'TAB' or inputDATA == 'TABLE'):
            mulTab()
        elif(inputDATA == '7'or inputDATA == 'LCM'):
            lcm()
        elif(inputDATA == '8'or inputDATA == 'hcf'):
            hcf()
            
        
main()