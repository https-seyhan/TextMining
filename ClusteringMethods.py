import pandas as pd
import math
from math import pow
from math import sqrt

#Cluster users by euclidian distance measure of their ratings
users = {"Angelica":{"Blues Traveller":3.5, "Broken Bells":2.0,
"Norah Jones":4.5, "Phonenix":5.0, "Slightly Stoopid":1.5,
"The Strookes":2.5, "Wampire Weekend":2.0},
"Bill":{"Blues Traveller":2.0, "Broken Bells":3.5, "Deadmau5":4.0, "Phonenix":2.0,
"Slightly Stoopid":3.5, "Wampire Weekend":3.0},
"Chan": {"Blues Traveller":5.0, "Broken Bells":1.0, "Deadmau5":1.0, "Norah Jones":3.0, "Phonenix":5, "Slightly Stoopid":1.0},
"Dan":{"Blues Traveller":3.0, "Broken Bells":4.0, "Deadmau5":4.5, "Phonenix":3.0,"Slightly Stoopid":4.5,
"The Strookes":4.0, "Wampire Weekend":4.5},
"Hailey":{"Broken Bells":4.0, "Deadmau5":1.0, "Norah Jones":4.0, "The Strookes":4.0, "Vampire Weekend":1.0},
"Jordyn" :{"Norah Jones":5.0, "Broken Bells":4.5, "Deadmau5":4.0, "Phonenix":5.0, "Slightly Stoopid":4.5, "The Strookes":4.0, 
"Wampire Weekend":4.0},
"Sam" :{"Slightly Stoopid":4.0, "Blues Traveller":5.0, "Broken Bells":2.0, "Norah Jones":3.0, "Phonenix":5.0,
"Slightly Stoopid":4.0, "The Strookes":5.0},
"Veronica":{"The Strookes":3.0, "Blues Traveller":3.0, "Norah Jones":5.0, "Phonenix":4.0, 
"Slightly Stoopid":2.5, "The Strookes":3.0 }}

def printpeople(user):
	print(user)

def euclidian(rating1, rating2):
	distance = 0
	total = 0
	for key in rating1:
		if key in rating2:
			distance = (rating1[key] - rating2[key])**2
			total += 1
	if total > 0:
		return math.sqrt(distance / total)
	else:
		return -1

def manhattan(rating1, rating2):
	distance = 0
	total = 0
	for key in rating1:
		if key in rating2 :
			distance +=abs(rating1[key] - rating2[key])
			total +=1
	if total > 0:
		return distance / total
	else:
		return -1 

def computeNearestNeigbour(username, users):
	distances = []
	
	for user in users:
		if user != username:
			#distance = manhattan(users[user], users[username])
			distance = euclidian(users[user], users[username])
			distances.append((distance, user))
	# sort based on distance --closest first
	distances.sort()
	print(distances)
	return distances

def recommend(username, users):
	#first find nearest neigbour
	nearest = computeNearestNeigbour(username, users)[0][1]
	print("Current User Ratings :", users[username])
	print(nearest)
	print("Neigbour Ratings :", users[nearest])
	recommendations = []
	#Now find bands neigbour rated that user did not
	neigbourRatings = users[nearest]
	userRatings = users[username]
	for artist in neigbourRatings:
		if not artist in userRatings:
			recommendations.append((artist, neigbourRatings[artist]))
	recommendations.sort(key = lambda artistTuple: artistTuple[1], reverse = True)
	print("Recommendation :", recommendations)
	return recommendations

def pearson(rating1, rating2):
	sum_xy = 0
	sum_x = 0
	sum_y = 0
	sum_x2 = 0
	sum_y2 = 0
	n = 0
	for key in rating1:
		if key in rating2:
			n += 1
			x = rating1[key]
			y = rating2[key]
			sum_xy = x*y
			sum_x += x
			sum_y += y
			print(sum_x - pow(sum_x,2)/n)
			sum_x2 = pow(x,2)
			sum_y2 = pow(y, 2)
	# now compute denominator
	denominator = sqrt(sum_x2 - (pow(sum_x, 2) / n)) * sqrt(sum_y2 - (pow(sum_y, 2) / n))
	if denominator == 0:
		return 0
	else:
		return(sum_xy - (sum_x*sum_y)/n) /denominator

if __name__ == '__main__':
	#printpeople(users['Hailey'])
	#printpeople(users['Veronica'])
	#print("Manhattan Distance is", manhattan(users['Hailey'], users['Veronica']))
	#print(computeNearestNeigbour('Hailey', users))
	#recommend('Hailey', users)
	#computeNearestNeigbour('Angelica', users)
	#recommend('Angelica', users)
	#recommend('Amy', users)
	#print("Euclidian Distance is :", euclidian(users['Hailey'], users['Veronica']) )
	print(pearson(users['Angelica'], users['Bill']))
