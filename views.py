from flask import Blueprint, render_template, request

import json
import utils

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


@main.route('/quizzes')
def quizzes():
    return render_template('Quizzes.html')


@main.route('/procedure')
def procedure():
    return render_template('Procedure.html')


@main.route('/further_readings')
def further_readings():
    return render_template('Further Readings.html')


@main.route('/feedback')
def feedback():
    return render_template('Feedback.html')


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

