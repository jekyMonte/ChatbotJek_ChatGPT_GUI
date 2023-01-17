# ChatbotJek_ChatGPT_GUI

ChatbotJek
is a simple chatbot built using Python and the OpenAI API. The chatbot uses the OpenAI API to generate responses to user input. The user interface is built using the customtkinter library, which is a wrapper for the tkinter library.

Getting Started
To run the chatbot, you will need to install the following libraries:

customtkinter
openai
You can install these libraries using pip by running the following command:

```bash
pip install customtkinter openai
```

You will also need to sign up for an API key from OpenAI. Once you have an API key, you will need to add it to the api_key.py file.

To run the chatbot, simply run the following command:

```bash
python chatbotjek.py
```

The chatbot will launch and you can begin chatting with it. Pressing the enter key or clicking the send button will send your message to the chatbot, which will generate a response.

The appearance of the chatbot can be customized by changing the appearance mode and color theme in the chatbotjek.py file. The possible values for the appearance mode are "Dark" or "Light", and the possible values for the color theme are "green", "blue", "orange", "red", "purple" and "brown"

Note
The customtkinter library is a custom library created by [TomSchimansky](https://github.com/TomSchimansky/CustomTkinter) that is not widely known, it is not a part of the standard library, so it has to be installed manually.
It is a simple wrapper of tkinter which makes it more easy to use and more customizable

Also, it is recommended to encrypt the api_key and decrypt it when the program is running for security reason.
