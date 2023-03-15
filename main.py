from fileinput import filename
from distutils.log import debug
from flask import *
from split_pdf import split_in_files
from pathlib import Path
from shutil import rmtree

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        n = int(request.form['size'])
        f.save(f'tmp/{f.filename}')
        split_result = split_in_files(f'tmp/{f.filename}', 'tmp/result', n)
        #return render_template('success.html', name=f.filename, zip_url=url_for('static', filename=str(split_result)))
        print(split_result)
        return send_from_directory('tmp', split_result)

if __name__ == '__main__':
    tmp_path = Path('tmp')
    rmtree(tmp_path)
    tmp_path.mkdir(parents=True, exist_ok=True)
    app.run(debug=True)