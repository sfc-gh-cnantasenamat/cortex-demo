import streamlit as st
import json
from snowflake.snowpark.functions import ai_complete

# Set the page title and a small introduction for the app
st.set_page_config(page_title="Cortex Demo", page_icon=":primary[:material/network_intel_node:]")
st.title(":primary[:material/network_intel_node:] Cortex Demo")
st.info("A demo of Snowflake Cortex in action.")

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
    #st.write(f"Your selected prompt: :primary-badge[{default_prompt}]")

# Create a text area for the user to enter or edit a prompt
prompt = st.text_area("Enter a Prompt:", value=default_prompt, key=f"prompt_input_{selection}")

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
                        model='claude-3-5-sonnet',
                        prompt=prompt,
                        show_details=True
                    ).alias("detailed_response")
                )
                json_string = df.collect()[0][0]
                data = json.loads(json_string)

               
                with st.expander("Full Output"):
                    st.json(data)

                with st.container(border=True):
                    st.write(data['choices'][0]['messages'])

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.session_state.result = ""
    else:
        st.warning("Please enter a prompt.")

# Display the result if one exists in the session state
if st.session_state.result:
    st.success("Completion generated!")
    st.write(st.session_state.result)
