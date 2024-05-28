class User:
    posts_dict = {}  # Define posts_dict as a class variable to store posts

    def __init__(self, username, email):
        if not username:
            raise ValueError("Username cannot be empty")
        if not email:
            raise ValueError("Email cannot be empty")
        self.username = username
        self.email = email
        self.posts = []  # List to store user's posts
        self.comments = []  # List to store user's comments
        self.likes = []  # List to store user's likes

    def create_post(self, content):
        if not content:
            raise ValueError("Post content cannot be empty")
        # Create a new Post instance with provided content and the current user as the author
        post = Post(content, self)
        self.posts.append(post)  # Add the post to the user's posts list
        return post

    def create_comment(self, post_id, content):
        if not content:
            raise ValueError("Comment content cannot be empty")
        post = User.posts_dict.get(post_id)  # Access the post using post_id from posts_dict
        if post:
            # Create a new Comment instance with provided content, the current user as the author, and the post
            comment = Comment(content, self, post)
            post.comments.append(comment)  # Add the comment to the post's comments list
            self.comments.append(comment)  # Add the comment to the user's comments list
            return comment
        else:
            print("Post not found!")
            return None

    def like_post(self, post_id):
        post = User.posts_dict.get(post_id)  # Access the post using post_id from posts_dict
        if post:
            # Create a new Like instance with the current user and the post
            like = Like(self, post)
            post.likes.append(like)  # Add the like to the post's likes list
            self.likes.append(like)  # Add the like to the user's likes list
            return like
        else:
            print("Post not found!")
            return None

class Post:
    def __init__(self, content, author):
        if not content:
            raise ValueError("Post content cannot be empty")
        self.content = content  # Content of the post
        self.author = author  # User who created the post
        self.comments = []  # List to store comments on the post
        self.likes = []  # List to store likes on the post

class Comment:
    def __init__(self, content, author, post):
        if not content:
            raise ValueError("Comment content cannot be empty")
        self.content = content  # Content of the comment
        self.author = author  # User who created the comment
        self.post = post  # Post on which the comment is made

class Like:
    def __init__(self, user, post):
        self.user = user  # User who liked the post
        self.post = post  # Post that was liked

def main():
    users = []  # List to store registered users
    post_id_counter = 1  # Initialize post ID counter

    while True:
        print("\n1. Register\n2. Create Post\n3. Comment\n4. Like\n5. Posts\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":  # Option for user registration
            username = input("Enter username: ")
            email = input("Enter email: ")
            if not username:
                print("Username cannot be empty")
                continue
            if not email:
                print("Email cannot be empty")
                continue
            if "@" not in email:
                print("Invalid email format. Email must contain '@'.")
                continue
            user = User(username, email)  # Create a new User instance
            users.append(user)  # Add the user to the list of registered users
            print("User registered successfully!")

        elif choice == "2":  # Option for creating a post
            if not users:
                print("No users registered yet!")
                continue
            username = input("Enter your username: ")
            user = next((u for u in users if u.username == username), None)
            if user:
                content = input("Enter post content: ")
                if not content:
                    print("Post content cannot be empty")
                    continue
                post = user.create_post(content)  # Create a new post for the user
                User.posts_dict[post_id_counter] = post  # Assign the post to a unique post ID
                post_id_counter += 1  # Increment post ID counter for the next post
                print("Post created successfully!")
            else:
                print("User not found!")

        elif choice == "3":  # Option for commenting on a post
            if not users:
                print("No users registered yet!")
                continue
            username = input("Enter your username: ")
            user = next((u for u in users if u.username == username), None)
            if user:
                post_id = int(input("Enter the ID of the post you want to comment on: "))
                content = input("Enter comment content: ")
                if not content:
                    print("Comment content cannot be empty")
                    continue
                user.create_comment(post_id, content)  # Create a new comment on the specified post
            else:
                print("User not found!")

        elif choice == "4":  # Option for liking a post
            if not users:
                print("No users registered yet!")
                continue
            username = input("Enter your username: ")
            user = next((u for u in users if u.username == username), None)
            if user:
                post_id = int(input("Enter the ID of the post you want to like: "))
                user.like_post(post_id)  # Like the specified post
            else:
                print("User not found!")

        elif choice == "5":  # Option for viewing posts
            if not any(user.posts for user in users):
                print("No posts yet")
            else:
                for user in users:
                    for idx, post in enumerate(user.posts, start=1):
                        print(f"{user.username}'s post {idx}: {post.content}")
                        if post.likes:
                            print(f"Likes: {len(post.likes)}")
                        if post.comments:
                            print("Comments:")
                            for comment in post.comments:
                                print(f"- {comment.content} by {comment.author.username}")
                    print()

        elif choice == "6":  # Option for exiting the program
            print("Exiting...")
            break

        else:  # Handle invalid choices
            print("Invalid choice!")

if __name__ == "__main__":
    main()
