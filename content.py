# content.py
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
import plotly.express as px
import plotly.figure_factory as ff

import os
import sys
import copy

from src.graphs import dist_age, dist_estimatedsalary, dist_balance


# DATA ANALYSIS

card_tensure = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Graph(figure = dist_age(), config = {"displayModeBar": False}, style = {"height": "42vh"})
            ]
        ),
    ],
    style = {"background-color": "#16103a"}
)

card_monthlycharges = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Graph(figure = dist_estimatedsalary(), config = {"displayModeBar": False}, style = {"height": "42vh"})
                    
            ]
        ),
    ],
    style = {"background-color": "#16103a"}
)



card_totalcharges = dbc.Card(
    [
        dbc.CardBody(
            [
                dcc.Graph(figure = dist_balance(), config = {"displayModeBar": False}, style = {"height": "42vh"})
            ]
        ),
    ],
    style = {"background-color": "#16103a"}
)

card_categorical = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Spinner(size="md",color="light",
                    children=[
                        dcc.Graph(id="categorical_bar_graph", config = {"displayModeBar": False}, style = {"height": "48vh"})
                    ]
                ),
                
            ], style = {"height": "52vh"}
        ),
    ],
    style = {"background-color": "#16103a"}
)

card_donut = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Spinner(size="md",color="light",
                    children=[
                        dcc.Graph(id="categorical_pie_graph", config = {"displayModeBar": False}, style = {"height": "48vh"})
                    ]
                ),
                
            ], style = {"height": "52vh"}
        ),
    ],
    style = {"background-color": "#16103a"}
)

# TABS

tab_graphs = [

    # Categorical Fetaures Visualization
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.Row(
                        [

                            dbc.Col([
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupAddon("Categorical Feature", addon_type="prepend"),
                                        dbc.Select(
                                            options=[
                                                {"label": "Geography", "value": "geography"},
                                                {"label": "Gender", "value": "gender"},
                                                {"label": "Has Credit Card", "value": "hascrcard"},
                                                {"label": "Is Active Member", "value": "isactivemember"},
                                                {"label": "Exited", "value": "exited"},
                            
                                            ], id = "categorical_dropdown", value="geography"
                                        )
                                    ]
                                ),


                                html.Img(src="../assets/customer.png", className="customer-img")
                                
                                
                                ],lg="4", sm=12,
                            ),


                            dbc.Col(card_donut, lg="4", sm=12),

                            # dbc.Spinner(id="loading2",size="md", color="light",children=[dbc.Col(card_categorical, lg="4", sm=12)]),

                            dbc.Col(card_categorical, lg="4", sm=12),

                        ], className="h-15", style={"height": "100%"}
                    )
                ]
            ),
            className="mt-3", style = {"background-color": "#272953"}
        ),

    # Age, Estimated Salary and Balance Visualizaion

    dbc.Card(
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(card_tensure, lg="4", sm=12),
                        dbc.Col(card_monthlycharges, lg="4", sm=12),
                        dbc.Col(card_totalcharges, lg="4", sm=12),  
                    ], className="h-15"
                )
            ]
        ),
        className="mt-3", style = {"background-color": "#272953"}
    )

]

tab_analysis_content = tab_graphs


# PREDICTION

tab_prediction_features = dbc.Card(
    dbc.CardBody(
        [
            # First Row

            dbc.Row(
                [
                    # Credit Score
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Credit Score", addon_type="prepend"),
                                    dbc.Input(
                                        id="ft_credit_score",
                                        placeholder="Amount", type="number", value="645"
                                    ),
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Geography
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Geography", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_geography",
                                        options=[
                                            {"label": "France", "value": "France"},
                                            {"label": "Spain", "value": "Spain"},
                                            {"label": "Germany", "value": "Germany"},
                                        ], value="Spain"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Gender
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Gender", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_gender",
                                        options=[
                                            {"label": "Female", "value": "Female"},
                                            {"label": "Male", "value": "Male"},
                                        ], value="Male"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Age
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Age", addon_type="prepend"),
                                    dbc.Input(
                                        id="ft_age",
                                        placeholder="Amount", type="number", value="44"
                                    ),
                                ]
                            )
                        ], lg="3", sm=12
                    )
                ], className="feature-row",
            ), 

            # Second Row

            dbc.Row(
                [
                    # Tenure
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Tenure", addon_type="prepend"),
                                    dbc.Input(
                                        id="ft_tenure",
                                        placeholder="Amount", type="number", value="8"
                                    ),
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Balance
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Balance ($)", addon_type="prepend"),
                                    dbc.Input(
                                        id="ft_balance",
                                        placeholder="Amount", type="number", value="113755.78"
                                    ),
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Number of products
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Number of Products", addon_type="prepend"),
                                    dbc.Input(
                                        id="ft_num_products",
                                        placeholder="Amount", type="number", value="2"
                                    ),
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Has Credit Card
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Has Credit Card", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_has_credit_card",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"}
                                        ], value="Yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    )
                ], className="feature-row",
            ),

            # Third Row

            dbc.Row(
                [
                    # Is Active Member
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Is Active Member", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_is_active_member",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"}
                                        ], value="No"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Estimated Salary
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Estimated Salary ($)", addon_type="prepend"),
                                    dbc.Input(
                                        id="ft_estimated_salary",
                                        placeholder="Amount", type="number", value="149756.71"
                                    ),
                                ]
                            )
                        ], lg="3", sm=12
                    )
                ], className="feature-row",
            ),
        ]
    ),
    className="mt-3", style = {"background-color": "#272953"}
)

tab_prediction_result = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Button("Predict", id='btn_predict', size="lg", className="btn-predict")
                        ], lg="4", sm=4, style={"display": "flex", "align-items":"center", "justify-content":"center"},
                        className="card-padding"
                    ),

                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        dbc.Spinner(html.H4(id="rf_result", children="-", style={'color':'#e7b328'}), size="sm", spinner_style={'margin-bottom': '5px'}),
                                        html.P("Random Forest")
                                    ]
                                ), className="result-card", style={"height":"16vh"}
                            )
                        ], lg=4, sm=4, className="card-padding"
                    ),

                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        dbc.Spinner(html.H4(id="svm_result", children="-", style={'color':'#e7b328'}), size="sm", spinner_style={'margin-bottom': '5px'}),
                                        html.P("SVM")
                                    ]
                                ), className="result-card", style={"height":"16vh"}
                            )
                        ], lg=4, sm=4, className="card-padding"
                    )


                ]
            ),


        ]
    ),
    className="mt-3", style = {"background-color": "#272953"}
)

tab_prediction_content = [
    
    tab_prediction_features,
    tab_prediction_result
    
]
