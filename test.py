from fuzzywuzzy import fuzz
from metaphone import doublemetaphone

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        string_1 = request.form['text1']
        string_2 = request.form['text2']
        x_1 = string_1.lower()
        x_2 = string_2.lower()
        r_1 = fuzz.ratio(doublemetaphone(x_1)[0], doublemetaphone(x_2)[0])
        r_2 = fuzz.ratio(x_1, x_2)
        if r_1 > 90:
            return render_template("result.html", value=r_1)
        elif r_2 > 85:
            return render_template("result.html", value=r_2)
        elif doublemetaphone(x_1)[0] is doublemetaphone(x_2)[0] :
            return render_template("result.html", value=)
        else:
            return render_template("result.html", value=0)




if __name__ == '__main__':
    app.run(debug=True)
