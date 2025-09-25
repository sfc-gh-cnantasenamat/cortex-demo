import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Cortex Demo", 
    page_icon=":primary[:material/network_intel_node:]",
    layout="wide"
)

# Define the pages as a list.
# A standalone st.Page object will be a top-level link.
# A dictionary will be a dropdown menu.
pages = [
    st.Page("text_app.py", title="Home", icon=":material/home:", url_path="home"),
    {
        "Cortex Text Demo": [
            st.Page("text_app.py", title="Cortex Text example", icon=":material/description:"),
            st.Page("text_minimal_app.py", title="Cortex Text (minimal) example", icon=":material/notes:"),
        ]
    }
]

# Create the navigation from the list of pages
pg = st.navigation(pages, position="top")

# Run the selected page
pg.run()
