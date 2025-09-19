# Create a button to trigger the AI response generation, using the dynamic type
if st.button("Generate Completion", type=button_type):
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

                # Use st.json() to display the full response for debugging
                st.json(data)

                # The correct key is likely 'response'. Update this if st.json() shows otherwise.
                st.session_state.result = data['response']
        
        # Handle any errors during the API call
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.session_state.result = ""
    else:
        # Show a warning if the user clicks the button with an empty prompt
        st.warning("Please enter a prompt.")
