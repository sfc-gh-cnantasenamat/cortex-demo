import streamlit as st
from snowflake.snowpark.functions import ai_complete

# Set the title of the Streamlit app
st.title("Snowflake Cortex `ai_complete` Example ❄️")

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
            # completion = ai_complete(
            #     model="claude-4-sonnet",
            #     prompt=prompt
            # )
            df = session.range(1).select(
                ai_complete(
                    model='claude-4-sonnet',
                    prompt=prompt,
                    show_details=True
                ).alias("detailed_response")
            )
            result = df.collect()[0][0]
            
        # Display the generated text
        st.success("Completion generated!")
        st.write(result)

    except Exception as e:
        st.error(f"An error occurred: {e}")
