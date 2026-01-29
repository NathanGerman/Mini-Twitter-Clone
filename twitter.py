users = {}
posts = []
post_id = 1

def create_user():
    username = input("username: ")
    bio = input("bio: ")
    if username in users:
        print("That username already exists.")
        return
    users[username] = {"bio": bio, "followers": 0}
    print("User created:", username)

def write_post():
    global post_id
    user = input("Who is posting: ")
    if user not in users:
        print("That user does not exist.")
        return
    text = input("What do you want to say: ")
    post = {"id": post_id, "user": user, "text": text, "likes": 0}
    posts.append(post)
    post_id += 1
    print("Post created.")

def view_feed():
    for post in posts:
        print("ID:", post["id"])
        print("User:", post["user"])
        print("Text:", post["text"])
        print("Likes:", post["likes"])
        print()

def like_post():
    post_number = input("Enter post ID to like: ")
    post_number = int(post_number)
    for post in posts:
        if post["id"] == post_number:
            post["likes"] += 1
            print("Post liked.")
            return
    print("Post not found.")

def menu():
    while True:
        print("1. Create a user")
        print("2. Write a post")
        print("3. View the feed")
        print("4. Like a post")
        print("5. Exit")

        choice = input("Choose a number: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            write_post()
        elif choice == "3":
            view_feed()
        elif choice == "4":
            like_post()
        elif choice == "5":
            break
        else:
            print("Not a valid choice.")

menu()
