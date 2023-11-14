from flask import Flask, redirect, render_template, request, url_for
import utility as u

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        classes = request.form['class']
        sections = request.form['sections']
        slots = request.form['slots']
        return redirect(url_for('result', classes=classes, sections=sections, slots=slots))
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    classes = request.args.get('classes')
    sections = request.args.get('sections')
    slots = request.args.get('slots')
    print(f"Classes: {classes}, Sections: {sections}, Slots: {slots}")
    s, k = u.findpattern()
    return render_template('createtable.html', schedule=s, header=k)

if __name__ == '__main__':
    app.run(debug=True)
