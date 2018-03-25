from wordcloud import WordCloud
from constants import WHOLE_CONV, WHATSAPP
from WAPPMessageAnalyzer import WAPPMessageAnalyzer

class Pshychocloud(object):
    type_to_analyzer = {WHATSAPP:WAPPMessageAnalyzer}    

    def _read_file(self, _file):
        return open(_file,'r').readlines()

    def _get_analyzer(self, type_of_conv):
        return self.type_to_analyzer[type_of_conv]

    def _create_wordcloud(self, text, analyzer, participant=None):
        words = analyzer.get_words(text, participant)
        text_after_filtering_words = " ".join(words)
        return WordCloud().generate(text_after_filtering_words)

    def create_wordclouds(self, _file, type_of_conv):
        text = self._read_file(_file)    
        analyzer = self._get_analyzer(type_of_conv)()
        participants = analyzer.get_participants(text)
        participants.add(None) #TO force the group wordcloud
        wordclouds = {}
        for participant in participants:
            wordclouds.update({(participant or WHOLE_CONV) :self._create_wordcloud(text, analyzer, participant)})
        return wordclouds


