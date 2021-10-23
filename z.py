scores = []
python_students = []
for _ in range(int(input())):
    Name = input()
    score = float(input()) 
    python_students+=[[Name,score]]
    if score not in scores:
    	scores.append(score) 
   #sorting scores

scores.sort()
second_minimum = scores[1]

# for loop to iterate and then compare scores with second minimum scores and 
#then printing the name of that student
sortedNames = []
for name,score in python_students:
	if score == second_minimum:
		sortedNames.append(name)
sortedNames.sort()
for Names in sortedNames:
	print(Names)