import os
from pshychocloud.pshychocloud import Pshychocloud
from argparse import ArgumentParser
from pshychocloud.constants import SUPPORTED_TYPES, ONLY_OWNER


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-f', dest='filepath',help="Path to file where the conversation is stored")
    parser.add_argument('-t', dest='client_type', choices= SUPPORTED_TYPES, help="Type of client (use --help to se availables)")
    parser.add_argument('-o', dest='output', help="Path to store the output")
    args = parser.parse_args()
    if not args.filepath or not args.client_type or not args.output:
        parser.error("Missing Arguments")

    wordclouds = Pshychocloud().create_wordclouds(args.filepath, args.client_type)

    if not os.path.exists(args.output):
        os.makedirs(args.output, ONLY_OWNER )

    for name, wordcloud in wordclouds.iteritems():
        img = wordcloud.to_image()
        img.save("{}/{}.png".format(args.output, name))
    
        

