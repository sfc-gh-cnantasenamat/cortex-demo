import streamlit as st
import json
from snowflake.snowpark.functions import ai_complete

# Set the title and a small introduction for the app
st.title(":material/network_intel_node: Cortex Demo")
st.success("A demo of Snowflake Cortex in action.")

# Initialize a variable in session state to hold the AI's response
if 'result' not in st.session_state:
    st.session_state.result = ""

# Define the preset prompts for the pills widget
option_map = {
    0: "Write a short poem about the first snowfall.",
    1: "What is Snowflake Cortex?",
    2: "What is Streamlit?",
}

# Create the pills widget for prompt selection
selection = st.pills(
    "Tool",
    options=option_map.keys(),
    format_func=lambda option: option_map[option],
)

# Set the prompt in the text area based on the user's pill selection
default_prompt = ""
if selection is not None:
    default_prompt = option_map[selection]
    st.write(f"Your selected prompt: {default_prompt}")
else:
    st.write("Select a preset prompt or enter your own below.")

# Create a text area for the user to enter or edit a prompt
prompt = st.text_area("Enter a prompt:", value=default_prompt, key=f"prompt_input_{selection}")

# Create a button to trigger the AI response generation
if st.button("Generate Completion"):
    # Check if the prompt box is empty before making an API call
    if prompt:
        try:
            # Securely connect to Snowflake
            session = st.connection("snowflake").session()
            # Show a spinner while the model is generating a response
            with st.spinner("Generating response..."):
                # Call the Cortex AI function with the prompt
                df = session.range(1).select(
                    ai_complete(
                        model='claude-3-5-sonnet',
                        prompt=prompt,
                        show_details=True
                    ).alias("detailed_response")
                )
                
                # Extract and parse the JSON response from the DataFrame
                json_string = df.collect()[0][0]
                data = json.loads(json_string)
                
                # Store the AI's message in the session state
                st.session_state.result = data['messages']
        
        # Handle any errors during the API call
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.session_state.result = ""
    else:
        # Show a warning if the user clicks the button with an empty prompt
        st.warning("Please enter a prompt.")

# Display the result if one exists in the session state
if st.session_state.result:
    st.success("Completion generated!")
    st.write(st.session_state.result)
