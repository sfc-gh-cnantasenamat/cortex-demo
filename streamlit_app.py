import streamlit as st
from snowflake.cortex import Complete

# Set the title of the Streamlit app
st.title("Snowflake Cortex `Complete` Example ❄️")

# Create a text area for user input
prompt = st.text_area("Enter a prompt:", "Write a short poem about the first snowfall.")

# Create a button to trigger the completion
if st.button("Generate Completion"):
    try:
        # Get the Snowflake session from the Streamlit connection
        # This securely uses the connection details stored in your Streamlit app's secrets
        session = st.connection("snowflake").session()

        # Display a spinner while waiting for the response
        with st.spinner("Generating response..."):
            # Call the Complete function with the desired model and the user's prompt
            completion = Complete(
                model="llama2-70b-chat",
                prompt=prompt,
                session=session
            )
        
        # Display the generated text
        st.success("Completion generated!")
        st.write(completion)

    except Exception as e:
        st.error(f"An error occurred: {e}")
