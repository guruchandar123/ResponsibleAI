import openai

def check_toxic_content(text):
    response = openai.Moderation.create(input=text)
    return response["results"][0]

user_input = "Sample text"
results = check_toxic_content(user_input)

if results["flagged"]:
    print([k for k, v in results["categories"].items() if v])
