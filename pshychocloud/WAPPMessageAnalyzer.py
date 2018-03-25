from constants import (WAPP_EXTRACT_PARTICIPANT_REGEX,
                       WAPP_EXTRACT_MESSAGE_REGEX,
                       WAPP_PARTICIPANT_WILDCARD)
from MessageAnalyzer import MessageAnalyzer

class WAPPMessageAnalyzer(MessageAnalyzer):
    extract_message_regex = WAPP_EXTRACT_MESSAGE_REGEX
    participant_wildcard = WAPP_PARTICIPANT_WILDCARD
    extract_participant_regex = WAPP_EXTRACT_PARTICIPANT_REGEX