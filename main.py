# some basic needs
ansTag = 'ans>> '
infoText = '''
1). Add
2). Subtract
3). Multiply
4). Divide1  (decimal)
5). Divide2  (quotient and remainder)
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
    ans = input(ansTag + 'Quotient: ' + str(int(num1/num2)) + '\n' + ansTag + 'Remainder: ' + str(num1%num2))


def main():
    print('\n ******* Paculator *******')
    while(True):
        inputDATA = str(input(infoText)).upper().replace(' ', '')

# <----------------------------- DANGER  ---------------------------------->
        if (inputDATA == 'EXIT' or inputDATA == '0'):
            input(
'''
********************
Thanks For using Paculator!!!
********************
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
            
        
main()