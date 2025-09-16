"""
Practice project
The functions of Watson AI libraries are deployed on IBM's Cloud IDE server, 
    and cannot be imported here.
"""
import json
import requests  # Import the requests library to handle HTTP requests

def sentiment_analyzer(text_to_analyse):
    """
    Takes a string input (text_to_analyse)
    """
    # URL of the sentiment analysis service
    url = ( 
        'https://sn-watson-sentiment-bert.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/SentimentPredict'
    )
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header, timeout=5)
  
    # Parse the JSON response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract sentiment label and score from the response
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # If the response status code is 500, set the label and score to None
    elif response.status_code == 500:
        label = None
        score = None
    
    # Return a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}