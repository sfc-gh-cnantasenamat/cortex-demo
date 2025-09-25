import streamlit as st
from snowflake.snowpark.functions import ai_complete
import json

def run():
    """
    This function runs the minimal version of the text generation demo.
    """
    # App title and info
    st.title(":primary[:material/network_intel_node:] Cortex Demo (Minimal)")
    st.info("A simplified demo of Snowflake Cortex for quick text generation.")

    # Create a text input for the user's prompt
    prompt = st.text_input("Enter a prompt:", label_visibility="collapsed", placeholder="Enter a prompt")

    # Determine button type based on prompt existence
    button_type = "primary" if prompt else "secondary"

    # Generate the response when the button is clicked and a prompt exists
    if st.button("Generate", type=button_type) and prompt:
        try:
            session = st.connection("snowflake").session()
            # Call the AI function and collect the string response
            with st.spinner("Generating response..."):
                df = session.range(1).select(
                    ai_complete(model='claude-4-sonnet', prompt=prompt, show_details=True).alias("detailed_response")
                )
                json_string = df.collect()[0][0]
                data = json.loads(json_string)
                st.markdown(data['choices'][0]['messages'])
        except Exception as e:
            st.error(f"An error occurred: {e}")
