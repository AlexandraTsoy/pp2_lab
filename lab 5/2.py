import re
def text_match(text):
        patterns = 'abb+?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

