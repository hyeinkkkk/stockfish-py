from app import db


class SubCategory(db.Model):
    __tablename__ = 'subCategories'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer)
    name = db.Column(db.String, default="")
    description = db.Column(db.String, default="")


