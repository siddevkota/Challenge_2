import streamlit as st

from streamlit_option_menu import option_menu
import product1,product2,product3,admin

st.set_page_config(
    page_title="Review Response Bot",
)


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title='Response Bot',
                options=['Product1', 'Product2', 'Product3', 'Admin'],
                icons=['chat-fill', 'chat-fill', 'chat-fill', 'person-circle'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}, }

            )

        if app == "Product1":
            product1.app()
        if app == "Product2":
            product2.app()
        if app == "Product3":
            product3.app()
        if app == "Admin":
            admin.app()
    run()

st.markdown("<p style='text-align:center'>Created by: Team Corazon</p>", unsafe_allow_html=True)