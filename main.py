import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

api_key = os.getenv('api')

# Ensure the API key is retrieved
if api_key is None:
    raise ValueError("API key not found in environment variables.")

# Configure the AI library with the API key
genai.configure(api_key=api_key)

# Load generation configuration from the JSON file
with open('generation_config.json', 'r') as file:
    generation_config = json.load(file)

# Load safety settings from the JSON file
with open('safety_settings.json', 'r') as file:
    safety_settings = json.load(file)['safety_settings']


# Initialize the model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Load prompt parts from the JSON file
with open('prompts.json', 'r') as file:
    data = json.load(file)
    prompt_parts = data['prompt_parts']

# Get user input
userinput = input("Ask a Gardening Question: ")

# Update the prompt parts with the user input
prompt_parts[7] = "Context " + userinput

# Generate content using the model
response = model.generate_content(prompt_parts)
print(response.text)
