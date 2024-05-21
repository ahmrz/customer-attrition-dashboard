import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

def get_navbar():

    nav_item_nn = dbc.NavItem(
        [
            dbc.NavLink(
                [
                    html.A(
                        [
                            html.Img(src="/assets/NN.png", className="nn-logo"),
                            html.P("Machine Learning", style={'display':'inline', 'color': '#EBEBEB'})
                        ],
                        href="https://www.ajman.ac.ae/en/academics/academic-programs-majors/programs/master-of-science-in-artificial-intelligence.html"
                    )
                    
                ]
            )
            
        ]
        
    )

    logo = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                        [
                            html.Img(src="/assets/ajman_logo_login.png", className="nn-logo"),
                            html.P("Ajman University", style={'display':'inline', 'color': '#EBEBEB'})
                        ],
                        href="https://www.ajman.ac.ae/en/"
                ),
                dbc.NavbarToggler(id="navbar-toggler"),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            #nav_item_home,
                            #nav_item_about,
                            nav_item_nn
                        ], className="ml-auto", navbar=True
                    ),
                    id="navbar-collapse",
                    navbar=True,
                ),
            ]
        ),
        color="primary",
        dark=True,
        className="mb-5",
    )

    return logo