from transformers import pipeline   # type: ignore

def detect_input(user_input):  
    ai_model = pipeline("text-classification", model="bert-base-uncased")  
    result = ai_model(user_input)  
    return result[0]["label"]