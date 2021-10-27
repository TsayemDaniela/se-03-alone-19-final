"""
Main file that defines the Flask backend and all the routes
"""

from flask import Flask,render_template,request,redirect,session,make_response,Response,jsonify

from flask_sqlalchemy import SQLAlchemy

# from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt



from app import createApp

config_name = os.getenv('FLASK_CONFIG')

app = createApp(config_name)








# sample demands most likely
demands = [8, 2, 2, 6, 4, 5, 2, 6]

@app.route('/<game_id>/make_retailer_order')
def make_retailer_order(game_id):
    """
    Order from retailer
    """

    outgoing = request.args.get('outgoing')
    this_game = Game.query.filter(
        Game.id == game_id
    ).first()
    if not this_game:
        return jsonify("This game doesn't exist in database!"), 400

    curr_player = this_game.curr_player
    if curr_player != 0:
        return jsonify("Not your turn yet!"), 403

    this_player = Player.query.filter(
        Player.current_game == game_id
    ).filter(
        Player.ptype == 0
    ).first()
    if not this_player:
        return jsonify("This player doesn't exist in database!"), 500

    curr_week = this_game.week

    if curr_week > len(demands):
        return jsonify("The game has ended!"), 400

    wholesaler_incoming = 0
    if this_game.week >= 2:

        wholesaler_incoming = Events.query.filter(
            Events.game_id == game_id
        ).filter(
            Events.ptype == 1
        ).filter(
            Events.week == this_game.week - 2
        ).first().order_amount
        if not wholesaler_incoming:
            return jsonify("The wholesaler order doesn't exist in database!"), 500

    this_player.inventory = this_player.inventory + wholesaler_incoming

    backorder = this_player.backorder
    inventory = this_player.inventory 
    demand = demands[this_game.week]
    total_demand = demand + backorder
    if inventory >= total_demand:
        backorder = 0
        inventory = inventory - total_demand
    else:
        difference = total_demand - inventory
        backorder = backorder + difference
        inventory = 0
    this_player.backorder = backorder
    stock_diff = this_player.inventory - inventory
    this_player.inventory = inventory

    new_event = Events(
        game_id = game_id,
        ptype = 0,
        order_amount = outgoing,
        week = this_game.week
    )

    this_game.curr_player = 1

    db.session.add(new_event)
    db.session.commit()

    next_incoming = Events.query.filter(
        Events.game_id == game_id
    ).filter(
        Events.ptype == 1
    ).filter(
        Events.week == this_game.week - 1
    ).first()
    if not next_incoming:
        next_incoming = 0
    else:
        next_incoming = next_incoming.order_amount

    demand
    return jsonify({
        "outgoing": stock_diff,
        "inventory": this_player.inventory,
        "backorder": this_player.backorder,
        "demand": "hidden",
        "incoming": next_incoming
    }), 200

@app.route('/<game_id>/make_wholesaler_order')
def make_wholesaler_order(game_id):
    """
    Order from wholesaler
    """

    outgoing = request.args.get('outgoing')
    this_game = Game.query.filter(
        Game.id == game_id
    ).first()
    if not this_game:
        return jsonify("This game doesn't exist in database!"), 400

    curr_player = this_game.curr_player
    if curr_player != 1:
        return jsonify("Not your turn yet!"), 403

    this_player = Player.query.filter(
        Player.current_game == game_id
    ).filter(
        Player.ptype == 1
    ).first()
    if not this_player:
        return jsonify("This player doesn't exist in database!"), 500

    curr_week = this_game.week

    if curr_week > len(demands):
        return jsonify("The game has ended!"), 400

    distributor_incoming = 0
    if this_game.week >= 2:

        distributor_incoming = Events.query.filter(
            Events.game_id == game_id
        ).filter(
            Events.ptype == 2
        ).filter(
            Events.week == this_game.week - 2
        ).first().order_amount
        if not distributor_incoming:
            return jsonify("The distributor order doesn't exist in database!"), 500

    this_player.inventory = this_player.inventory + distributor_incoming
    demand = 0

    prev_event = Events.query.filter(
        Events.game_id == game_id
    ).filter(
        Events.ptype == 0,
        Events.week == curr_week
    ).first()

    if not prev_event:
        return jsonify("The retailer's order doesn't exist in database!"), 500

    backorder = this_player.backorder
    inventory = this_player.inventory 
    demand = prev_event.order_amount
    total_demand = demand + backorder
    if inventory >= total_demand:
        backorder = 0
        inventory = inventory - total_demand
    else:
        difference = total_demand - inventory
        backorder = backorder + difference
        inventory = 0
    this_player.backorder = backorder
    stock_diff = this_player.inventory - inventory
    this_player.inventory = inventory

    new_event = Events(
        game_id = game_id,
        ptype = 1,
        order_amount = outgoing,
        week = this_game.week
    )

    this_game.curr_player = 2

    db.session.add(new_event)
    db.session.commit()

    next_incoming = Events.query.filter(
        Events.game_id == game_id
    ).filter(
        Events.ptype == 2
    ).filter(
        Events.week == this_game.week - 1
    ).first()
    if not next_incoming:
        next_incoming = 0
    else:
        next_incoming = next_incoming.order_amount

    return jsonify({
        "outgoing": stock_diff,
        "inventory": this_player.inventory,
        "backorder": this_player.backorder,
        "demand": "hidden",
        "incoming": next_incoming
    }), 200

