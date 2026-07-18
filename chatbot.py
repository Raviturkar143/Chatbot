intents = {

    ("hi","hello","hey"): "Hello! How can I help you?",

    ("bye","goodbye","see you"):
    "Goodbye!",

    ("sql","oracle","mysql"):
    "SQL is a language used to manage databases.",

    ("python","py"):
    "Python is widely used for automation and AI.",

    ("spark","pyspark"):
    "Apache Spark is used for big data processing."

}

def get_response(message):

    message = message.lower()

    for keywords,response in intents.items():

        for word in keywords:

            if word in message:
                return response

    return "Sorry, I couldn't understand."