# navbar.py
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
