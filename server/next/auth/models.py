from flask_dance.consumer.storage.sqla import OAuthConsumerMixin
from flask_security import UserMixin, RoleMixin, Security
from flask_security.datastore import SQLAlchemyDatastore

from next import db

roles_users = db.Table(
    "roles_users",
    db.Column(
        "user_id",
        db.Integer,
        db.ForeignKey("user.id"),
    ),
    db.Column("role_id", db.Integer, db.ForeignKey("role.id")),
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class Profile(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    email = db.Column(db.String())


class OAuth(OAuthConsumerMixin, db.Model):
    provider_user_id = db.Column(db.String, unique=True, nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey(Profile.id), nullable=False)
    profile = db.relationship("Profile")


user_datastore = SQLAlchemyDatastore(db, Profile, Role)
security = Security(datastore=user_datastore)
