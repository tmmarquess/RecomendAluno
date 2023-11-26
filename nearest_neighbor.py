from func_euclidian import Euclidian


def NearestNeighbor(username, users):
    distances = []

    for user in users:
        if user != username:
            distance = Euclidian(users[user], users[username])
            distances.append((distance, user))

    distances.sort()
    return distances
