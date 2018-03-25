from wordcloud import WordCloud
from pshychocloud.pshychocloud import Pshychocloud
from pshychocloud.auxiliaries import clean_line, remove_space_as_word
from pshychocloud.constants import WAPP_EXTRACT_PARTICIPANT_REGEX, WHATSAPP


def test_wordcloud():
    text = '''
        This tool was created because we wanted random text for our web
        designs. When we show a design to a client we want to have some text 
        that doesn't mean anything in particular just to indicate that "here
        is where the text will be". So why shouldn't we just copy-paste a
        single sentence and get a block of text ? Have a look at the following
        examples:
        This is some dummy text. This is some dummy text. This is some dummy
        text. This is some dummy text. This is some dummy text. This is some
        dummy text.	This is some dummy text. This is some dummy text. This is
        some dummy text. This is some dummy text.
        This is a single sentence repeated a few times.
        Is post each that just leaf no. He connection interested so we an
        sympathize advantages. To said is it shed want do. Occasional 
        middletons everything so to. Have spot part for his quit may. Enable
        it is square my an regard. Often merit stuff first oh up hills as he.
        And this is some text from our generator.
        As you can easily notice the second block of text looks more realistic
        . This way when you show a design to a client you can have a result
        that resembles the final product. However you can also use this text
        when you need meaningless text in the background of a design for a
        poster, t-shirt or whatever else you please. 
        Why not use lorem ipsum ? 
        Lorem ipsum is the most common form of "Greeking". However more and 
        more people are sick and tired of using the same sample text over 
        and over again. Also lorem ipsum is in latin and it may not always 
        be the best choice. We tried to have text generated in some of the 
        most widely used languages but if you are in desperate need of random
        text in your own language, send us an email and we'll add it here. 
        I love it, how can I help ?
        It's easy. Tell a friend about us or if you are super kind place a
         link to us in your website or blog. Thank you :)
        Geek talk.
        Our random text generator was made in PHP and MySQL. 
        '''

    cleaned_text = [clean_line(line) for line in text]
    words = text.split(" ")
    cleaned_words = remove_space_as_word(words)
    
    wordcloud = WordCloud().generate(text)
    image = wordcloud.to_image()
    image.show()

def test_parsing_whatsapp_conversation():
    pshychocloud = Pshychocloud()
    type_of_conv = WHATSAPP
    text = pshychocloud._read_file("wapp_example.txt")
    expected = {"Giovanni", "Betinho"}
    participants = pshychocloud._get_participants(text,type_of_conv)
    assert  expected == participants, "Test fail: Expecting: {}, got: {} "\
                                        .format(expected, participants)

def test_get_words_from_participant():
    pshychocloud = Pshychocloud()
    type_of_conv = WHATSAPP
    text = pshychocloud._read_file("wapp_example.txt")
    participant = 'Giovanni'
    expected = ['hey','man','who','are','u','u','ther','it','is','important','Mark','is','here']
    words = pshychocloud._get_words(text, type_of_conv, participant)
    assert  expected == words, "Test fail: Expecting: {}, got: {} "\
                                        .format(expected, words)

def test_get_words_from_group():
    pshychocloud = Pshychocloud()
    type_of_conv = WHATSAPP
    text = pshychocloud._read_file("wapp_example.txt")
    participant = None
    expected = ["hey","man","who","are","u","u","ther","it","is","important","yes","what","happened","Mark","is","here","Holly","shit","Are","you","fucking","kidding","me","I","can","not","belive","it","Photo","I","need","a","photo"]
    words = pshychocloud._get_words(text, type_of_conv, participant)
    assert  expected == words, "Test fail: Expecting: {}, got: {} "\
                                        .format(expected, words)



    


if __name__ == "__main__":
    #test_wordcloud()
    test_parsing_whatsapp_conversation()
    test_get_words_from_participant()
    test_get_words_from_group()    
    print "All tests ran successfully"
    