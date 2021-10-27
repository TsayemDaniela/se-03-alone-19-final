from unittest.mock import MagicMock, patch, call
import main
import pytest


def test_create_instructor_less_args():

    req = MagicMock()

    def make_req_se(text, *args, **kwargs):
        return_values = {
            'name': '',
            'email': 'name@email.com',
            'password': "abcdef"
        }
        return return_values[text]
    req.form.get.side_effect = make_req_se

    instructor = MagicMock()
    db = MagicMock()
    make_req = MagicMock()
    with patch("main.request", req), \
    patch("main.Instructor", instructor), \
    patch("main.SQLAlchemy", db), \
    patch("main.make_response", make_req):

        main.create_instructor()

    assert make_req.call_args == call("Error: too few args")

def test_create_instructor_existing_instructor():
    
    req = MagicMock()

    def make_req_se(text, *args, **kwargs):
        return_values = {
            'name': 'Name',
            'email': 'name@email.com',
            'password': "abcdef"
        }
        return return_values[text]
    req.form.get.side_effect = make_req_se

    instructor = MagicMock()
    instructor.query.filter.first.return_value = "anything"
    db = MagicMock()
    make_req = MagicMock()
    with patch("main.request", req), \
    patch("main.Instructor", instructor), \
    patch("main.SQLAlchemy", db), \
    patch("main.make_response", make_req):

        main.create_instructor()

    assert make_req.call_args == call("name@email.com already exists!")

def test_create_instructor():
    
    req = MagicMock()

    def make_req_se(text, *args, **kwargs):
        return_values = {
            'name': 'Name',
            'email': 'name@email.com',
            'password': "abcdef"
        }
        return return_values[text]
    req.form.get.side_effect = make_req_se

    instructor = MagicMock()
    instructor.query.filter.return_value = MagicMock()
    instructor.query.filter.return_value.first.return_value = False
    
    db = MagicMock()
    make_req = MagicMock()
    with patch("main.request", req), \
    patch("main.Instructor", instructor), \
    patch("main.db", db), \
    patch("main.make_response", make_req):

        main.create_instructor()

    assert "successfully created!" in str(make_req.call_args[0])

def test_login_less_args():

    req = MagicMock()

    def make_req_se(text, *args, **kwargs):
        return_values = {
            'email': '',
            'password': "abcdef"
        }
        return return_values[text]
    req.form.get.side_effect = make_req_se

    instructor = MagicMock()
    db = MagicMock()
    make_req = MagicMock()

    with patch("main.request", req), \
    patch("main.Instructor", instructor), \
    patch("main.SQLAlchemy", db), \
    patch("main.make_response", make_req):

        main.login_check()
    assert make_req.call_args == call("Error: too few args")

def test_login_wrong_creds():

    req = MagicMock()

    def make_req_se(text, *args, **kwargs):
        return_values = {
            'email': 'email@email.com',
            'password': "abcdef"
        }
        return return_values[text]
    req.form.get.side_effect = make_req_se

    instructor = MagicMock()
    db = MagicMock()
    make_req = MagicMock()

    instructor = MagicMock()
    instructor.query.filter.return_value.filter.return_value = MagicMock()
    instructor.query.filter.return_value.filter.return_value.first.return_value = False

    with patch("main.request", req), \
    patch("main.Instructor", instructor), \
    patch("main.SQLAlchemy", db), \
    patch("main.make_response", make_req):

        main.login_check()

    assert make_req.call_args == call("Wrong credentials!")

def test_login():

    req = MagicMock()

    def make_req_se(text, *args, **kwargs):
        return_values = {
            'email': 'email@email.com',
            'password': "abcdef"
        }
        return return_values[text]
    req.form.get.side_effect = make_req_se

    instructor = MagicMock()
    db = MagicMock()
    make_req = MagicMock()

    instructor = MagicMock()
    instructor.query.filter.return_value.filter.return_value = MagicMock()
    instructor.query.filter.return_value.filter.return_value.first.return_value = True

    with patch("main.request", req), \
    patch("main.Instructor", instructor), \
    patch("main.SQLAlchemy", db), \
    patch("main.make_response", make_req):

        main.login_check()

    assert make_req.call_args == call("Logged in successfully!")

