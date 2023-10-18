from fastapi import FastAPI, Query
import openai
import re
import requests

api_key = "YOUR_OPENAI_API_KEY"
app = FastAPI()
openai.api_key = api_key


def has_sensitive_keywords(text):
    sensitive_keywords = ["sexist", "misogyny", "health hazard", "offensive"]
    for keyword in sensitive_keywords:
        if re.search(rf'\b{keyword}\b', text, re.I):
            return True
    return False

@app.get("/test")
async def test(desc: str = Query(..., title="Product Description"), review: str = Query(..., title="Review")):

    messages = []
    rev = []

    if has_sensitive_keywords(review):
        # If sensitive keywords are found, send an alert to the admin
        admin_url = "http://127.0.0.1:8501/admin/sensitive_alert"
        response = requests.post(admin_url)

    # be as specific as possible in the behavior it should have
    system_content = '''
    You are a review response bot which responds to various kinds of reviews of users.
    You will be provided with a Product Description and the Review posted by the users.
    Your task is to give a custom to the Review of the product using only the using product description.
    If the review is positive respond gratefully, and if it is harsh or critical respond like a responsible salesman addressing the concerns. 
    .    '''

    messages.append({"role": "system", "content": system_content})

    prompt_text = f"""
     '''Product Description: {desc}'''
     
     '''Review: {review}'''
    
    """

    messages.append({"role": "user", "content": prompt_text})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000,
        temperature=0.5)


    return {"response": response}
