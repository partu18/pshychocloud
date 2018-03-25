import re

# Spanish stopwords
SPANISH_PREPOSITIONS = ['a','ante','bajo','cabe','con','contra','de','desde','durante','en','entre','hacia','hasta','mediante','para','por','segun','sin','so','sobre','tras','versus','via']
SPANISH_ARTICLES = ['el','la','las','lo','los','le','les','al','un','unos','una','unas']
SPANISH_OTHERS = ['que','cuando','este','se','esto','es','del', 'est', 'te']
SPANISH_STOPWORDS = SPANISH_PREPOSITIONS + SPANISH_ARTICLES + SPANISH_OTHERS


#  Permissions

ONLY_OWNER = 0700

# General

WHOLE_CONV = "whole_conversation"

# Supported message types

WHATSAPP = 'Whatsapp'
SUPPORTED_TYPES = [WHATSAPP]

# Regex

REGEX_FLAGS =  re.IGNORECASE