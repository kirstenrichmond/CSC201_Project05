# Kirsten Richmond
#Program 01
#Project 1
#February 26, 2016

#asking user how many levels the half pyramid should have as integer
levels = int(input("How many levels should the half pyramid have?"))


#assigning simple, concise, variables to use 
height = levels


h = height


#asking the user for the character of the half pyramid

building_block = input("What character should we use for the half pyramid?")

bb = building_block #bb as for the character


#creating the half pyramid    

for i in range(h):
    print (bb * (i +1))
    
    

#Project 2

#asking user how many levels the full pyramid should have as integer
levels = int(input("How many levels should the full pyramid have?"))


#assigning simple, concise, variables to use 

height = levels

h = height

#asking the user for the character of the pyramid

building_block = input("What character should we use for the full pyramid?")

bb = building_block #bb as for the character

#creating the full pyramid

for i in range(h):
    print (" " *(h-i-1) + bb* (2*i+1))

#project 3
    #fixing the problem
    #allowing user to enter more than a single character as a "building block"
    


#drawing a parabola

#asking user for range of values for x                  
range = int(input("Enter a range of values of x")
