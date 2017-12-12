import os
import httplib2
import json
import datetime
import random
import string
import requests
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for
from flask import flash, jsonify, make_response, g
from flask import session as login_session
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_create import Base, Category, Item, User
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError


app = Flask(__name__)


# Connect to database.
engine = create_engine('sqlite:///filmgenrecatalog.db')
Base.metadata.bind = engine

# Create database session.
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Authentication
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Film Catalog App"


@app.route('/login')
def showLogin():
    """ 

    Creates a state token to prevent request forgery. Stores it in the 
    session for later validation. 
    """
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    """ Facebook authentication.

    Gathers data from Fcebook Sign In API and places it inside a session 
    variable.
    """
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data

    # Exchange client token for long-lived server-side token.
    app_id = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = ('https://graph.facebook.com/v2.10/oauth/access_token?grant_type='
           'fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token'
           '=%s') % (app_id, app_secret, access_token)
    http = httplib2.Http()
    result = http.request(url, 'GET')[1]
    data = json.loads(result)

    # Extract the access token from response.
    token = 'access_token=' + data['access_token']

    # Use token to get user info from API.
    url = 'https://graph.facebook.com/v2.10/me?%s&fields=name,id,email' % token
    http = httplib2.Http()
    result = http.request(url, 'GET')[1]
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to proplerly
    # logout, let's strip out the information before the equals sign in
    # our token.
    stored_token = token.split("=")[1]
    login_session['access_token'] = stored_token

    # Get user picture.
    url = ('https://graph.facebook.com/v2.10/me/picture?%s&redirect=0'
           '&height=200&width=200') % token
    http = httplib2.Http()
    result = http.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # Check if the user exists in the database. If not create a new user.
    user_id = getUserID(login_session['email'])
    if user_id is None:
        user_id = create_user()
        login_session['user_id'] = user_id

    output = ''
    output += '<h4>Welcome, '
    output += login_session['username']
    output += '!</h4>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style="width: 200px; height: 200px;"> '
    flash("You are now logged in as %s" % login_session['username'])
    return output


@app.route('/fbdisconnect')
def fbdisconnect():
    """Logout via Facebook OAuth."""
    facebook_id = login_session['facebook_id']

    # The access token must be included to successfully logout.
    access_token = login_session['access_token']
    url = ('https://graph.facebook.com/%s/permissions?'
           'access_token=%s') % (facebook_id, access_token)
    http = httplib2.Http()
    result = http.request(url, 'DELETE')[1]

    if result == '{"success":true}':
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/gconnect', methods=['POST'])
def gconnect():
    """Gmail authentication.

    Gathers data from Google Sign In API and places it inside a session variable.
    """
    # Validate state token.
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain aurorization code.
    code = request.data

    try:
        # Updgrade the authorization code into a credentials object.
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check to see if user is already logged in.
    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info from API.
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['provider'] = 'google'
    login_session['username'] = data["name"]
    login_session['picture'] = data["picture"]
    login_session['email'] = data["email"]

    # See if user exists, if he/she doesn't make a new one.
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h4>Welcome, '
    output += login_session['username']
    output += '!</h4>'
    output += '<img src="'
    output += login_session['picture']
    output += ' "style = "width: 200px; height: 200px;"> '
    flash("You are now logged in as %s" % login_session['username'])
    return output


def createUser(login_session):
    """User helper functions.

    These functions serve as local permission system.
    """
    newUser = User(
        name=login_session['username'],
        email=login_session['email'],
        image=login_session['picture'])

    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()

    return newUser.id


def getUserInfo(user_id):
    """Returns the user_id from the session."""
    user = session.query(User).filter_by(id=user_id).one()
    return user.id


def getUserID(email):
    """Filters the user by their e-mail."""
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


