from flask import session, flash
import hashlib
from database import find_user, new_user, match_pass


def login( usr, pwd ):
    #good username?
    if find_user(usr):
        #good username but password?
        if match_pass( usr, pwd ):
            session['user'] = usr
            return 0;
        #bad password
        else:
            flash("Incorrect password.");
            return 1;
    #bad username
    else:
        flash("Incorrect username.");
        return 1;

    
def is_logged_in():
    return 'user' in session


def logout():
    if is_logged_in():
        session.pop('user')

        
#if username is not taken, 
def sign_up( usr, pwd ):
    if find_user( usr ):
        #bad, reenter info
        flash("Username taken.");
        return 1;
    else:
        #good, add user
        new_user( usr, pwd );
        return 0;
