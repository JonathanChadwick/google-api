import os
import requests

KEYS = ['title', 'name', 'date', 'feedback']
URL = 'http://<corpweb-external-IP>/feedback'
def review_to_dict(path):
    list_of_feedback = []
    for review_txt in os.listdir(path):
        with open(path + review_txt) as file:
            feedback_dict = {
                'title' : '',
                'name' : '',
                'date' : '',
                'feedback' : ''
            }
            for i, line in enumerate(file):
                if i >= 3:
                    feedback_dict['feedback'] += line
                else:
                    feedback_dict[KEYS[i]] = line.strip()
            list_of_feedback.append(feedback_dict)
    return list_of_feedback

def post_feedback(list_of_feedback):
    for feedback_dict in list_of_feedback:
        response = requests.post(URL , data=feedback_dict)
        print(f"status: {response.status()}")





#print(review_to_dict('reviews/'))
