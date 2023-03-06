import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Diferent models
# print(openai.Model.list()

# Select the type of chatbot
system_message = input("What type of chatbot do you want me to be? : " )
print("-----------------------------------")
messages = []
print("BOT : Hello! I'm a chatbot. Ask me a question or type 'quit' to exit.")
# Loop until the user types "quit"
while True:
    # Add the system message to the list of messages
    messages.append({"role": "system", "content": system_message})

    # Ask the user for their message
    message = input("\n" + "ME : ")

    # If the user typed "quit", break out of the loop
    if message == "quit":
        print("Goodbye!")
        break

    # Add the user's message to the list of messages
    messages.append({"role": "user", "content": message})

    try:
        # Call the chatbot API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.6,
        )

        # Extract the response from the API's output
        reply = response.choices[0].text.strip()
    except Exception as e:
        # If there was an error calling the API, show an error message
        print("Oops! Something went wrong:", str(e))
        continue

    # Add the chatbot's response to the list of messages and display it to the user
    messages.append({"role": "bot", "content": reply})
    print(" ")
    print(f'BOT : {reply}')
          
        
    

