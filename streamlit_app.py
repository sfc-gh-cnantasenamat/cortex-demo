import streamlit as st
import text_app
import text_minimal_app

# Set the page configuration. This should be the first Streamlit command.
st.set_page_config(
    page_title="Cortex Demo", 
    page_icon=":primary[:material/network_intel_node:]",
    layout="wide"
)

# Define the pages for the navigation
pg = st.navigation(
    {
        "Examples": [
            st.Page(text_app.run, title="Text example", icon=":material/description:"),
            st.Page(text_minimal_app.run, title="Text (minimal) example", icon=":material/notes:"),
        ]
    }
)

# Run the selected page
pg.run()
