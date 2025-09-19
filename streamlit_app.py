import streamlit as st
import json
from snowflake.snowpark.functions import ai_complete

# Set the title of the Streamlit app
st.title(":material/network_intel_node: Cortex Demo")
st.success("A demo of Snowflake Cortex in action.")

# Initialize session state to store the result
if 'result' not in st.session_state:
    st.session_state.result = ""

option_map = {
    0: "Write a short poem about the first snowfall.",
    1: "What is Snowflake Cortex?",
    2: "What is Streamlit?",
}
selection = st.pills(
    "Tool",
    options=option_map.keys(),
    format_func=lambda option: option_map[option],
)
st.write(
    "Your selected prompt: "
    f"{None if selection is None else option_map[selection]}"
)

# Create a text area for user input
if selection is not None:
    # Use a unique key for the text_area to ensure its state is managed correctly
    prompt = st.text_area("Enter a prompt:", option_map[selection], key=f"prompt_input_{selection}")

    # Create a button to trigger the completion
    if st.button("Generate Completion"):
        if prompt: # Ensure the prompt is not empty
            try:
                session = st.connection("snowflake").session()
                with st.spinner("Generating response..."):
                    df = session.range(1).select(
                        ai_complete(
                            model='claude-3-5-sonnet',
                            prompt=prompt,
                            show_details=True
                        ).alias("detailed_response")
                    )
                    
                    json_string = df.collect()[0][0]
                    data = json.loads(json_string)

                    # --- THIS IS THE FIX ---
                    # The correct key is 'messages' at the top level of the JSON.
                    # We store the result in session_state.
                    st.session_state.result = data['messages']
            
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.session_state.result = "" # Clear previous result on error
        else:
            st.warning("Please enter a prompt.")

# Always display the result if it exists in session state
if st.session_state.result:
    st.success("Completion generated!")
    st.write(st.session_state.result)
