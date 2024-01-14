from flask import current_app
from flask_dance import OAuth1ConsumerBlueprint
from flask_dance.consumer import oauth_authorized
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_login import current_user

from next import db
from next.auth.models import OAuth

trello_bp = OAuth1ConsumerBlueprint(
    "trello",
    __name__,
    base_url="https://trello.com",
    authorize_url="https://trello.com/1/OAuthAuthorizeToken",
    access_token_url="https://trello.com/1/OAuthGetAccessToken",
    consumer_key=current_app.config["TRELLO_KEY"],
    consumer_secret=current_app.config["TRELLO_SECRET"],
    request_token_url="https://trello.com/1/OAuthGetRequestToken",
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user),
)


@oauth_authorized.connect_via(trello_bp)
def trello_authorized(blueprint, token, **kwargs):
    if token is None:
        return False

    import pdb

    pdb.set_trace()
    return False
