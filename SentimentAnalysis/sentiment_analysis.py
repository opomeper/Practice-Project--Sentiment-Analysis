''' This function send text_to_analyse to the watson to analyse
'''
import json
import requests

def sentiment_analyzer(text_to_analyse):
    '''
    This function sends text_to_analyse to the Watson API for sentiment analysis.
    '''
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict' # Watson API endpoint, no access yet, need to created IBM cloud account, alredy send ticket
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=header)
    if response.status_code == 500:
        return {'label' : None, 'score' : None}

    formatted_response = json.loads(response.text)
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']
    return {'label': label, 'score': score}
