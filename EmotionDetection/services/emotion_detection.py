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

        emotions_dict = response.json()

        emotion_scores = {
        emotion: score
            for emotion, score in emotions_dict["emotionPredictions"][0]["emotion"].items()
        }

        emotion_scores['dominant_emotion'] = max(zip(emotion_scores.values(), emotion_scores.keys()))[1]  

        emotion_statements = []

        for emotion, score in emotion_scores.items():
            if emotion != "dominant_emotion":
                emotion_statements.append(f"'{emotion}': {score}")

        concatenated_emotions_value = ", ".join(emotion_statements[:-1]) + f" and {emotion_statements[-1]}"
        response = f"For the given statement, the system response is {concatenated_emotions_value}. The dominant emotion is {emotion_scores['dominant_emotion']}."

        return response
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"
