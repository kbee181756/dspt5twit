# web_app/routes/twitter_routes.py

from flask import Blueprint, render_template, jsonify
from web_app.model import db, User, Tweet, parse_records
from web_app.services.twitter_service import twitter_api
from web_app. services.basilica_service import basilica_api_client

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)
    api = twitter_api()
    user = api.get_user(screen_name)
    statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    
    db_user = User.query.get(user.id) or User(id=user.id)
    db_user.screen_name = user.screen_name
    db_user.name = user.name
    db_user.location = user.location
    db_user.followers_count = user.followers_count
    db.session.add(db_user)
    db.session.commit()

    # get existing user from the db or initilaize a new one: 

    return jsonify({"user": user._json, "tweets": [s._json for s in statuses]})