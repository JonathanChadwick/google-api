import os


def review_to_dict(path): #---> dict
    for review_txt in os.listdir(path):
        with open(review_txt) as file:
            for i, line in enumerate(file):
                #create list of dictionary titles to match with i
                pass
