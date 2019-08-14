import math #not needed for this to work but I might add some code
#author Michael Lannon aka Evilous10101
print('welcome to this calculator')
print('what do you want to do')
#asks user what to do
ab=0
bb=0
cb=0
a=0
b=0
c=0
d=0
def calculaor():
    loop=True
    while loop is True:
        math=True
        loop3=True
        input1=input('Put in the first number:')
        input2=input('Put in second number:')
        #asks for numbers
        ab=input1
        bb=input2
        add= float(ab) + float(bb)
        subtract= float(ab) - float(bb)
        mult= float(ab) * float(bb)
        divide= float(ab) / float(bb)
        #Math equatons are put in
        print('Now what type of equation do you want to do')
        print('a for addition')
        print('b for subtraction')
        print('c for multiplation')
        print('d for division')
        #user is asked for what they want to do
        while math is True:
            input3=input('Choose one and only one:')
            #user chooses what they want to do
            if input3 == "a":
                print(add)
                math=False
            if input3 == "b":
                print(subtract)
                math=False
            if input3 == "c":
                print(mult)
                math=False
            if input3 == "d":
                print(divide)
                math=False
                #Each of these chooses a math equation.
            if (input3 != "a" and "b" and "c" and "d"):
                #User choose incorrectly so it restarts
                print('that was not a valid option. Please try again')
                input3=0
        print('Do you want to go again?')
        while loop3 is True:
            #User chooses if they want to use the calculator again
            question=input('Please but a Y or an N:')
            if question == "Y":
                print('(((here we go again)))')
                loop3=False
            if question == "N":
                loop=False
                loop3=False
            if question != "Y" and "N":
                print('please put in a real letter shown in the text')
                question=""
                #user choose incorrectly so it is looping back to ask again
        #User is shown the math and then the program exits
        print('Thank you for using this calculator')

calculaor()
