import re
from auxiliaries import clean_line
from constants import REGEX_FLAGS

class MessageAnalyzer(object):
    def get_words(self, text, participant=None):
        ''' 
            When no input of parcipnt is provided it means that we shall 
            treat it as a group, therefore we should use the wildcard for
            the type of conversation we're using
        '''
        wildcard = self.participant_wildcard
        regex_string = self.extract_message_regex % (participant or wildcard) #FIX THIS!!
        regex = re.compile(regex_string, REGEX_FLAGS)
        words = []
        for line in text:
            match = regex.match(line)
            if match:
                clean_words = clean_line(match.groups()[0])
                words.extend(clean_words.split(' '))
        return words

    def get_participants(self, text):
        '''
            Function to extract partipants from whateve type of file was provided
            using the regex. 
        '''
        regex_string = self.extract_participant_regex
        regex = re.compile(regex_string, REGEX_FLAGS)
        participants = set()
        for line in text:
            match = regex.match(line)
            if match:
                participants.add(match.groups()[0])
        return participants

