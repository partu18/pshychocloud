from MessageAnalyzer import MessageAnalyzer

class WAPPMessageAnalyzer(MessageAnalyzer):
    WAPP_DATE_REGEX = "[0-9]{1,2}/[0-9]{1,2}/[0-9]{1,2}"
    WAPP_TIME_REGEX = "[0-9]{1,2}:[0-9]{1,2}"
    WAPP_EXTRACT_PARTICIPANT_REGEX = r"{date}\s*,\s*{time}\s*-\s*(.+?)\s*:\s*"\
                                        .format(
                                            date=WAPP_DATE_REGEX,
                                            time=WAPP_TIME_REGEX    
                                        ) 
    WAPP_EXTRACT_MESSAGE_REGEX = r"{date}\s*,\s*{time}\s*-\s*{participant}\s*:\s+(.+?)$"\
                                    .format(
                                       date=WAPP_DATE_REGEX,
                                       time=WAPP_TIME_REGEX,
                                       participant='%s' #UGLY UGLY UGLY!
                               )
    WAPP_PARTICIPANT_WILDCARD = "[^:]+"
    
    extract_message_regex = WAPP_EXTRACT_MESSAGE_REGEX
    participant_wildcard = WAPP_PARTICIPANT_WILDCARD
    extract_participant_regex = WAPP_EXTRACT_PARTICIPANT_REGEX

    def _get_clean_words_from_line(self, line):
        '''
            Remove Whatsapp automatic generated messages    
        '''
        omitted_file = '<Archivo omitido>'.lower()
        filtered_line =  '' if omitted_file in line else line
        return super(WAPPMessageAnalyzer, self)._get_clean_words_from_line(filtered_line)

        