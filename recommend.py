from nearest_neighbor import NearestNeighbor


def Recommend(username, users):
    nearest = NearestNeighbor(username, users)[0][1]
    print(nearest)
    recommendations = []

    neighborRatings = users[nearest]
    userRatings = users[username]

    for subject in neighborRatings:
        if subject not in userRatings:
            recommendations.append((subject, neighborRatings[subject]))

    return sorted(
        recommendations, key=lambda subjectTuple: subjectTuple[1], reverse=True
    )
