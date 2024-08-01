import requests
import html
from question_model import Questions
parameter = {
    "amount": 20,
    "category": 17,
    "type": "boolean"
 }

response = requests.get(url= "https://opentdb.com/api.php", params= parameter)
response.raise_for_status()
data = response.json()

question_data = data["results"]
question_bank = []
for quizebook in question_data:
    text = html.unescape(quizebook["question"])
    answer= quizebook["correct_answer"]
    new_question = Questions(text,answer)
    question_bank.append(new_question)

