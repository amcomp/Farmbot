# Farmbot
Will use Gemini API with Context about my garden, to answer questions I have.

# To Get Started
## create a ".env" file, with your API key in it. Name the key "api"
## run pip install -r requirements.txt

# Generation_Config
## Tune the Output creativity of the model

# Prompts
## This is a structured model, allowing you to give it context and inform the model how you would like it to respond. Add more prompts, by copying and pasting the context/output lines, then writing in two new prompt lines, the last two need the be blank, as they are now, this is where the use input goes later in the code.

# Safety_Settings
## Tune the model's safety settings for if it should allow it to respond to certain kinds of speech. This prompt has it turned all the way up, because its intended for gardening questions. 

# Description of function
## Opening main.py then running, the user will be prompted to give an input (in this case a question about gardening). The Gemini AI API will be queried and then respond back with an answer. The AI model is given context with the prompts.json file.