import streamlit as st
import json
from snowflake.snowpark.functions import ai_complete

# Set the title of the Streamlit app
st.title(":material/network_intel_node: Cortex Demo")
st.success("A demo of Snowflake Cortex in action.")

option_map = {
    0: "Write a short poem about the first snowfall.",
    1: "What is Snowflake Cortex?",
    2: "What is Streamlit",
}
selection = st.pills(
    "Tool",
    options=option_map.keys(),
    format_func=lambda option: option_map[option],
    selection_mode="single",
)
st.write(
    "Your selected prompt: "
    f"{None if selection is None else option_map[selection]}"
)

# Create a text area for user input
if option_map[selection] is not None:
    prompt = st.text_area("Enter a prompt:", option_map[selection])

if prompt is not None:
    # Create a button to trigger the completion
    if st.button("Generate Completion"):
        try:
            # Get the Snowflake session from the Streamlit connection
            # This securely uses the connection details stored in your Streamlit app's secrets
            session = st.connection("snowflake").session()
    
            # Display a spinner while waiting for the response
            with st.spinner("Generating response..."):
                # Call the Complete function with the desired model and the user's prompt
                df = session.range(1).select(
                    ai_complete(
                        model='claude-3-5-sonnet',
                        prompt=prompt,
                        show_details=True
                    ).alias("detailed_response")
                )
                # Extracting result from the generated JSON output
                json_string = df.collect()[0][0]
                data = json.loads(json_string)
                result = data['choices'][0]['messages']
                
            # Display the generated text
            st.success("Completion generated!")
            st.write(result)
    
        except Exception as e:
            st.error(f"An error occurred: {e}")
