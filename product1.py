import streamlit as st
import requests
import re


def app():
    # Define the Streamlit app
    st.title("Review Response Bot")


    st.image("product1.png", caption="Product Image", width=300)

    st.write('''
    Product: \n
    XYZ Noise-Canceling Headphones\n
    Description: \n
    These headphones feature advanced noise-cancellation technology and premium sound quality.
''')
    
    sensitive_keywords = ["sexist", "misogyny", "health hazard", "offensive"]
    

    # Create an input field for user input
    product_description = '''
    Product: XYZ Noise-Canceling Headphones
    Description: These headphones feature advanced noise-cancellation technology and premium sound quality.
'''

    if "review" not in st.session_state:
            st.session_state["review"] = ""

    review = st.text_area("Post a review:", st.session_state["review"])
    json_payload = {
            "desc": product_description,
            "review": review
        }
    # Check if the user has entered any input
    if review:
        # Make an API request
        api_url = "http://127.0.0.1:8000/test"  # Replace with your API endpoint

        response = requests.get(api_url,params=json_payload)

        # Check if the API request was successful
        if response.status_code == 200:
            # Display the API response
            rep = response.json()  # Assuming the API returns JSON data
            data = rep['response']['choices'][0]['message']['content']
            st.write("Review Response:")
            st.write(data)
        else:
            st.write(f"API request failed with status code: {response.status_code}")

        for keyword in sensitive_keywords:
            if re.search(rf'\b{keyword}\b', review, re.I):
                st.session_state["review"] = review
        return False
        
        


