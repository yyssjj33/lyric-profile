from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from textblob import TextBlob

lyrics = ["When I look into your eyes\nIt's like watching the night sky\nOr a beautiful sunrise\nThere's so much they hold\n\nAnd just like them old stars\nI see that you've come so far\nTo be right where you are\nHow old is your soul?\n\nI won't give up on us\nEven if the skies get rough\nI'm giving you all my love\nI'm still looking up\n\nAnd when you're needing your space\nTo do some navigating\n...\n\n******* This Lyrics is NOT for Commercial use *******", "I've been all around the world\nI've been a new sensation\nBut it doesn't really matter\nIn this ge-generation\nThe sophomore slump is an uphill battle\nAnd someone said it ain't my scene\n\n'Cause they need a new song\nLike a new religion\nMusic for the television\nI can't do the long division\nSomeone do the math\n\nFor the record label puts me on the shelf up in the freezer\nGot to find another way to live the life of leisure\nSo I drop my top, mix and I mingle\nIs everybody ready for the single and it goes\n\nAh, la, la, la, la\nNow listen closer to the verse I lay\nAh, la, la, la, la\nIt's all about the wordplay\nAh, la, la, la, love\nThe wonderful thing it does\nBecause, because\nI am the wizard of ooh's and ah's and fa-la-la's\nYeah, the Mister A to Z\nThey say I'm all about the wordplay\n\n...\n\n******* This Lyrics is NOT for Commercial use *******", "I picture something is beautiful\nIt's full of life and it is all blue\nI've seen the sunset on the beach, yeah\nIt makes me feel calm, when I'm calm\n\nI feel good (Good)\nAnd when I feel good I sing (Sing)\nAnd the joy it brings makes me feel good (Good)\nAnd when I feel good I sing (Sing)\nAnd the joy it brings\n\nI see birds fly across the sky, yeah\nAnd everyone's heart flies together\nFood is frying and people smiling\nLike there is no other way...\nTo feel good (Good)\n\nAnd when I feel good I sing (Sing)\n...\n\n******* This Lyrics is NOT for Commercial use *******", "I picture something is beautiful\nIt's full of life indeed and all blue\nI've seen the sunset on the beach\nYeah, it makes me feel calm\nAnd when I'm calm\n\nI feel good\nWhen I feel good I sing\nAnd the joy it brings make it feel good\nAnd when I feel good, I sing\nAnd the joy it brings\n\nI see birds fly across the sky\nYeah, and everyone's heart fly together\nFoot is flying and people smiling\nThere is no other way to feel good\n\nI feel good\nWhen I feel good I sing\nAnd the joy it brings make it feel good\nAnd when I feel good I sing\nAnd the joy it brings\n\nCome on alone\nI know you really want to feel our song\nWe got some life to bring\nWe got some joy in this thing\n\nSo come on alone\n...\n\n******* This Lyrics is NOT for Commercial use *******", "I picture something is beautiful\nIt's full of life and it is all blue\nI've seen the sunset on the beach, yeah\nIt makes me feel calm, when I'm calm\n\nI feel good (Good)\nAnd when I feel good I sing (Sing)\nAnd the joy it brings makes me feel good (Good)\nAnd when I feel good I sing (Sing)\nAnd the joy it brings\n\nI see birds fly across the sky, yeah\nAnd everyone's heart flies together\nFood is frying and people smiling\nLike there is no other way...\nTo feel good (Good)\n\nAnd when I feel good I sing (Sing)\n...\n\n******* This Lyrics is NOT for Commercial use *******", "I picture something is beautiful\nIt's full of life and it is all blue\nI've seen the sunset on the beach, yeah\nIt makes me feel calm, when I'm calm\n\nI feel good (Good)\nAnd when I feel good I sing (Sing)\nAnd the joy it brings makes me feel good (Good)\nAnd when I feel good I sing (Sing)\nAnd the joy it brings\n\nI see birds fly across the sky, yeah\nAnd everyone's heart flies together\nFood is frying and people smiling\nLike there is no other way...\nTo feel good (Good)\n\nAnd when I feel good I sing (Sing)\n...\n\n******* This Lyrics is NOT for Commercial use *******", "I picture something is beautiful\nIt's full of life and it is all blue\nI've seen the sunset on the beach, yeah\nIt makes me feel calm, when I'm calm\n\nI feel good (Good)\nAnd when I feel good I sing (Sing)\nAnd the joy it brings makes me feel good (Good)\nAnd when I feel good I sing (Sing)\nAnd the joy it brings\n\nI see birds fly across the sky, yeah\nAnd everyone's heart flies together\nFood is frying and people smiling\nLike there is no other way...\nTo feel good (Good)\n\nAnd when I feel good I sing (Sing)\n...\n\n******* This Lyrics is NOT for Commercial use *******", "I picture something is beautiful\nIt's full of life and it is all blue\nI've seen the sunset on the beach, yeah\nIt makes me feel calm, when I'm calm\n\nI feel good (Good)\nAnd when I feel good I sing (Sing)\nAnd the joy it brings makes me feel good (Good)\nAnd when I feel good I sing (Sing)\nAnd the joy it brings\n\nI see birds fly across the sky, yeah\nAnd everyone's heart flies together\nFood is frying and people smiling\nLike there is no other way...\nTo feel good (Good)\n\nAnd when I feel good I sing (Sing)\n...\n\n******* This Lyrics is NOT for Commercial use *******", "Let's drive out to the desert at midnight\nTo dance in the dust of our headlights\nAnd score some good seats for the sunrise\nAnd dress up in clothes we don't mind getting messed up\nWhen no one would know how to get us\nWe don't need the map, we'll just drive, drive, drive\n\nI wanna get lost with you\nAnd hideout out under the light of the moon\nI wanna get lost with you\nAnd see what it's like to spend the whole night\nWith you, just you\nYou, just you\n\nWe can head North over the oceans of turquoise\nWell after a while there'll be no noise\nExcept for the sound of our heartbeats beating on\nAnd we'll stand in the canyon alone\n...\n\n******* This Lyrics is NOT for Commercial use *******", "Wake up everyone\nHow can you sleep at a time like this\nUnless the dreamer is the real you\nListen to your voice\nThe one that tells you to taste past the tip of your tongue\nLeap and the net will appear\n\nI don't wanna wake before\nThe dream is over\nI'm gonna make it mine\nYes I... I know it\nI'm gonna make it mine\nYes I'll make it all mine\n\nI keep my life on a heavy rotation\nRequesting that it's lifting you up\n...\n\n******* This Lyrics is NOT for Commercial use *******"]


def remove_water_mark(lyric):
    if lyric is None:
        return ""
    return lyric.replace("This Lyrics is NOT for Commercial use", "")


def clean(lyrics):

    trunck_lyrics = map(remove_water_mark, lyrics)

    all = "".join(trunck_lyrics)
    """tokenize"""
    tokens = word_tokenize(all)
    """stemming words"""
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in tokens]
    """remove punctuation"""
    words = [word for word in stemmed if word.isalpha()]
    """remove stop words"""
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]

    return " ".join(words)


def analyse(lyrics):
    words = clean(lyrics)
    analysis = TextBlob(words)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


if __name__ == '__main__':
    res = analyse(clean(lyrics))

    print(res)

