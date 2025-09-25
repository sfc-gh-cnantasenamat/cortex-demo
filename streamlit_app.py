import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Cortex Demo", 
    page_icon=":primary[:material/network_intel_node:]",
    layout="wide"
)

# Define the page structure with unique url_path for each page
pages = {
        "Home": [st.Page("text_app.py", title="Home", icon=":material/home:", url_path="home")],
        "Cortex Text Demo": [
            st.Page("text_app.py", title="Cortex Text example", icon=":material/description:"),
            st.Page("text_minimal_app.py", title="Cortex Text (minimal) example", icon=":material/notes:"),
        ]
    }

# Define the pages for the navigation
pg = st.navigation(pages, position="top")

# Run the selected page
pg.run()