@app.route('/gdisconnect')
def gdisconnect():
    """Revokes a current user's Google+ token and reset their login session."""
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(json.dumps('Current user not'
                                            'connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s'\
        % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        # reset the user's session.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Succesfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return redirect(url_for('default'))
    else:
        # For whatever reason the given token was invalid.
        response = make_response(json.dumps('Failed to revoke'
                                            'token for given user'), 400)
        response.headers['Content-Type'] = 'application/json'
        return redirect(url_for('default'))


@app.route('/disconnect')
def disconnect():
    """Revokes a current user's tokens and logs them out."""
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
            del login_session['username']
            del login_session['email']
            del login_session['picture']
            del login_session['user_id']
            del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('default'))
    else:
        flash("You were not logged in to begin with!")
        return redirect(url_for('default'))


@app.route('/json')
@app.route('/category/JSON')
def allcategoriesJSON():
    """Makes an API endpoint for the database."""
    categories = session.query(Category).all()
    catalog = []
    for c in categories:
        catalog.append(c.serialize)
        items = session.query(Item).filter_by(category_id=c.id).all()
        catalog[-1]['Items'] = [i.serialize for i in items]
    return jsonify(Categories=catalog)


# Adding primary routes.
def login_required(f):
    """Login decorater function."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            flash('Please log in to manage items.')
            return redirect('/default')
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
@app.route("/category/")
def default():
    """Default page route."""
    categories = session.query(Category).order_by(asc(Category.id))
    latest = session.query(Item).order_by(Item.created_at.desc()). \
        limit(8).all()
    return render_template('index.html', categories=categories, latest=latest)


@app.route('/category/<int:category_id>/')
def filmGenre(category_id):
    """Category page route."""
    category = session.query(Category).filter_by(id=category_id).one()
    categories = session.query(Category).order_by(asc(Category.id))
    items = session.query(Item).filter_by(category_id=category.id)
    return render_template(
        'categories.html', category=category, items=items,
        categories=categories)


@app.route("/category/<int:category_id>/<int:item_id>")
def showItem(category_id, item_id):
    """Show item route."""
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('showItem.html', item=item, category=category)


@app.route('/category/<int:category_id>/new/', methods=['GET', 'POST'])
@login_required
def newFilmItem(category_id):
    """Route for creating a new Film item."""
    if request.method == 'POST':
        newItem = Item(
            name=request.form['name'],
            description=request.form['description'],
            created_at=datetime.datetime.now(),
            category_id=category_id,
            user_id=login_session['user_id'])

        session.add(newItem)
        session.commit()
        flash("New film succesfully added!")
        return redirect(url_for(
            'showItem', category_id=category_id, item_id=newItem.id))
    else:
        categories = session.query(Category).all()
        return render_template('newfilmitem.html', categories=categories)


@app.route('/category/<int:category_id>/'
           '<int:item_id>/edit/', methods=['GET', 'POST'])
@login_required
def editFilmItem(category_id, item_id):
    """Route for editig a Film item."""

    editedItem = session.query(Item).filter_by(id=item_id).one()
    creator = getUserInfo(editedItem.user_id)

    if editedItem.user_id != creator:
        return redirect(
            'showItem', category_id=category.id, item_id=editedItem.id)
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        session.add(editedItem)
        session.commit()
        flash("Film edited succesfully!")
        return redirect(url_for(
            'showItem', category_id=category_id, item_id=editedItem.id))
    else:
        return render_template(
            'editfilmitem.html', category_id=category_id,
            item_id=item_id, i=editedItem)


@app.route('/category/<int:category_id>/<int:item_id>/delete/',
           methods=['GET', 'POST'])
@login_required
def deleteFilmItem(category_id, item_id):
    """Route for deleting a Film item."""
    itemToDelete = session.query(Item).filter_by(id=item_id).one()
    creator = getUserInfo(itemToDelete.user_id)
    if itemToDelete.user_id != creator:
        return redirect('showItem', category_id=category.id,
                        item_id=itemToDelete.id)
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("Film deleted succesfully!")
        return redirect(url_for('default', category_id=category_id))
    else:
        return render_template('deletefilmitem.html', item=itemToDelete)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
