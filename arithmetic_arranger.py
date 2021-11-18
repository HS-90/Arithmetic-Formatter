def arithmetic_arranger(problems, t = False):
    #enter operator functions
    ops = {"+": lambda x,y: x+y, "-": lambda x,y: x-y}
    
    #check if list entered into function satisfies length requirements
    
    if len(problems) < 1:
        return ('Error: No problems entered.')
    
    if len(problems) > 5:
        return ('Error: Too many problems.')
    
    
    #set up empty strings to be added to before printing final version of problem + answer
    first_num =''
    second_num =''
    line =''
    answer =''
    
    for x in problems:
        
        if '+' in x:
            half = x.find('+')
        elif '-' in x:
            half = x.find('-')
        else:
            return ("Error: Operator must be '+' or '-'.")
    
        first_half = x[0:half].strip()
        operator = x[half]
        second_half = x[half+1:].strip()
        
        #check if numbers are digits
        if first_half.isnumeric() == False or second_half.isnumeric() == False:
            return ("Error: Numbers must only contain digits.")
        
        #check if numbers greater than 4 digits
        if len(first_half) > 4 or len(second_half) > 4:
            return("Error: Numbers cannot be more than four digits.")
        
        
        #this finds the solution to the problem using ops we defined earlier
        solution = ops[operator](int(first_half), int(second_half))
        
        #finds how long we want each string to print for each line
        larger_number = max(len(first_half), len(second_half))
        length = len(operator + (larger_number-len(second_half)+1)*" " + second_half)
        first_half = first_half.rjust(length) + 4*" "
        first_num += first_half
        second_half = (operator + (larger_number-len(second_half)+1)*" " + second_half).rjust(length) + 4*" "
        second_num += second_half
        solution = str(solution).rjust(length) + 4*" "
        answer += solution
        line +='-'*length + 4*" "
        
    #print the solution
    if t == True:
      return(f'{first_num[0:len(first_num)-4]}\n{second_num[0:len(second_num)-4]}\n{line[0:len(line)-4]}\n{answer[0:len(answer)-4]}')
        
    else:
      return(f'{first_num[0:len(first_num)-4]}\n{second_num[0:len(second_num)-4]}\n{line[0:len(line)-4]}')