import streamlit as st

# Set the page configuration
page_icon = ":primary[:material/network_intel_node:]"
st.set_page_config(
    page_title="Cortex Demo", 
    page_icon=page_icon,
    layout="wide"
)

def home():
    st.title(f"{page_icon} Cortex Demo App")

    st.markdown("""
    Key Cortex functions:
        - `ai_complete()` for text and image processing
        - `ai_transcribe()` for audio transcription
    """)

# Define the pages for the sections
main_pages = [
    st.Page(home, title="Home", icon=":material/home:")
]

cortex_demo_pages = [
    st.Page("text_app.py", title="Text Demo 1", icon=":material/description:"),
    st.Page("text_minimal_app.py", title="Text Demo 2", icon=":material/notes:"),
]

# Define the full navigation structure
pages = {
    "": main_pages,
    "Text Demo": cortex_demo_pages
}

# Create the navigation from the list of pages
pg = st.navigation(pages, position="top")

# Run the selected page
pg.run()
