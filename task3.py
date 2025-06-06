import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK data only once
nltk.download('punkt')
nltk.download('stopwords')


def generate_response(user_input):
    user_input = user_input.lower()

    try:
        words = word_tokenize(user_input)
    except LookupError:
        return "Sorry, I had trouble understanding that."

    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    print("DEBUG - Tokens after filtering:", filtered_words)  # Helps you see what’s being processed

    if "hello" in filtered_words:
        return "Hi there! How can I help you today?"
    elif "name" in filtered_words:
        return "I'm CodBot, your friendly assistant!"
    elif "bye" in filtered_words:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."


print("CodBot: Hello! Type something or type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("CodBot: Bye! Take care.")
        break
    else:
        response = generate_response(user_input)
        print("CodBot:", response)