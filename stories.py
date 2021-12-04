"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""
        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# 2 story templates to choose from 


story1 = Story(
    'history',
    'A History Tale',
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    'fiction',
    'A Fiction Tale',
    ['place', 'noun', 'verb', 'adjective', 'plural_noun'],
    '''There once was a {adjective} {noun} who lived in a {place}, called fantasy 
    {place}. There lived a giant monster who enjoyed to {verb} {plural_noun}.'''
)

story3 = Story(
    'winter',
    'Winter Story',
    ['noun', 'adjective', 'verb'],
    '''Oh the {noun} outside is {adjective}, but the {noun} is so {adjective}. And
    since we have no place to {verb}. Let It Snow! Let It Snow! Let It Snow!'''
)

# create dictionary of {code: story, code:story}
stories = {s.code: s for s in [story1, story2, story3]}