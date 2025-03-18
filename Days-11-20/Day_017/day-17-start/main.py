class User:
    def __init__(self, user_id="000", username="default_user"):   # this is a class constructor used to initialize an object with attributes.
        self.id = user_id
        self.username = username
        self.followers = 0   # Another way to add an attribute with default value and not required as a class argument.
        self.following = 0

    def follow(self, user):   # When a function is defined inside a Class, it is called a method.
        user.followers += 1
        self.following += 1


# user_1 = User()   # create an object for User class.
# user_1.id = "001"   # add an attribute for user_1 object.
# user_1.username = "Bob"

# print(user_1.username)


user_2 = User("002", "Jack")

print(user_2.username)
print(user_2.followers)

user_3 = User("003", "Andrew")
user_3.follow(user_2)
print(f"Following {user_3.following}, {user_2.username}")
