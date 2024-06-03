import streamlit as st
import requests
import pandas as pd

API_URL = 'http://127.0.0.1:5000/submit-statement'

def main():
    st.title("Upload a File and Display JSON Response as Tables")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        payload = {"filename": uploaded_file.name}
        files = {'file': uploaded_file.getvalue()}

        # Make the POST request to the API
        response = requests.post(API_URL, params=payload,files=files)
        if response.status_code == 400:
            st.error("Invalid file format.")
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json().get("data")

            # Check if the response is a list of JSON objects
            if isinstance(data, list):
                # Display each JSON object as a table
                df = pd.DataFrame()
                for index, item in enumerate(data):
                    _df = pd.DataFrame([item])
                    df = pd.concat([df, _df], ignore_index=True)
                    
                st.table(df)
            else:
                st.error("The response is not a list of JSON objects.")
        else:
            st.error("Failed to get a valid response from the API.")

if __name__ == '__main__':
    main()