def test_student_login_less_args():

    req = MagicMock()

    def make_req_se(text, *args, **kwargs):
        return_values = {
            'email': '',
            'password': "abcdef"
        }
        return return_values[text]
    req.form.get.side_effect = make_req_se

    player = MagicMock()
    db = MagicMock()
    make_req = MagicMock()

    with patch("main.request", req), \
    patch("main.Player", player), \
    patch("main.SQLAlchemy", db), \
    patch("main.make_response", make_req):

        main.student_login_check()
    assert make_req.call_args == call("Error: too few args")

def test_student_login_wrong_creds():

    req = MagicMock()

    def make_req_se(text, *args, **kwargs):
        return_values = {
            'email': 'email@email.com',
            'password': "abcdef"
        }
        return return_values[text]
    req.form.get.side_effect = make_req_se

    player = MagicMock()
    db = MagicMock()
    make_req = MagicMock()

    player = MagicMock()
    player.query.filter.return_value.filter.return_value = MagicMock()
    player.query.filter.return_value.filter.return_value.first.return_value = False

    with patch("main.request", req), \
    patch("main.Player", player), \
    patch("main.SQLAlchemy", db), \
    patch("main.make_response", make_req):

        main.student_login_check()

    assert make_req.call_args == call("Wrong credentials!")

def test_student_login():

    req = MagicMock()

    def make_req_se(text, *args, **kwargs):
        return_values = {
            'email': 'email@email.com',
            'password': "abcdef"
        }
        return return_values[text]
    req.form.get.side_effect = make_req_se

    player = MagicMock()
    db = MagicMock()
    make_req = MagicMock()

    player = MagicMock()
    player.query.filter.return_value.filter.return_value = MagicMock()
    player.query.filter.return_value.filter.return_value.first.return_value = True

    with patch("main.request", req), \
    patch("main.Player", player), \
    patch("main.SQLAlchemy", db), \
    patch("main.make_response", make_req):

        main.student_login_check()

    assert make_req.call_args == call("Logged in successfully!")

def test_create_game_less_args():

    req = MagicMock()

    def make_req_se(text, *args, **kwargs):
        return_values = {
            'email': 'email@email.com',
            'password': "abcdef",
            'institute': 'jacobs',
            'games': '0'
        }
        return return_values[text]
    req.form.get.side_effect = make_req_se

    instructor = MagicMock()
    game = MagicMock()
    db = MagicMock()
    make_req = MagicMock()

    instructor = MagicMock()
    instructor.query.filter.return_value.filter.return_value = MagicMock()
    instructor.query.filter.return_value.filter.return_value.first.return_value = False

    with patch("main.request", req), \
    patch("main.Game", game), \
    patch("main.Instructor", instructor), \
    patch("main.db", db), \
    patch("main.make_response", make_req):

        main.create_game()

    assert make_req.call_args == call("Not enough args!")

def test_create_game_wrong_creds():

    req = MagicMock()

    def make_req_se(text, *args, **kwargs):
        return_values = {
            'email': 'email@email.com',
            'password': "abcdef",
            'institute': 'jacobs',
            'games': '8'
        }
        return return_values[text]
    req.form.get.side_effect = make_req_se

    instructor = MagicMock()
    game = MagicMock()
    db = MagicMock()
    make_req = MagicMock()

    instructor = MagicMock()
    instructor.query.filter.return_value.filter.return_value = MagicMock()
    instructor.query.filter.return_value.filter.return_value.first.return_value = False

    with patch("main.request", req), \
    patch("main.Game", game), \
    patch("main.Instructor", instructor), \
    patch("main.db", db), \
    patch("main.make_response", make_req):

        main.create_game()

    assert make_req.call_args == call("Wrong credentials!")

def test_create_game():

    req = MagicMock()

    def make_req_se(text, *args, **kwargs):
        return_values = {
            'email': 'email@email.com',
            'password': "abcdef",
            'institute': 'jacobs',
            'games': '8'
        }
        return return_values[text]
    req.form.get.side_effect = make_req_se

    instructor = MagicMock()
    game = MagicMock()
    db = MagicMock()
    make_req = MagicMock()

    instructor = MagicMock()
    instructor.query.filter.return_value.filter.return_value = MagicMock()

    with patch("main.request", req), \
    patch("main.Game", game), \
    patch("main.Instructor", instructor), \
    patch("main.db", db), \
    patch("main.make_response", make_req):

        main.create_game()

    assert game.call_count == 8
    assert "Created games with IDs: " in str(make_req.call_args[0])
