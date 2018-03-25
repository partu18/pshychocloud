import re

# Permissions
ONLY_OWNER = 0700

# General
WHOLE_CONV = "whole_conversation"

# Supported message types

WHATSAPP = 'Whatsapp'
SUPPORTED_TYPES = [WHATSAPP]

# Regex

REGEX_FLAGS =  re.IGNORECASE

# For Whatsapp 
WAPP_DATE_REGEX = "[0-9]{1,2}/[0-9]{1,2}/[0-9]{1,2}"
WAPP_TIME_REGEX = "[0-9]{1,2}:[0-9]{1,2}"
WAPP_EXTRACT_PARTICIPANT_REGEX = r"{date}\s*,\s*{time}\s*-\s*(.+?)\s*:\s*"\
        .format(date=WAPP_DATE_REGEX,
                time=WAPP_TIME_REGEX
        )
WAPP_EXTRACT_MESSAGE_REGEX = r"{date}\s*,\s*{time}\s*-\s*{participant}\s*:\s+(.+?)$"\
                                .format(
                                       date=WAPP_DATE_REGEX,
                                       time=WAPP_TIME_REGEX,
                                       participant='%s' #UGLY UGLY UGLY!
                               )
WAPP_PARTICIPANT_WILDCARD = "[^:]+"