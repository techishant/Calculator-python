ansTag = 'ans>> '

def main():
    while(True):
        inputDATA = str(input(
'''
1). Add
2). Subtract
3). Multiply
4). Divide1  (decimal)
5). Divide2  (quotient and remainder)
0). exit
?). ---help for help
>>  '''
        )).upper().replace(' ', '')

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


        elif(inputDATA == 'ADD' or inputDATA == '1' or inputDATA == '+'):
            num1 = int(input('First Num >>  '))
            num2 = int(input('Second Num >>  '))
            ans = input(ansTag + str(num1+num2))

        elif(inputDATA == 'SUBTRACT' or inputDATA == 'SUB' or inputDATA == '2' or inputDATA == '-' or inputDATA == '_'):
            num1 = int(input('First Num >>  '))
            num2 = int(input('Second Num >>  '))
            ans = input(ansTag + str(num1-num2))
            
        elif(inputDATA == 'MULTIPLY' or inputDATA == 'MUL' or inputDATA == '3' or inputDATA == '*'):
            num1 = int(input('First Num >>  '))
            num2 = int(input('Second Num >>  '))
            ans = input(ansTag + str(num1*num2))

        elif(inputDATA == 'DIVIDE' or inputDATA == 'DIVIDE1' or inputDATA == 'DIV' or inputDATA == 'DIV1' or inputDATA == '4' or inputDATA == '/'):
            num1 = int(input('First Num >>  '))
            num2 = int(input('Second Num >>  '))
            if num2 == 0:
                input("Can't divide by 0")
            else:
                ans = input(ansTag + str(num1/num2))

        elif(inputDATA == 'DIVIDE1' or inputDATA == 'DIV1' or inputDATA == '5' or inputDATA == '!/' or inputDATA == '/1'):
            num1 = int(input('First Num >>  '))
            num2 = int(input('Second Num >>  '))
            ans = input(ansTag + 'Quotient: ' + str(int(num1/num2)) + '\n' + ansTag + 'Remainder: ' + str(num1%num2))
            
        
main()