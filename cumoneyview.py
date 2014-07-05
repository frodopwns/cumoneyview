# -*- coding: utf-8 -*-
"""
    CU Money View
    ~~~~~~

    A data visualizer for CU-Boulder Faculty/Staff salary information

"""

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
from flask.ext.pymongo import PyMongo

# create application
app = Flask(__name__)
#connect to mongo using db name = app.name...probably cumoneyview
mongo = PyMongo(app)
#show stack traces
app.debug = True


@app.route('/')
def show_entries():
    return render_template('show_entries.html')


@app.route('/ajax/entries')
def ajax_entries():
    entries = mongo.db.employees.find()
    #filter objectid then return entries as json
    return jsonify({"data":[{k: v for k, v in d.iteritems() if k != '_id'} for d in entries]})


if __name__ == "__main__":
    app.run(host='0.0.0.0')