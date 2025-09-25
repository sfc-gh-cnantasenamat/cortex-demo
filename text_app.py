import streamlit as st
import json
from snowflake.snowpark.functions import ai_complete

def run():
    """
    This function runs the main text generation demo with example prompts.
    """
    st.title(":primary[:material/network_intel_node:] Cortex Demo")
    st.info("A demo of Snowflake Cortex in action, with example prompts.")

    # Initialize a variable in session state to hold the AI's response
    if 'result' not in st.session_state:
        st.session_state.result = ""

    # Define the preset prompts for the pills widget
    option_map = {
        0: "Write a short poem about the first snowfall.",
        1: "What is Python?",
        2: "What is Streamlit?",
    }

    # Create the pills widget for prompt selection
    selection = st.pills(
        "Example Prompts:",
        options=option_map.keys(),
        format_func=lambda option: option_map[option],
    )

    # Set the prompt in the text area based on the user's pill selection
    default_prompt = ""
    if selection is not None:
        default_prompt = option_map[selection]

    # Create a text area for the user to enter or edit a prompt
    # The key is updated dynamically to reset the text area when a new pill is selected
    prompt = st.text_area("Enter a Prompt:", value=default_prompt, key=f"prompt_input_{selection}", height=150)

    # Set the button type to 'primary' (filled) if there is text, otherwise 'secondary' (outlined)
    button_type = "primary" if prompt else "secondary"

    # Create a button to trigger the AI response generation
    if st.button("Generate Completion", type=button_type):
        if prompt:
            try:
                session = st.connection("snowflake").session()
                with st.spinner("Generating Response..."):
                    df = session.range(1).select(
                        ai_complete(
                            model='claude-4-sonnet',
                            prompt=prompt,
                            show_details=True
                        ).alias("detailed_response")
                    )
                    json_string = df.collect()[0][0]
                    data = json.loads(json_string)

                    # Display the full JSON output in an expander
                    with st.expander("Full JSON Output"):
                        st.json(data)

                    # Display the main response in a container
                    with st.container(border=True):
                        st.markdown(data['choices'][0]['messages'])

            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.session_state.result = ""
        else:
            st.warning("Please enter a prompt.")
