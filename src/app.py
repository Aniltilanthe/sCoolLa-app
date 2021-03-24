# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 19:06:08 2020

@author: tilan
"""

# -*- coding: utf-8 -*-
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

from flask import request

from dash.dependencies import Input, Output, State

from flask_login import LoginManager, UserMixin


import numpy as np
import pandas as pd
#from data import studentGrouped


FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"

external_stylesheets = [
                        dbc.themes.BOOTSTRAP,
                        dbc.themes.MATERIA,
                        FA
                        ]

external_scripts = ["https://cdn.plot.ly/plotly-locale-fr-latest.js"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, external_scripts=external_scripts)
app.config.suppress_callback_exceptions = True

server = app.server
app.title = 'sCool Data Analysis App'


#<script src="plotly-locale-de-ch.js"></script>
#<script>Plotly.setPlotConfig({locale: 'de-CH'})</script>


# Setup the LoginManager for the server
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'

# config
server.config.update(
    SECRET_KEY='SCOOLSECRET@HEREITIS',
)



class User(UserMixin):
    def __init__(self, name, Id, active=True, isAdmin = False, securityStamp = ''):
        self.name = name
        self.id = Id
        self.active = active
        self.isAdmin = isAdmin
        self.securityStamp = securityStamp

    def is_active(self):
        return self.active

    def is_authenticated(self):
        return True

    def is_admin(self):
        return self.isAdmin



#VALID_USERNAME_PASSWORD_PAIRS = {
#    'peter.lerchbacher@schule.at': 'peter.lerchbacher@schule.at',
#    'a.kojic@live.com' : 'a.kojic@live.com'
#}
#
#
#
#auth = dash_auth.BasicAuth(
#    app,
#    VALID_USERNAME_PASSWORD_PAIRS
#)