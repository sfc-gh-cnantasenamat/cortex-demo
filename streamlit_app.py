import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Cortex Demo", 
    page_icon=":primary[:material/network_intel_node:]",
    layout="wide"
)

# Define the pages for the "Cortex Text Demo" section
cortex_demo_pages = [
    st.Page("text_app.py", title="Cortex Text example", icon=":material/description:"),
    st.Page("text_minimal_app.py", title="Cortex Text (minimal) example", icon=":material/notes:"),
]

# Define the full navigation structure
pages = [
    # A standalone page for Home, set as the default
    st.Page("text_app.py", title="Home", icon=":material/home:", url_path="home", default=True),
    # A page that creates a section with the pages defined above
    st.Page("Cortex Text Demo", icon=":material/text_fields:", pages=cortex_demo_pages),
]

# Create the navigation from the list of pages
pg = st.navigation(pages, position="top")

# Run the selected page
pg.run()
