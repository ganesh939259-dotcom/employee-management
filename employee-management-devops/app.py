from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

employees = []

@app.route('/')
def home():
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form.get('name')
    role = request.form.get('role')

    employees.append({"name": name, "role": role})
    return redirect(url_for('home'))

@app.route('/delete/<int:index>')
def delete_employee(index):
    if index < len(employees):
        employees.pop(index)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