@app.route('/<game_id>/make_distributor_order')
def make_distributor_order(game_id):
    """
    Order from distributor
    """

    outgoing = request.args.get('outgoing')
    this_game = Game.query.filter(
        Game.id == game_id
    ).first()
    if not this_game:
        return jsonify("This game doesn't exist in database!"), 400

    curr_player = this_game.curr_player
    if curr_player != 2:
        return jsonify("Not your turn yet!"), 403

    this_player = Player.query.filter(
        Player.current_game == game_id
    ).filter(
        Player.ptype == 2
    ).first()
    if not this_player:
        return jsonify("This player doesn't exist in database!"), 500

    curr_week = this_game.week

    if curr_week > len(demands):
        return jsonify("The game has ended!"), 400

    manufacturer_incoming = 0
    if this_game.week >= 2:

        manufacturer_incoming = Events.query.filter(
            Events.game_id == game_id
        ).filter(
            Events.ptype == 3
        ).filter(
            Events.week == this_game.week - 2
        ).first().order_amount
        if not manufacturer_incoming:
            return jsonify("The manufacturer order doesn't exist in database!"), 500

    this_player.inventory = this_player.inventory + manufacturer_incoming
    demand = 0

    prev_event = Events.query.filter(
        Events.game_id == game_id
    ).filter(
        Events.ptype == 1,
        Events.week == curr_week
    ).first()

    if not prev_event:
        return jsonify("The retailer's order doesn't exist in database!"), 500

    backorder = this_player.backorder
    inventory = this_player.inventory 
    demand = prev_event.order_amount
    total_demand = demand + backorder
    if inventory >= total_demand:
        backorder = 0
        inventory = inventory - total_demand
    else:
        difference = total_demand - inventory
        backorder = backorder + difference
        inventory = 0
    this_player.backorder = backorder
    stock_diff = this_player.inventory - inventory
    this_player.inventory = inventory

    new_event = Events(
        game_id = game_id,
        ptype = 2,
        order_amount = outgoing,
        week = this_game.week
    )

    this_game.curr_player = 3

    db.session.add(new_event)
    db.session.commit()

    next_incoming = Events.query.filter(
            Events.game_id == game_id
        ).filter(
            Events.ptype == 3
        ).filter(
            Events.week == this_game.week - 2
    ).first()
    if not next_incoming:
        next_incoming = 0
    else:
        next_incoming = next_incoming.order_amount

    return jsonify({
        "outgoing": stock_diff,
        "inventory": this_player.inventory,
        "backorder": this_player.backorder,
        "demand": "hidden",
        "incoming": next_incoming
    }), 200

@app.route('/<game_id>/make_factory_order')
def make_factory_order(game_id):
    """
    Order from factory
    """

    outgoing = request.args.get('outgoing')
    this_game = Game.query.filter(
        Game.id == game_id
    ).first()
    if not this_game:
        return jsonify("This game doesn't exist in database!"), 400

    curr_player = this_game.curr_player
    if curr_player != 3:
        return jsonify("Not your turn yet!"), 403

    this_player = Player.query.filter(
        Player.current_game == game_id
    ).filter(
        Player.ptype == 3
    ).first()
    if not this_player:
        return jsonify("This player doesn't exist in database!"), 500

    curr_week = this_game.week

    if curr_week > len(demands):
        return jsonify("The game has ended!"), 400

    fact_order_incoming = 0
    if this_game.week >= 2:

        fact_order_incoming = Events.query.filter(
            Events.game_id == game_id
        ).filter(
            Events.ptype == 3
        ).filter(
            Events.week == this_game.week - 2
        ).first().order_amount
        if not fact_order_incoming:
            return jsonify("The factory order doesn't exist in database!"), 500

    this_player.inventory = this_player.inventory + fact_order_incoming
    demand = 0

    prev_event = Events.query.filter(
        Events.game_id == game_id
    ).filter(
        Events.ptype == 2,
        Events.week == curr_week
    ).first()

    if not prev_event:
        return jsonify("The retailer's order doesn't exist in database!"), 500

    backorder = this_player.backorder
    inventory = this_player.inventory 
    demand = prev_event.order_amount
    total_demand = demand + backorder
    if inventory >= total_demand:
        backorder = 0
        inventory = inventory - total_demand
    else:
        difference = total_demand - inventory
        backorder = backorder + difference
        inventory = 0
    this_player.backorder = backorder
    stock_diff = this_player.inventory - inventory
    this_player.inventory = inventory

    new_event = Events(
        game_id = game_id,
        ptype = 3,
        order_amount = outgoing,
        week = this_game.week
    )

    next_incoming = Events.query.filter(
        Events.game_id == game_id
    ).filter(
        Events.ptype == 3
    ).filter(
        Events.week == this_game.week - 1
    ).first()
    if not next_incoming:
        next_incoming = 0
    else:
        next_incoming = next_incoming.order_amount

    this_game.curr_player = 0
    this_game.week = this_game.week + 1

    db.session.add(new_event)
    db.session.commit()

    return jsonify({
        "outgoing": stock_diff,
        "inventory": this_player.inventory,
        "backorder": this_player.backorder,
        "demand": "hidden",
        "incoming": next_incoming
    }), 200

