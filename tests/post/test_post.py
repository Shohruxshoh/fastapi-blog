from post.models import Post
from user.models import User
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_post():
    post = Post(title="My first post", content="content")
    assert post.title == "My first post"
    assert post.content == "content"


def test_user_posts_relationship():
    user = User(username="user", email="user@gmail.com", hashed_password="password")
    post = Post(title="My first post", content="content", author_id=user.id)
    assert post.author_id == user.id

