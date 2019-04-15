from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import db, Feedback, Quiz

import json
from . import utils


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/introduction')
def introduction():
    return render_template('Introduction.html')


@main.route('/theory')
def theory():
    return render_template('Theory.html')


@main.route('/objective')
def objective():
    return render_template('Objective.html')


@main.route('/experiment')
def experiment():
    return render_template('Experiment.html')


@main.route('/manual')
def manual():
    return render_template('Manual.html')


@main.route('/quizzes', methods=['GET', 'POST'])
def quizzes():
    if request.method == 'POST':
        one_correct = 0
        two_correct = 0
        three_correct = 0
        four_correct = 0
        sub_q1 = request.form['q1']
        sub_q2 = request.form['q2']
        sub_q3 = request.form['q3']
        sub_q4 = request.form['q4']
        sub_q5 = request.form['q5']
        if sub_q1 == "22":
            one_correct = 1
        if sub_q2 == "240":
            two_correct = 1
        if sub_q3 == "Private":
            three_correct = 1
        if sub_q4 == "Yes":
            four_correct = 1
        response = Quiz(sub_q1=sub_q1, sub_q2=sub_q2, sub_q3=sub_q3, sub_q4=sub_q4, sub_q5=sub_q5)
        print(response)
        db.session.add(response)
        db.session.commit()
        flash("You got " + str(one_correct + two_correct + three_correct + four_correct) + " correct out of 4")

    return render_template('Quizzes.html')


@main.route('/procedure')
def procedure():
    return render_template('Procedure.html')


@main.route('/further_readings')
def further_readings():
    return render_template('Further Readings.html')


@main.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        if not request.form['first_name'] or not request.form['last_name'] or not request.form['email']:
            flash('Please enter your details.', 'error')
        else:
            if len(request.form['first_name']) < 2:
                flash("First name too short", "error")
            elif len(request.form['last_name']) < 2:
                flash("Last name too short", "error")
            elif request.form['email'].find('@') == -1:
                flash("Please enter valid email", "error")
            else:
                response = Feedback(first_name=request.form['first_name'], last_name=request.form['last_name'],
                                email=request.form['email'], feedback=request.form['feedback'])
                print(response)
                db.session.add(response)
                db.session.commit()

                flash("Your feedback was recorded successfully", 'success')
                return redirect(url_for('main.feedback'))
    return render_template('Feedback.html')


@main.route('/see-all-quizzes')
def see_all_quizzes():
    return render_template('SeeAllQuizzes.html', quizzes=Quiz.query.all())


@main.route('/see-all-feedback')
def see_all():
    return render_template('SeeAll.html', feedbacks=Feedback.query.all())


@main.route('/api/generate')
def generate():
    sz = int(str(request.args.get('sz')))
    e = ""
    if request.args.get('e'):
        e = int(str(request.args.get('e')))
    if sz:
        if request.args.get('e'):
            ret = utils.generate(sz, e)
        else:
            ret = utils.generate(sz)
    else:
        return "Invalid"
    final_ret = {
        'n': ret[0],
        'e': hex(ret[1]),
        'p': ret[3],
        'q': ret[4],
        'dp_1': ret[5],
        'dq_1': ret[6],
        'coef': ret[7],
        'd': hex(ret[9].d)
    }

    return json.dumps(final_ret)


@main.route('/api/encrypt')
def encrypt():
    return json.dumps({'response': utils.encrypt(request.args.get('message'), int(request.args.get('n'), 16),
                                                 int(request.args.get('e'), 16)).hex()})


@main.route('/api/decrypt')
def decrypt():
    return utils.decrypt(request.args.get('crypto'), request.args.get('n'), request.args.get('e'),
                         request.args.get('d'), request.args.get('p'), request.args.get('q'))
