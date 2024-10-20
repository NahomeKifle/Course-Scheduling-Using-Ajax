from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'VCU_CLASS_OVERRIDE_FORM_KEY_136'  
Bootstrap(app)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    student_name = request.form.get('student_name')
    student_id = request.form.get('student_id')
    course_name = request.form.get('course_name')
    course_number = request.form.get('course_number')
    justification = request.form.get('justification')

    print(student_name, student_id, course_name, course_number)

    if not student_name or not student_id or not course_name or not course_number:
        flash('All required fields must be filled out', 'danger')
        return redirect(url_for('index'))

    flash('The course override has been submitted successfully!', 'success')
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)