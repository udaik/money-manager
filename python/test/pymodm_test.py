from pymodm import connect
from User import User as User
from Post import Post

connect("mongodb://localhost:27017/pymod-test", alias="my-app")
# User('User@email.com', 'Bob', 'Ross').save()
# User('User1@email.com', last_name='Ross', first_name='Bob').save()

usrs = []

for i in range(10001,1000000):
    #  print i
    email = "user1" + str(i) +  "@email.com"
    usrs.append( User(email, "u1", "l1"))

print len(usrs)
User.objects.bulk_create(usrs)

    # Users.append
    # User('User@email.com', 'Bob', 'Ross'),
    # User('anotherUser@email.com', 'David', 'Attenborough')
# User.objects.bulk_create(Users)

# some_author = "User@email.com"
# post = Post(author=some_author, content='This is the first post!').save()
