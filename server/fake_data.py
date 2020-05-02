import sys
from application import db
from application.components.users.model import User
from application.components.lists.model import List
from application.components.posts.model import Post
from application.components.links.model import Link
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError


user1 = User(
    username = "amir",
    first_name = "amir hossein",
    last_name = "mazinani",
    gender = 1,
    email = "amir@email.com",
    password = generate_password_hash('pass', 'sha3_512', 128),
)
user2 = User(
    username = "asal",
    first_name = "asal",
    last_name = "hadadian",
    gender = 0,
    email = "asal@email.com",
    password = generate_password_hash('pass', 'sha3_512', 128),
)

if __name__ == "__main__":
    try:
        print('start')
        if sys.argv[-1] == 'delete':
            User.query.delete()
            List.query.delete()
            Post.query.delete()
            Link.query.delete()
            print('all rows deleted')
        elif sys.argv[-1] == 'create':
            db.session.add(user1)
            db.session.add(user2)
            print('created successfully')
        else:
            print('error: please add [delete] or [create] argument to run fake data module')
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print('error in add user')
    finally:
        db.session.close()
        print('end')