@app.route('/create_instructor', methods=['GET', 'POST'])
def create_instructor():
    """Create a instructor via query string parameters."""
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    if name and email and password:
        existing_instructor = Instructor.query.filter(
            Instructor.email == email
        ).first()
        if existing_instructor:
            return make_response(
                f'{email} already exists!'
            )
        new_instructor = Instructor(
            name=name,
            email=email,
            password=password,
        )
        db.session.add(new_instructor)
        db.session.commit()
        return make_response(f"{new_instructor} successfully created!")
    else:
        return make_response(f"Error: too few args")

@app.route('/login_check', methods=['GET', 'POST'])
def login_check():
    """
    Check for instructor login
    """

    email = request.form.get('email')
    password = request.form.get('password')
    if email and password:
        existing_instructor = Instructor.query.filter(
            Instructor.email == email
        ).filter(
            Instructor.password == password
        ).first()
        if existing_instructor:
            return make_response("Logged in successfully!")
        else:
            return make_response("Wrong credentials!")
    else:
        return make_response("Error: too few args")

@app.route('/student_login_check', methods=['GET', 'POST'])
def student_login_check():
    """
    Check for student login
    """

    email = request.form.get('email')
    password = request.form.get('password')
    if email and password:
        existing_player = Player.query.filter(
            Player.email == email
        ).filter(
            Player.password == password
        ).first()
        if existing_player:
            return make_response("Logged in successfully!")
        else:
            return make_response("Wrong credentials!")
    else:
        return make_response("Error: too few args")

@app.route('/create_game', methods=['GET', 'POST'])
def create_game():
    """
    Create X amount of games for a certain instructor
    """

    email = request.form.get('email')
    password = request.form.get('password')
    games = int(request.form.get('games'))
    institute = request.form.get('institute')

    if email and password and institute and games:
        existing_instructor = Instructor.query.filter(
            Instructor.email == email
        ).filter(
            Instructor.password == password
        ).first()
        if existing_instructor:
            response = "Created games with IDs: "
            for _ in range(games):
                new_game = Game(
                    session_length=10,
                    distributor_present=True,
                    wholesaler_present=True,
                    holding_cost=4,
                    backlog_cost=8,
                    session_id=1,
                    instructor=existing_instructor,
                    active=True,
                    info_sharing=True,
                    curr_player=0,
                    info_delay=2,
                    is_default_game=False,
                    starting_inventory=10,
                    instructor_id=existing_instructor.id,
                    week=0

                )
                db.session.add(new_game)
                db.session.commit()
                for ptype in range(4):
                    print(new_game.id)
                    new_player = Player(
                        ptype = ptype,
                        name = "foo player",
                        password = "password",
                        current_game = new_game.id,
                        inventory = 12,
                        backorder = 0
                    )
                    db.session.add(new_player)

                db.session.commit()
                response = response + f'{new_game.id}, '
            return make_response(response[:-2])


        else:
            return make_response("Wrong credentials!")
    else:
        return make_response("Not enough args!")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
   if request.method == 'POST':
    
      print(request.json)
    #   return redirect(url_for('success',name = user))
   else:
       print("here")
       pass
    #   user = request.args.get('nm')
    #   return redirect(url_for('success',name = user))

if __name__=="__main__":
    with app.app_context():
        db.create_all()
        if not Game.query.first():
            dummy_instructor = Instructor(
                name="dummy",
                email="dummy@dummy.com",
                password="dummy",
            )
            db.session.add(dummy_instructor)
            db.session.commit()
            new_game = Game(
                session_length=10,
                distributor_present=True,
                wholesaler_present=True,
                holding_cost=4,
                backlog_cost=8,
                session_id=1,
                instructor=dummy_instructor,
                active=True,
                info_sharing=True,
                curr_player=0,
                info_delay=2,
                is_default_game=False,
                starting_inventory=10,
                instructor_id=dummy_instructor.id,
                week=0
            )
            db.session.add(new_game)
            db.session.commit()
            for ptype in range(4):
                new_player = Player(
                    ptype = ptype,
                    name = "foo player",
                    password = "password",
                    current_game = new_game.id,
                    inventory = 12,
                    backorder = 0
                )
                db.session.add(new_player)
            db.session.commit()
        app.run(debug=True)
