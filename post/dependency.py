from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db, get_current_user
from user.models import User
from post.models import Post


def get_post_for_user(post_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> Post:
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not fount")
    if post.author_id != user.id:
        raise HTTPException(status_code=403, detail="You don't have permissions to modify this post")

    return post
