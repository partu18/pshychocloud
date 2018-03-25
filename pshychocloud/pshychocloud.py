import re
from wordcloud import WordCloud

from constants import (WAPP_EXTRACT_PARTICIPANT_REGEX, REGEX_FLAGS, WHATSAPP,
                       WAPP_EXTRACT_MESSAGE_REGEX, WAPP_PARTICIPANT_WILDCARD,
                       WHOLE_CONV)
from auxiliaries import clean_line


class Pshychocloud(object):
    type_to_participant_regex = {WHATSAPP:WAPP_EXTRACT_PARTICIPANT_REGEX}
    type_to_message_regex = {WHATSAPP:WAPP_EXTRACT_MESSAGE_REGEX}    
    type_to_wildcard = {WHATSAPP:WAPP_PARTICIPANT_WILDCARD}    

    def _read_file(self, _file):
        return open(_file,'r').readlines()

    def _get_participants_regex_from_type(self, type_of_conv):
        return self.type_to_participant_regex[type_of_conv]

    def _get_message_regex_from_type(self, type_of_conv):
        return self.type_to_message_regex[type_of_conv]

    def _get_participant_wildcard_for_type(self, type_of_conv):
        return self.type_to_wildcard[type_of_conv]

    def _get_participants(self, text, type_of_conv):
        '''
            Function to extract partipants from whateve type of file was provided
            using the regex. 
        '''
        regex_string = self._get_participants_regex_from_type(type_of_conv)
        regex = re.compile(regex_string, REGEX_FLAGS)
        participants = set()
        for line in text:
            match = regex.match(line)
            if match:
                participants.add(match.groups()[0])
        return participants


    def _get_words(self, text, type_of_conv, participant=None):
        ''' 
            When no input of parcipnt is provided it means that we shall 
            treat it as a group, therefore we should use the wildcard for
            the type of conversation we're using
        '''
        wildcard = self._get_participant_wildcard_for_type(type_of_conv)
        regex_string = self._get_message_regex_from_type(type_of_conv) %\
                        (participant or wildcard) #FIX THIS!!
        regex = re.compile(regex_string, REGEX_FLAGS)
        words = []
        for line in text:
            match = regex.match(line)
            if match:
                clean_words = clean_line(match.groups()[0])
                words.extend(clean_words.split(' '))
        return words

    def _create_wordcloud(self, text, type_of_conv, participant=None):
        words = self._get_words(text, type_of_conv, participant)
        text_after_filtering_words = " ".join(words)
        return WordCloud().generate(text_after_filtering_words)

    def create_wordclouds(self, _file, type_of_conv):
        text = self._read_file(_file)        
        participants = self._get_participants(text, type_of_conv)
        participants.add(None) #TO force the group wordcloud
        wordclouds = {}
        for participant in participants:
            wordclouds.update({(participant or WHOLE_CONV) :self._create_wordcloud(text, type_of_conv, participant)})
        return wordclouds


