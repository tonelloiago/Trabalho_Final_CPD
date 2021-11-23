from quickSort import *

def queryUserRatings(table, userID):

    userRatings = table[userID]
    
    quick_sort(userRatings, len(userRatings))
    userRatings.reverse()

    return userRatings    





