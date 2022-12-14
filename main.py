
#! /usr/bin/env python3

import os
import requests

KEYS = ['title', 'name', 'date', 'feedback']
URL = 'http://34.70.137.218/feedback/'
PATH_TO_REVIEWS = '/data/feedback/'

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
    response = requests.post(URL , data=list_of_feedback)
    if not response.ok:
        raise Exception("GET failed with status code {}".format(response.status_code))
    print(f"status: {response.status_code}, text = {response.text}")


def main():
    list_of_feedback = review_to_dict(PATH_TO_REVIEWS)
#    print(list_of_feedback)
    for feedback_dict in list_of_feedback:
        post_feedback(feedback_dict)
    print("finished")

main()
