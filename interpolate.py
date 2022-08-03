import test_polymatrix_mult as poly
import numpy as np
import time


poly1 = input("Type your first polynomial, no spaces, and use ^ for power: ")
poly2 = input("Type your second polynomial, no spaces, and use ^ for power: ")


'''
Description: Turns the user input for the polynomial into a coefficient matrix
@poly_num: polynomial to convert
'''
def create_coef(poly_num):
    poly_num += " "
    temp = ""
    coef_pow_array = []     
    for i in range(0,len(poly1)):
        char_ascii = ord(poly_num[i])
        #If the char is a number or a subtraction sign, we
        #add the value to temp. 
        if((char_ascii > 47 and char_ascii < 58) or char_ascii == 45):
            temp += str(poly_num[i])
            
            if(i < len(poly_num) - 1):
                next_value = ord(poly_num[i+1])
                #Check if next character is also a number, if so, we add it
                #to temp. At the end, temp will be our full number
                if(not((next_value > 47) and next_value < 58)):
                    coef_pow_array.append(temp)
                    #make sure to erase temp for next full number
                    temp = ""
    coef_pow_len = len(coef_pow_array)
    return_array = np.zeros(int(coef_pow_len/2),dtype = int)

    tmp = 0
    #currently coef_pow_array contains every number in our polynomial string
    #we care only about the even indexed ones, because they contain
    #the coefficients (rather than the powers which we can figure out using
    #the dimension of our resulting polynomial
    for i in range(0,coef_pow_len):
        if(i % 2 == 0):
            return_array[tmp] = coef_pow_array[i]
            tmp += 1

    #returning the polynomial coefficient matrix
    return return_array

'''
Description: Take two polynomial coefficient matrices
             and return the resulting product coefficient matrix.
@poly1: First polynomial coefficient matrix
@poly2: Second polynomial coefficient matrix to multiply the first one 
'''
def coef_result(poly1,poly2):
    coef1 = create_coef(poly1) #create coefficient matrix 1 
    coef2 = create_coef(poly2) #create coefficient matrix 2

    coef1 = coef1.reshape(1,len(coef1))  #reshape into a proper numpy matrix
    coef2 = coef2.reshape(len(coef2),1)
    result = poly.no_thread_mult(coef2,coef1) #attain result using poly function
    
    return result
'''
Description: This is a purely aesthetic result outputter. We ignore
             0 coefficient x's and simply print out our result
@poly1: First polynomial
@poly2: Second polynomial

BUG NOTE: negative numbers will show up right next to addition symbols
'''
def user_output(poly1,poly2):
    values = coef_result(poly1,poly2)
    dimension = len(values) - 1
    result = ""
    for i in range(0,dimension):
        if(values[i] != 0):
            result += str(values[i])
            result += "x^"
            result += str(dimension-i)
            result += "+"
    #this is seperate because we don't want the plus sign at the end 
    result += str(values[dimension])
    result += "x^0"
    print(result)

user_output(poly1,poly2)
