from pshychocloud import Pshychocloud
from argparse import ArgumentParser
from constants import SUPPORTED_TYPES


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-f', dest='filepath',help="Path to file where the conversation is stored")
    parser.add_argument('-t', dest='client_type', choices= SUPPORTED_TYPES, help="Type of client (use --help to se availables)")
    args = parser.parse_args()
    if not args.filepath or not args.client_type:
        parser.error("Missing Arguments")

    wordclouds = Pshychocloud().create_wordclouds(args.filepath, args.client_type)

    for name, wordcloud in wordclouds.iteritems():
        img = wordcloud.to_image()
        img.save("{}.png".format(name))
    
        

