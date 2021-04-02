from models import db, Article, Category


def create_tables():
    db.create_tables([Article, Category])
