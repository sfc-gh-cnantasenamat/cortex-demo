import streamlit as st

# Set the page configuration. This should be the first Streamlit command.
st.set_page_config(
    page_title="Cortex Demo", 
    page_icon=":primary[:material/network_intel_node:]",
    # layout="wide"
)

pages = {
        "Cortex Text Demo": [
            st.Page("text_app.py", title="Cortex Text example", icon=":material/description:"),
            st.Page("text_minimal_app.py", title="Cortex Text (minimal) example", icon=":material/notes:"),
        ]
    }

# Define the pages for the navigation
pg = st.navigation(pages, position="top")

# Run the selected page
pg.run()
