import db_handler
import pytest

def test_find_existing_post():
    db_handler.create_table()
    db_handler.insert_sample_data()

    post = db_handler.Post.find(1)
    assert post is not None
    assert isinstance(post, db_handler.Post)
    assert post.id == 1
    assert post.title == "Le Wagon"

def test_find_nonexistent_post():
    db_handler.create_table()
    db_handler.insert_sample_data()

    post = db_handler.Post.find(42)
    assert post is None

def test_find_with_sql_injection():
    db_handler.create_table()
    db_handler.insert_sample_data()

    id = "2' OR 1=1 --"
    post = db_handler.Post.find(id)
    assert post is None

def test_all_posts():
    db_handler.create_table()
    db_handler.insert_sample_data()

    posts = db_handler.Post.all()
    assert len(posts) == 5
    assert isinstance(posts, list)
    assert isinstance(posts[0], db_handler.Post)
    assert posts[0].title == "Le Wagon"
    assert posts[-1].title == "Stackoverflow"

if __name__ == "__main__":
    pytest.main(["test_post.py"])
