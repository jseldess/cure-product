import re
import json
import requests
import unirest

# Create poem with word repetitions
def poem_from_pattern():
    f1 = file('source.txt').read()
    with open('PATTERN-ta.txt', 'w') as f2:
        for word in f1.split():
            if re.search(r'.*sto.*', word):
                return word
                check_pos = word
                access_token = "OpFZKHgToNmshU6LTG6oFc62Mghip1dKibEjsncdEjNIYPeA8M"
                detail = "partOfSpeech"
                try:
                    api_client = WordsAPI.swagger.ApiClient(api_server="https://www.wordsapi.com")
                    words_api = WordsAPI.WordsApi(api_client)
                    response = words_api.details(access_token, check_pos, detail) 
                    pprint(response)

                except Exception, e:
                    print(e)


# poem_from_pattern()

r = unirest.get('https://www.wordsapi.com/words/purchase/partOfSpeech?mashape-key=TgsKSgUKnImshT9ENZXxSoXFdzNTp122HhIjsnqUZA1CJHBW5n', callback = None)

print r.raw_body 

#auth = {'mashape-key': 'skLZFxcCwLmshCinse0aoK4fZd6Sp1S76dNjsnmzgPMEzhrIHz'}
#headers = {'content-type': 'application/x-www-form-urlencoded'}
#r = requests.get('https://www.wordsapi.com/words/purchase/partOfSpeech?mashape-key=skLZFxcCwLmshCinse0aoK4fZd6Sp1S76dNjsnmzgPMEzhrIHz')
#print r.json()



#access_token = "OpFZKHgToNmshU6LTG6oFc62Mghip1dKibEjsncdEjNIYPeA8M"
#word = "variegated"
#detail = "partOfSpeech"


#try:
#    api_client = WordsAPI.swagger.ApiClient(api_server="https://wordsapiv1.p.mashape.com/words/mashape-key=OpFZKHgToNmshU6LTG6oFc62Mghip1dKibEjsncdEjNIYPeA8M")
#    words_api = WordsAPI.WordsApi(api_client)
#    response = words_api.details(access_token, word, detail) 
#    pprint(response)

#except Exception, e:
#    print(e)

# def poem_from_pattern():
#     f1 = file('/Users/jesseseldess/PTRY/The_Offers/Experiments/python/source.txt').read()
#     with open('/Users/jesseseldess/PTRY/The_Offers/Experiments/python/PATTERN-th_wh_ch.txt', 'w') as f2:
#         words_seen = set()
#         for word in f1.split():
#             if word not in words_seen:
#                 if re.search(r'.*th.*', word):
#                     f2.write(word + " ")
#                     words_seen.add(word)
#                 if re.search(r'.*wh.*', word):
#                     f2.write(word + " ")
#                     words_seen.add(word)
#                 if re.search(r'.*ch.*', word):
#                     f2.write(word + "\n")
#                     words_seen.add(word)
#
# poem_from_pattern()
