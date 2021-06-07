from flask import Flask
from flask import render_template
from flask import request
from block import write_block, check_integrity

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        patient = request.form.get('patient')
        dateofbirth = request.form.get('dateofbirth')
        address = request.form.get('address')

        write_block(patient=patient, dateofbirth=dateofbirth, address=address)
       

    return render_template('index.html')

@app.route('/checking')
def check():
    results = check_integrity()
    return render_template('index.html', checking_results=results)

if __name__ == '__main__':
    app.run(debug=True)