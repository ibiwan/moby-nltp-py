# Jeremiah Kent
# 2023-08-07

from nltk.util import ngrams
from collections import Counter
import csv

class TrigramChart:
    """Compute trigrams from a wordlist, and output to a CSV chart.

        Instantiate with an ordered list of tokens from a corpus.
        Their trigrams (consecutive sets of 3) will be generated, then the counts of each computed. 
    """
    def __init__(self, words):
        trigrams = ngrams(words, 3)
        self.trigram_counts = Counter(gram for gram in trigrams)
    
    def writeCsv(self, filename):
        """Write the pre-computed counts and trigrams to a CSV file with the provided name.

            Whitespace padding will be added to make the CSV visually scannable, and should not affect parsing.
        """
        with open(filename, 'w', newline='') as csvfile:
            csvout = csv.writer(csvfile, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            # This function formats the counts to fit under "Occurrences", then add a space before and after the delimiter.
            def row(a, b): csvout.writerow([a.rjust(11, ' ') + ' ', ' ' + b])

            # Write header row
            row('Occurrences', 'Trigram')
            for [gram, count] in self.trigram_counts.most_common():
                # Write each data row
                row(str(count), " ".join(gram))
