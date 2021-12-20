## How to sort a list of dicts based on formula:
## [review score/distance from variable 'point_coord']

import math

dict_list = [{'name': 'business 1', 'latitude': 49.5, 'longitude':-74.2, 'reviewscore': 3.5}, 
             {'name': 'business 2', 'latitude': 49.1, 'longitude':-74.29, 'reviewscore': 4.5}, 
             {'name': 'business 3', 'latitude': 49.3, 'longitude':-74.13, 'reviewscore': 4}, 
             {'name': 'business 4', 'latitude': 49.5, 'longitude':-74.19},
             {'name': 'business 5', 'latitude': 50.3, 'longitude':-74.13, 'reviewscore': 4}, 
             {'name': 'business 6', 'latitude': 49.3, 'longitude':-74.13, 'reviewscore': 3}, 
             {'name': 'business 7', 'latitude': 59.3, 'longitude':-74.13, 'reviewscore': 4.8}, 
             {'name': 'business 8', 'latitude': 48.3, 'longitude':-74.13, 'reviewscore': 3.6}, 
             {'name': 'business 9', 'latitude': 49.3, 'longitude':-74.13, 'reviewscore': 4.1}, 
             {'name': 'business 10', 'latitude': 49.0, 'longitude':-74.12}]

point_coord = (49.5, -74.2) ## should work for any point coordinate

## separate point_coord tuple to get x and y values (for distance formula)
x1=point_coord[0]
y1=point_coord[1]

## create temp lists to store latitude and longitude
lats=[]
longs=[]
revScores=[]
distances=[]
totalScores=[]


def ranker(point_coord,dict_list):

    for index in range(len(dict_list)): 
        for key in dict_list[index]:
            ## take latitudes/longitudes from list of dicts and append to lists
            if key=='latitude':
                lats.append(dict_list[index][key])
            elif key=='longitude':
                longs.append(dict_list[index][key])
                
            ## append reviewscore to list.
            ## If no reviewscore exists in a dict, make reviewscore = 0 as the default value.
            elif key=='reviewscore':
                revScores.append(dict_list[index][key])
            elif 'reviewscore' not in dict_list[index]:
                revScores.append(0)

    for i in range(len(lats)):
        ## compute distance using distance formula √(x2-x1)^2 + (y2-y1)^2
        distance_from_point_coordinate=math.sqrt((lats[i]-x1)**2+(longs[i]-y1)**2)
        distances.append(distance_from_point_coordinate)

    ## generate sorting for dicts by doing: reviewscore/distance from point coordinate
    for j in range(len(revScores)):
        if distances[j]==0:
            totalScores.append(0)
        else:
            totalScores.append(revScores[j]/distances[j])

    ## determine the order of the scores
    maxIndex=0
    count=0
    indexList=[]
    
    while count<len(totalScores):
    ## sort by min or max - comment out other 4 lines
        
##        minIndex=totalScores.index(min(totalScores))
##        indexList.append(minIndex)
##        totalScores[minIndex]=1000
##        count+=1
        
        maxIndex=totalScores.index(max(totalScores))
        indexList.append(maxIndex)
        totalScores[maxIndex]=-1
        count+=1

    sorted_dict_list=[]

    ## create the new sorted dictionary
    sorted_dict_list=[]
    for z in range(len(dict_list)):
        sorted_index=indexList[z]
        sorted_dict_list.append(dict_list[sorted_index])
        
    return sorted_dict_list

sorted_list = ranker(point_coord, dict_list)
print(sorted_list)
