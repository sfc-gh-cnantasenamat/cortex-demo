import streamlit as st
from snowflake.snowpark.functions import ai_complete
import json

# App title and info
st.title(":primary[:material/network_intel_node:] Cortex Demo")
st.info("A demo of Snowflake Cortex in action.")

# Create a text input for the user's prompt
prompt = st.text_input("Enter a prompt:")

# Generate the response when the button is clicked and a prompt exists
button_type = "primary" if prompt else "secondary"

if st.button("Generate", type=button_type) and prompt:
    session = st.connection("snowflake").session()
    # Call the AI function and collect the string response
    with st.spinner("Generating response...", show_time=True):
        df = session.range(1).select(
              ai_complete(model='claude-4-sonnet', prompt=prompt, show_details=True).alias("detailed_response")
        )
        json_string = df.collect()[0][0]
        data = json.loads(json_string)
        st.write(data['choices'][0]['messages'])
