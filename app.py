import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash import no_update

import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

import os
import sys
import copy
import time

from sklearn.preprocessing import StandardScaler
from src.navbar import get_navbar
from src.graphs import data, layout, svm_model, rf_model
from content import tab_prediction_content, tab_analysis_content

# Creating the app

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    external_stylesheets = [dbc.themes.SUPERHERO,'/assets/styles.css']
) 

server=app.server

# Tabs Content

tabs = dbc.Tabs(
    [
        dbc.Tab(tab_prediction_content, label="Prediction"),
        dbc.Tab(tab_analysis_content, label="Data Analysis")
    ]
)


jumbotron = dbc.Jumbotron(
    [
        # html.H1("Jumbotron", className="display-3"),
        # html.P(
        #     "Use a jumbotron to call attention to "
        #     "featured content or information.",
        #     className="lead",
        # ),
        # html.Hr(className="my-2"),
        html.H4("Bank Customer Attrition Prediction System"),
        # html.P(dbc.Button("Learn more", color="primary"), className="lead"),
    ], className="cover"
)


# App Layout

app.layout = html.Div(
    [
        get_navbar(),
        jumbotron,
        html.Div(
            [
                
                dbc.Row(dbc.Col(tabs, width=12)),
                
            ], id="mainContainer",style={"display": "flex", "flex-direction": "column"}
        ),

        html.P("Modified by Lamees and Sharaz", className="footer")


    ],
)

# Callbacks

@app.callback(
    Output("categorical_bar_graph", "figure"),
    [
        Input("categorical_dropdown", "value"),
    ],
)

def bar_categorical(feature):

    time.sleep(0.2)

    temp = data.groupby([feature, 'exited']).count()['isactivemember'].reset_index()
    
    fig = px.bar(temp, x=feature, y="isactivemember",
             color=temp['exited'].map({0: 'Not Exited', 1: 'Exited'}),
             color_discrete_map={"Not Exited": "#f26522", "Exited": "#47acb1"},
             barmode='group')
    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    _title = (feature[0].upper() + feature[1:]) + " Distribution by Exited"
    
    fig.update_layout(
        title = {'text': _title, 'x': 0.5},
        #xaxis_visible=False,
        xaxis_title="",
        yaxis_title="Count",
        legend_title_text="",
        legend = {'x': 0.16}
    )
    return fig

@app.callback(
    Output("categorical_pie_graph", "figure"),
    [
        Input("categorical_dropdown", "value"),
    ],
)

def donut_categorical(feature):

    time.sleep(0.2)

    temp = data.groupby([feature]).count()['gender'].reset_index()

    fig = px.pie(temp, values="gender", names=feature, hole=.5,
                            #color=temp['Exited'].map({'Yes': 'Exited', 'No': 'NoExited'}),
                                #color_discrete_map={"Exited": "#47acb1",
                                                            #"NoExited": "#f26522"},
    )

    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    _title = (feature[0].upper() + feature[1:]) + " Percentage"

    if(data[feature].nunique() == 2):
        _x = 0.3
    elif(data[feature].nunique() == 3):
        _x = 0.16
    else:
        _x = 0

    fig.update_layout(
        title = {'text': _title, 'x': 0.5},
        legend = {'x': _x}
    )



    return fig


# Prediction

@app.callback(
    [dash.dependencies.Output('rf_result', 'children'),
    dash.dependencies.Output('svm_result', 'children')],

    [dash.dependencies.Input('btn_predict', 'n_clicks')],

    [dash.dependencies.State('ft_credit_score', 'value'),
     dash.dependencies.State('ft_geography', 'value'),
     dash.dependencies.State('ft_gender', 'value'),
     dash.dependencies.State('ft_age', 'value'),
     dash.dependencies.State('ft_tenure', 'value'),
     dash.dependencies.State('ft_balance', 'value'),
     dash.dependencies.State('ft_num_products', 'value'),
     dash.dependencies.State('ft_has_credit_card', 'value'),
     dash.dependencies.State('ft_is_active_member', 'value'),
     dash.dependencies.State('ft_estimated_salary', 'value')]
)

def predict_exited(n_clicks, ft_credit_score, ft_geography, ft_gender, ft_age, ft_tenure,
                    ft_balance, ft_num_products, ft_has_credit_card, ft_is_active_member,
                    ft_estimated_salary):

    time.sleep(0.4)

    sample = {'creditscore': int(ft_credit_score), 'geography': ft_geography, 'gender': ft_gender,
              'age': int(ft_age), 'tenure': int(ft_tenure), 'balance': float(ft_balance), 
              'numofproducts': int(ft_num_products), 'hascrcard': ft_has_credit_card,
              'isactivemember': ft_is_active_member, 'estimatedsalary': float(ft_estimated_salary)}

    sample_df = pd.DataFrame(sample, index=[0])

    gender = {"Female": 0, "Male": 1}
    city = {'France' : 0, 'Spain' : 1,'Germany' : 2}
    truefalse = {"No": 0, "Yes": 1}

    sample_df['gender'] = sample_df['gender'].replace(gender)
    sample_df['geography'] = sample_df['geography'].replace(city)
    sample_df['hascrcard'] = sample_df['hascrcard'].replace(truefalse)
    sample_df['isactivemember'] = sample_df['isactivemember'].replace(truefalse)

    rf_prediction = rf_model.predict(sample_df)
    svm_prediction = svm_model.predict(sample_df)

    def exited_to_text(num):
        if(num == 0):
            return "Predicted: Not Exited"
        elif(num == 1):
            return "Predicted: Exited"

    if(n_clicks):
        return exited_to_text(rf_prediction.item(0)), exited_to_text(svm_prediction.item(0))
    else:
        return no_update

@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)

# we use a callback to toggle the collapse on small screens
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)