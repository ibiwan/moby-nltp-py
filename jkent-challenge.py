# UAz D2L Python Challenge - Problem 1
# Jeremiah Kent
# 2023-08-07
# Per https://community.d2l.arizona.edu/d2l/le/content/1298610/viewContent/14905884/View



from file_tokens import FileTokens
from trigram_chart import TrigramChart
from pos_histo import PosHistogram

# Load tokens from text corpus file provided
words = FileTokens('dialog1.txt').tokens()

# Generate and save trigrams from token list
TrigramChart(words).writeCsv('Trigrams.csv')

# Generate and save parts-of-speech histogram plot from token list
PosHistogram(words).plot_to_file('Speech.jpg')
