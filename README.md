# AI Text-Speech & Speech-Text Chatbot

* Combines speech & text recognition system with an AI algorithm.
* It is uses Natural Language Processing, NLP.

```
To commence this project, I'll start by installing the required packages such as;

1. SpeechRecognition - to allow conversion from speech to text
2. gTTs - (Google Text to Spech library) to convey text to speech and also speak it.
3. transformers - language model
4. tensorflow - deep learning/ml library
```

# How to install

* Make sure that python and virtual environment is installed. In my case, i'm using PyCharm.

* or

* Use Google Colab

### Now install the requirements

```
pip install -r requirements.txt
```

### Microsoft DialoGPT
```
This project also used Microsoft DialoGPT; a SOTA large-scale pretrained 
dialogue response generation model for multiturn conversations.

Source: https://huggingface.co/microsoft/DialoGPT-medium & https://github.com/microsoft/DialoGPT

Note: This model is no longer maintained and you might encounter issues.
```

## Project Summary

```
Overall, this code defines a ChatBot class with several methods that allow it to convert speech 
to text, convert text to speech, check whether its name is mentioned in the input text, and return 
the current time. When run, the code creates an instance of the ChatBot class and uses its methods to 
interact with the user.

The wake_up method returns True if the chatbot's name appears in the text attribute of the ChatBot instance,
and False otherwise.

The action_time method returns the current time in the format 'HH:MM'.

The last code block at the end runs the chatbot. It creates an instance of the
ChatBot class, named ai, and enters a loop that listens for speech, processes it, and responds with 
text-to-speech. The chatbot can recognise when it is being called by its name, respond with the 
current time when asked, and thank the user when appropriate. It can also exit the loop and shut down
when told to do so. The chatbot uses the transformers library and the DialoGPT model to generate 
responses to other kinds of input.

Thanks to ChatGPT for the helping out with the summary.
```

# Credit

* Thanks to [Arnab Mondal](https://github.com/arnabm14/Dev_AIChatbot_NLP), I made some adjustments.
