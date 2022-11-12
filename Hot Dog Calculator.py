hot_dog_pk = 10
buns_pk = 8

print(
    """
    **********************
      HOT DOG CALCULATOR    
    **********************
    """
)
#declaring Variables
adults = (int(input("Enter number of adults \n")))
HD_adults= (int(input("How many hot dogs for each adults?. \n")))
children = (int(input("Enter number of children \n")))
HD_children= (int(input("How many hot dogs for each child?. \n")))

#how many hot dogs needs based on the people
HotDogs_needed = adults * HD_adults + children * HD_children

# calculate material needed
HD_PK = HotDogs_needed / hot_dog_pk
BUN_PK = HotDogs_needed / buns_pk

import math

#calculate material used
HD_PKused = math.ceil(HD_PK) * hot_dog_pk
BUN_PKused =math.ceil(BUN_PK) * buns_pk

#to verify
# print (HD_PKused)
# print (BUN_PKused)
# print(HotDogs_needed)

print("\nFor the Cookout you need:")
print(math.ceil(HD_PK) ,"packages of hot dogs")
print (math.ceil(BUN_PK), "packages of Hot dog Buns\n")
print ("left over:")
print(HD_PKused - HotDogs_needed , "hot dogs")
print(BUN_PKused - HotDogs_needed, "hot dog buns")