from app import db
from app.common import create_or_update_query, make_plain_dict, make_plain_dict_list


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default="")
    description = db.Column(db.String, default="")

def get_all():
    return make_plain_dict_list(Category.query.filter().order_by(Category.id).all())

def get(category_id):
    return make_plain_dict(Category.query.filter(Category.id == category_id).first())


def get_id_by_game_name(name):
    category_c = Category.query.filter(Category.name == name).first()
    return category_c.id

