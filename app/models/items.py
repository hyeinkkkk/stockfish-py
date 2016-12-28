from app import db
from app.common import make_plain_dict, make_plain_dict_list


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    sub_category_id = db.Column(db.String, default=None)
    name = db.Column(db.String, default="")
    description = db.Column(db.String, default="")
    file_name = db.Column(db.String, default="")


def get(item_id):
    return make_plain_dict(Item.query.filter(Item.id == item_id).first())


def get_list_by_category(category_id):
    item_list = Item.query.filter(Item.category_id == category_id).all()
    return make_plain_dict_list(item_list)

