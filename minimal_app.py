import streamlit as st
from snowflake.snowpark.functions import ai_complete

# App title and info
st.title(":material/network_intel_node: Cortex Demo")
st.info("A demo of Snowflake Cortex in action.")

# Create a text input for the user's prompt
prompt = st.text_input("Enter a prompt:")

# Generate the response when the button is clicked and a prompt exists
if st.button("Generate") and prompt:
    session = st.connection("snowflake").session()
    # Call the AI function and collect the string response
    raw_response = session.range(1).select(ai_complete('claude-3-5-sonnet', prompt)).collect()[0][0]
    
    # Chain methods: 1. Strip quotes, 2. Replace '\\n' with '\n'
    response = raw_response.strip('"').replace('\\n', '\n')
    
    st.write(response)
