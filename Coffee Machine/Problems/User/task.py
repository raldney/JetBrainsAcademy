class User:
    users = []
    n_active = 0

    def __init__(self, active, user_name):
        if active:
            User.n_active += 1

        self.user_name = user_name
        self.active = active
        User.users.append(self)


    # create the class here
