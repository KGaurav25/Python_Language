post=input("Enter the post: ")

# if ("harry" in post or "Harry" in post):
#     print("The post is about Harry")
# else:
#     print("this is a normal post")


if ("harry".lower() in post.lower()): #converts both strings to lowercase and then compares
    print("The post is about Harry")
else:
    print("this is a normal post")