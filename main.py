import db_handler

if __name__ == "__main__":
    # Example usage of the find and all methods
    post = db_handler.Post.find(1)
    if post:
        print(f"Post ID: {post.id}, Title: {post.title}, Content: {post.content}")

    posts = db_handler.Post.all()
    for post in posts:
        print(f"Post ID: {post.id}, Title: {post.title}, Content: {post.content}")
