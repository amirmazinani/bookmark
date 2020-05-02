import sys
import random
from application import db
from application.components.users.model import User
from application.components.lists.model import List
from application.components.posts.model import Post
from application.components.links.model import Link
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import func, select


def create_user():
    user1 = User(
        username="amir",
        first_name="amir hossein",
        last_name="mazinani",
        gender=1,
        email="amir@email.com",
        password=generate_password_hash("pass", "sha3_512", 128),
    )
    user2 = User(
        username="asal",
        first_name="asal",
        last_name="hadadian",
        gender=0,
        email="asal@email.com",
        password=generate_password_hash("pass", "sha3_512", 128),
    )
    db.session.add(user1)
    db.session.add(user2)


def create_link():
    link1 = Link(
        title="website",
        link="https://amirmazinani.ir",
        user_id=random.choice(User.query.all()).user_id
    )
    link2 = Link(
        title="company",
        link="https://lemoni.ir",
        user_id=random.choice(User.query.all()).user_id
    )
    link3 = Link(
        title="telegram",
        link="https://t.me/amirmazinani_ir",
        user_id=random.choice(User.query.all()).user_id
    )
    db.session.add(link1)
    db.session.add(link2)
    db.session.add(link3)


def create_list():
    list1 = List(
        title="ui tips",
        description="design and art of user interface",
        user_id=random.choice(User.query.all()).user_id
    )
    list2 = List(
        title="web learning",
        description="learning web programming in frontend and backend",
        user_id=random.choice(User.query.all()).user_id
    )
    list3 = List(
        title="python best practices",
        description="scripting python for automating works",
        user_id=random.choice(User.query.all()).user_id
    )
    list4 = List(
        title="blockchain",
        description="this is a p2p service for all of people",
        user_id=random.choice(User.query.all()).user_id
    )
    db.session.add(list1)
    db.session.add(list2)
    db.session.add(list3)
    db.session.add(list4)


def create_post():
    post1 = Post(
        title="trello",
        link="https://trello.com",
        description="team management and task management program",
        user_id=random.choice(User.query.all()).user_id,
        list_id=random.choice(List.query.all()).list_id
    )
    post2 = Post(
        title="taskulu",
        link="https://trello.com",
        description="internal team management app",
        user_id=random.choice(User.query.all()).user_id,
        list_id=random.choice(List.query.all()).list_id
    )
    post3 = Post(
        title="instagram",
        link="https://instagram.com",
        description="an app for sharing images and videos",
        user_id=random.choice(User.query.all()).user_id,
        list_id=random.choice(List.query.all()).list_id
    )
    post4 = Post(
        title="youtube",
        link="https://youtube.com",
        description="best service for lean any thing",
        user_id=random.choice(User.query.all()).user_id,
        list_id=random.choice(List.query.all()).list_id
    )
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)


if __name__ == "__main__":
    try:
        if sys.argv[-1] == "delete":
            Link.query.delete()
            Post.query.delete()
            List.query.delete()
            User.query.delete()
        elif sys.argv[-1] == "create":
            create_user()
            create_link()
            create_list()
            create_post()
        else:
            print(
                "error: please add [delete] or [create] argument to run fake data module")
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()
