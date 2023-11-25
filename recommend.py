from nearest_neighbor import NearestNeighbor


def Recommend(username, users):
    nearest = NearestNeighbor(username, users)[0][1]
    recommendations = []

    neighborRatings = users[nearest]
    userRatings = users[username]

    for artist in neighborRatings:
        if artist not in userRatings:
            recommendations.append((artist, neighborRatings[artist]))

    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse=True)