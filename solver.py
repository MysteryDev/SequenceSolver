
"""
COPYRIGHT 2018 - SEQUENCE SOLVER BY MysteryDev!

Read the README.md for more information.
"""

""" Functions """
#The main algorithm to solve the equation
def Solve(seq,target):

    #These functions perform the calculations on the numbers given
    def add(x,y):
        return x + y
    def multiply(x,y):        
        return x*y
    def sub(x,y):
        #Only subtract if the first number is greater
        if x > y:
            return x - y
        else:
            return False
    def div(x,y):
        #Only divide if the result is an integer
        try:
            if (x/y).is_integer():
                return x/y
            else:
                return False
        except Exception:
            return False

    operators = [] #This stores all the operators used in the sub-calculations
    temp_operators = [] #This stores the temporary operators only used in a particular sub-calculation
    final_operators = [] #This stores the final operators for the equation

    current_nums = [seq[0]] #This stores all the sub-calcualtion numbers. It starts off with the first number in the sequence
    temp_current_nums = [] #This stores the temporary numbers only used in a particular sub-calculation
    final_calculations = [] #This is a 3d array storing all the sub-calculations which are 2d
    nums_index = 0 #Counts the index for which number will be calculated on from the sequence

    #Iterate over each number in the sequence
    for l in range(len(numbers)-1):
        #Iterate over each sub-calculation in the set of current numbers
        for calculation_data in current_nums:
            #Iterate 4 times for the 4 calculations (+,-,/,*)
            for i in range(4):
                #Add the numbers
                if i == 0:
                    #The first sub-calculation is the first number in the sequence.
                    #There will be a TypeError if accessing the 3rd index of the sub-calculation
                    #If the error occurs, the code will only assign the value of a to that first number
                    try:
                        a = calculation_data[3] #Number from sub-calculation being calculated on
                    except TypeError:
                        a = calculation_data
                    b = numbers[nums_index+1] #Number from sequnce being calculated on

                    result = add(a,b) #Result of the calculation
                    temp_current_nums.append([a,'+',b,result]) #Append both the numbers, the operator used and the result to the calculation array
                    temp_operators.append('+') #Append the operator used to the temporary operators array
                #Subtract the numbers
                elif i == 1:
                    try:
                        a = calculation_data[3]
                    except TypeError:
                        a = calculation_data
                    b = numbers[nums_index+1]
                    result = multiply(a,b)
                    temp_current_nums.append([a,'X',b,result])
                    temp_operators.append('X')
                #Divide the numbers
                elif i == 2:
                    try:
                        a = calculation_data[3]
                    except TypeError:
                        a = calculation_data
                    b = numbers[nums_index+1]
                    result = div(a,b)
                    if result != False:
                        temp_current_nums.append([a,'÷',b,result])
                        temp_operators.append('÷')
                #Divide the numbers
                elif i == 3:
                    try:
                        a = calculation_data[3]
                    except TypeError:
                        a = calculation_data
                    b = numbers[nums_index+1]
                    result = sub(a,b)
                    if result != False:
                        temp_current_nums.append([a,'-',b,result])
                        temp_operators.append('-')

        nums_index += 1 #Increment to the next index of the next number in the sequence

        #Transfer temporary current numbers to main current numbers array
        current_nums = []
        current_nums = temp_current_nums
        temp_current_nums = []
        final_calculations.append(current_nums)

        #Transfer temporary operators to main operators array
        operators = []
        operators = temp_operators
        temp_operators = []

    temp_target = target #The temporary target starts with the main target
    #Iterate backwards through the 3d array
    for i in range((len(final_calculations)-1),-1,-1):
        calculations = final_calculations[i] #Each calculation is each row in the 3d array

        #Iterate over each row in the calculation row
        for row in calculations:
            #The result of the calculation is equal to the target 
            if row[3] == temp_target:
                #print(row)
                final_operators.append(row[1]) #Append the operator used for that specific calculation
                temp_target = row[0] #Set the new temporary target to the first number in the previous calculation
                break

    #If it couldn't be solved, then the final operators will be empty
    if len(final_operators) > 0:
        return final_operators
    else:
        return False

""" Beginning of program """  
target = 11 #Number to find
numbers = [1,2,3,4,5] #Sequence of numbers in equation

isSolved = Solve(numbers,target) #Result of algorithm solving the equation

#If the equation is solved
if isSolved != False:
    final_operators = isSolved #The function returns an array of the correct operators

    #Display the question
    print("Here is the UNSOLVED equation:")
    for i in range(len(numbers)):
        if i < len(numbers)-1:
            print(numbers[i],end=" ? ")
        else:
            print(numbers[i],end=" = {}".format(target))
    print()
    #Display the equation with the operators in their correct position
    print("\nHere is the solved equation:")
    for i in range(len(numbers)):
        if i < len(numbers)-1:
            #Display the operators in reverse order as this is the final order the operators must be in
            print(numbers[i],end=" {} ".format(final_operators[len(final_operators)-(1+i)])) 
        else:
            print(numbers[i],end=" = {}".format(target))
else:
    #The equation couldn't be solved
    print("The equation to find the number {} can't be solved.".format(target))
    print("Please use another target number OR another equation sequence.")
 
