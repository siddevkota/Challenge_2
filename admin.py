import streamlit as st

def app():
    st.title("Admin Page")
    st.write("This is the admin page for monitoring sensitive reviews.")

    # Listen for sensitive review alerts
    st.write("Alerts:", st.session_state["review"])

if __name__ == "__main__":
    app()
