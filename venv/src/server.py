from flask import Flask, Response, render_template, send_file, request, jsonify
import os
import sys
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estimated_price', methods=['get'])
def calculate_estimated_price():
    import filter
    price_range = 500
    thomann = filter.get_in_price_range(int(request.args.get('price')) - price_range/2, int(request.args.get('price')) + price_range/2, source='thomann')
    muztorg = filter.get_in_price_range(int(request.args.get('price')) - price_range/2, int(request.args.get('price')) + price_range/2, source='muztorg')
    t_av = 0
    m_av = 0

    for t in thomann:
        t_av += t['price']

    for m in muztorg:
        m_av += m['price']

    # return "idi nahuy"
    res = round(round(t_av/thomann.count(), 2)/round(m_av/muztorg.count(), 2), 2) * int(request.args.get('price'))
    return str(res)

import import_export

@app.route('/export/guitars')
def export_guitars():
    return import_export.export_collection()

@app.route('/export/reverb')
def export_reverb():
    return import_export.export_collection(collection='reverb', filepath='reverb.json')

@app.route('/import/guitars')
def import_guitars():
    return import_export.import_collection()

@app.route('/import/reverb')
def import_reverb():
    return import_export.import_collection(collection='reverb', filepath='reverb.json')
