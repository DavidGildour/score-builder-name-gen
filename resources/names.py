import random
from flask_restful import Resource

from words.adjectives import adjectives
from words.nouns import nouns


class GenerateName(Resource):
    @classmethod
    def get(cls):
        return {
            'message': 'Here ya go!',
            'content': f'{random.choice(adjectives)} {random.choice(nouns)}'
        }