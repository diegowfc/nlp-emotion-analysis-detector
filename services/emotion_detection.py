import requests

def emotion_detector(text_to_analyze):
    """Function that calls the AI API to analyze the word/emotion"""
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    json_payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, headers=headers, json=json_payload, verify=False)
        response.raise_for_status()
        return response.json().get('text', 'No definition found')
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"
