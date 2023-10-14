# Response Bot API

This API demonstration, developed using FastAPI, serves as a Review Response Bot. It takes a product description and user-generated reviews and provides responses based on the description. It uses the OpenAI GPT-3 model to generate custom responses for the reviews. The API is intended for applications that involve responding to user reviews.

## API Endpoint

- Endpoint: `/test`
- Method: GET

### Request Parameters

- `desc`: Product description (string)
- `review`: User's review (string)

### Response

The API generates a response for the provided review and returns it in the JSON format:
  ```json
  {
  "response": "Generated review response content"
  }
  ```
The review response bot's api application is shown through streamlit app

## How to run the api
```bash
uvicorn api:app --reload
```

## How to run the streamlit app
```bash
streamlit run main.py
```
## Pip installs
```bash
pip install fastapi openai streamlit requests
```
