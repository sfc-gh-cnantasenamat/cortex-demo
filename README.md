# Cortex Demo

A simple [Streamlit in Snowflake (SiS)](https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit) app that demonstrates [Snowflake Cortex](https://docs.snowflake.com/en/user-guide/snowflake-cortex/overview) AI functions for text generation using large language models.

## Overview

This app showcases how to call Cortex AI functions directly from a Streamlit app running inside Snowflake. It uses the `ai_complete()` function to generate text completions powered by LLMs (e.g. `claude-4-sonnet`).

## App Pages

| File | Description |
|------|-------------|
| `streamlit_app.py` | Main entry point with multi-page navigation |
| `text_app.py` | Text generation with example prompt pills and full JSON output |
| `text_minimal_app.py` | Simplified single-input text generation |
| `minimal_app.py` | Bare-minimum single-page Cortex demo |

## Requirements

- A Snowflake account with Cortex AI enabled
- The `snowflake-snowpark-python` package (listed in `requirements.txt`)

## Deploying to Streamlit in Snowflake

1. **Open Snowsight** and navigate to **Projects → Streamlit**.
2. Click **+ Streamlit App** and give it a name (e.g. `CORTEX_DEMO`).
3. Select a warehouse, database, and schema for the app.
4. In the editor, upload or paste the contents of `streamlit_app.py` as the main file.
5. Upload `text_app.py` and `text_minimal_app.py` as additional files in the same app.
6. In the **Packages** panel, add `snowflake-snowpark-python` (or leave it at the default — it is pre-installed in SiS).
7. Click **Run** to launch the app.

> **Note:** The app uses `st.connection("snowflake")` which resolves automatically when running inside Snowflake — no extra credentials or secrets are needed.

## Running Locally (Optional)

To run against a Snowflake account from your local machine:

1. Create a `.streamlit/secrets.toml` file with your Snowflake connection details:

   ```toml
   [connections.snowflake]
   account   = "<your_account>"
   user      = "<your_user>"
   password  = "<your_password>"
   warehouse = "<your_warehouse>"
   database  = "<your_database>"
   schema    = "<your_schema>"
   ```

2. Install dependencies:

   ```bash
   pip install streamlit snowflake-snowpark-python
   ```

3. Run the app:

   ```bash
   streamlit run streamlit_app.py
   ```

## Further Reading

- [Snowflake Cortex Overview](https://docs.snowflake.com/en/user-guide/snowflake-cortex/overview)
- [Streamlit in Snowflake Docs](https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit)
- [ai_complete() Function Reference](https://docs.snowflake.com/en/sql-reference/functions/ai_complete-snowflake-cortex)
