# 11-2023-OpenAI-gradio-DEMO

OpenAI API Call via Gradio
This repository contains a simple example of how to use the OpenAI API via Gradio. Gradio is a Python library that allows you to quickly create customizable UI components around your machine learning models.

Table of Contents
Installation

Usage

Contributing

License

Installation
To use this repository, you need to have Python 3.6 or later installed on your machine. You can install the required Python packages using pip:

bash
Copy code
pip install gradio openai
Usage
The openai_chat function in the main.py file is the main function that interacts with the OpenAI API. It takes a message and the chat history as input, generates a response from the OpenAI API, and returns the updated chat history.

The main.py file also contains a Gradio interface that allows you to chat with the OpenAI chat model. The Gradio interface displays the chat history and allows you to input new messages.

To run the Gradio interface, simply execute the main.py file:

bash
Copy code
python main.py
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
