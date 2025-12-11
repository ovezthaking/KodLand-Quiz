from flask import (Flask, render_template_string, request, make_response)
from templates.index import INDEX


app = Flask(__name__)


@app.route('/')
def index():
    best_score = request.cookies.get('best_score', '0')

    return render_template_string(INDEX,
                                  best_score=best_score,
                                  username=None,
                                  result=None)


@app.route('/submit', methods=['POST'])
def sumbit_form():
    username = request.form.get('username').strip()
    points = 0
    solutions = {
        1: 'pytorch',
        2: 'Scikit',
        3: 'numpy'
    }

    q1 = request.form.get('question1')
    q2 = request.form.get('question2')
    q3 = request.form.get('question3')
    questions = [q1, q2, q3]

    for i in range(1, len(solutions)+1):
        if questions[i-1] == solutions.get(i):
            points += 1

    q4 = request.form.get('question4')

    if 'train_test_split' in q4:
        points += 1

    score = round(points * 100/(len(solutions)+1))

    current_best = int(request.cookies.get('best_score', 0))

    new_best = max(score, current_best)

    res = make_response(render_template_string(INDEX,
                                               username=username,
                                               best_score=new_best,
                                               score=points,
                                               percentage=score,
                                               result=True))

    res.set_cookie('best_score', str(new_best), max_age=60*60*24*365)

    return res


if __name__ == '__main__':
    print('Server starting...')
    app.run(host='0.0.0.0', port=3000)
