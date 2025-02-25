import random
from collections import Counter
from tabulate import tabulate

#Defining a generator function to generate random numbers
def random_number_generator(n):
    for _ in range(n):
        yield random.random() # generates a float number between 0 and 1

#mapping the random numbers to die faces
def get_die_face(x):
    if x < 1/6:
        return 1
    elif x < 2/6:
        return 2
    elif x < 3/6:
        return 3
    elif x < 4/6:
        return 4
    elif x < 5/6:
        return 5
    elif x < 6/6:
        return 6
    
#rolling the die 1000 times
die_rolls = [get_die_face(x) for x in random_number_generator(1000)]

#counting the frequency of each die face
face_counts = Counter(die_rolls)

#calculating the percentage of each die face
total_rolls = sum(face_counts.values()) #total number of rolls which is 1000
percentages = {face: count/total_rolls*100 for face, count in face_counts.items()}

#defining the table for results
table_data = [[face, face_counts[face], f"{percentages[face]:.1f}%"] for face in sorted(face_counts.keys())]
table_data.append(["Total", total_rolls, "100%"]) #adding the total row

#printing the table
print(tabulate(table_data, headers=["Face", "Frequency", "Percentage"], tablefmt="grid"))