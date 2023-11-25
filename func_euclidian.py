
def Euclidian(rating1, rating2):
    distance = 0
    commonRatings = False

    for key in rating1:
        if key in rating2:
            distance += pow(pow(abs(rating1[key] - rating2[key]), 2), 1/2)
            commonRatings = True

    if commonRatings:
        return distance
    else:
        return 0