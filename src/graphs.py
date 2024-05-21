# graphs.py
#
# Copyright (C) 2024 Lamees Mohammad Dalbah, Sharaz Ali and Ghazi Al-Naymat
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import pandas as pd
import joblib
import plotly.express as px
import plotly.figure_factory as ff

import copy

layout = dict(
    autosize=True,
    #automargin=True,
    margin=dict(l=20, r=20, b=20, t=30),
    hovermode="closest",
    plot_bgcolor="#16103a",
    paper_bgcolor="#16103a",
    legend=dict(font=dict(size=10), orientation="h"),
    title="Satellite Overview",
    font_color ="#e0e1e6",
    xaxis_showgrid=False,
    yaxis_showgrid=False
)

# Model Read
svm_path = 'data/Support_Vector_Machine_Model.sav'
svm_model = joblib.load(svm_path)

rf_path = 'data/Random_Forest_Model.sav'
rf_model = joblib.load(rf_path)

# Data Read
data = pd.read_csv('data/Data1_Churn_Modelling.csv')

# Convert all columns heading in lowercase 
clean_column_name = []
columns = data.columns
for i in range(len(columns)):
    clean_column_name.append(columns[i].lower())
data.columns = clean_column_name

data = data.drop(["rownumber", "customerid", "surname"], axis = 1)


def dist_age():
    x1 = data[data['exited'] == 1]['age']
    x2 = data[data['exited'] == 0]['age']

    ff.create_distplot
    
    fig = ff.create_distplot([x1,x2], group_labels= ['Exited', 'Not Exited'],
                             bin_size=3,
                            #  curve_type='kde',
                             show_rug=False,
                            #  show_hist=False,
                             show_curve=False,
                             colors=['#47acb1','#f26522'])
    
    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    fig.update_layout(
        title = {'text': 'Age', 'x': 0.5},
        legend = {'x': 0.25}
    )
    
    return fig


def dist_estimatedsalary():
    x1 = data[data['exited'] == 1]['estimatedsalary']
    x2 = data[data['exited'] == 0]['estimatedsalary']
    
    fig = ff.create_distplot([x1,x2], group_labels= ['Exited', 'Not Exited'],
                             bin_size=3,
                             curve_type='kde',
                             show_rug=False,
                             show_hist=False,
                             show_curve=True,
                             colors=['#47acb1','#f26522'])
    
    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    fig.update_layout(
        title = {'text': 'Estimated Salary', 'x': 0.5},
        legend = {'x': 0.25}
        
    )
    
    return fig

def dist_balance():
    x1 = data[data['exited'] == 1]['balance']
    x2 = data[data['exited'] == 0]['balance']
    
    fig = ff.create_distplot([x1,x2], group_labels= ['Exited', 'Not Exited'],
                             bin_size=3,
                             curve_type='kde',
                             show_rug=False,
                             show_hist=False,
                             show_curve=True,
                             colors=['#47acb1','#f26522'])
    
    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    fig.update_layout(
        title = {'text': 'Balance', 'x': 0.5},
        legend = {'x': 0.25}
    )
    
    return fig
