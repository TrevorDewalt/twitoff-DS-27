"""SQLAlchemy models and utility functions for Twitoff applciation"""

from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()


class User(DB.Model):
    """Twitter User Table that will correspond to tweets - SQLAlchemy syntax"""
    id = DB.Column(DB.BigInteger, primary_key=True)  # id column
    name = DB.Column(DB.String, nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return "<User: {}>".format(self.name)

# creates Tweet Table
# similar


class Tweet(DB.Model):
    """Tweet text and data"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    vect = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'))
    user = DB.relationship("User", backref=DB.backref('tweets', lazy=True))


def __repr__(self):
    return f"<Tweet: {self.text}>"
