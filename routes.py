from flask import Flask, request, render_template, redirect
from services import get_statistics_by_role

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    device_type = request.args['device_type'] if 'device_type' in request.args else 'switch'
    stat = get_statistics_by_role(device_type)
    return render_template('index.html', stat=stat, device_type=device_type)
    

@app.route('/reload/<device_type>')
def reload(device_type):
    return redirect(f'/?device_type={device_type}')
