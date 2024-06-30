import os
import json
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Loading my fine-tuned model and tokenizer
model_name = "JrX44/gemma-2b-it-fine-tune-email-spam"
model = AutoModelForSequenceClassification.from_pretrained(model_name,token='<<HF_TOKEN>>')
tokenizer = AutoTokenizer.from_pretrained(model_name,token='<<HF_TOKEN>>')

def load_json_from_file(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def save_json_to_file(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def classify_email_as_spam(email):
    try:
        # Tokenize input text and prepare for model input
        inputs = tokenizer(email['content'], return_tensors="pt", truncation=True, max_length=512)
        # Forward pass through the model
        outputs = model(**inputs)
        # Get predicted class (0: Not Spam, 1: Spam)
        predicted_class = torch.argmax(outputs.logits, dim=1).item()
        return predicted_class == 1
    except Exception as e:
        print(f"Error classifying email: {e}")
        return False

# Directory where JSON files are stored and where results will be saved
INPUT_DIRECTORY = "./email_extraction/extracted_emails"
OUTPUT_DIRECTORY = "./output"

# List all JSON files in the directory
json_files = [f for f in os.listdir(INPUT_DIRECTORY) if f.endswith('.json')]
for filename in json_files:
    input_filepath = os.path.join(INPUT_DIRECTORY, filename)
    output_filepath = os.path.join(OUTPUT_DIRECTORY, filename)
    email_data = load_json_from_file(input_filepath)
    is_spam = classify_email_as_spam(email_data)
    print(f"\nEmail '{email_data['subject']}' is classified as {'Spam' if is_spam else 'Not Spam'}")
    email_data['is_spam'] = is_spam
    save_json_to_file(email_data, output_filepath)
    print(f"Updated JSON file saved: {output_filepath}")
