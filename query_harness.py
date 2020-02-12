import json
import requests
import sys
import os

URL_PROD = 'https://bifrost.apartmentlist.com/v4/search'

write_file = open("responses.txt", "a+")


def search(payload, scorer=None):
    payload.update({'scorer': scorer})
    return requests.post(
            URL_PROD,
            data=json.dumps(payload),
            headers={
                'content-type': 'application/json', 'Authorization': 'Token token={}'.format(
                    os.environ['TOKEN']
                )
            }
        )


with open(sys.argv[1]) as read_file:
    line_count = 0
    for line in read_file:
        responses = []
        query = json.loads(line)
        scorers = [None] + sys.argv[2:]

        # call search endpoints scorers
        for scorer in scorers:
            response = search(query, scorer)

            if response.status_code == 200:
                responses.append({
                    'payload': response,
                    'variation': scorer if scorer else 'control'
                })
            else:
                print(response.text)
                break
        if len(responses) == len(scorers):
            print(line_count)
            for response in responses:
                write_file.write('{}\n{}\n'.format(
                    response['variation'], response['payload'].text)
                )
        else:
            print('error on ' + line_count)
        line_count += 1
