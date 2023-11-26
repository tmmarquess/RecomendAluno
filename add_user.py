def add_user(new_user_name, new_user_data, users_dict: dict):
    users_dict[new_user_name] = dict()

    for subject, score in new_user_data:
        users_dict[new_user_name].update({subject: score})
