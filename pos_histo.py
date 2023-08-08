# Jeremiah Kent
# 2023-08-07

from nltk import pos_tag
from nltk.probability import FreqDist
from matplotlib import pyplot

class PosHistogram:
    """Generate Histogram of Parts-of-Speech
    
        Instantiate with a list of tokens to be categorized.
        Their parts-of-speech will be mapped, 
        then a frequency distribution of those generated.
    """
    def __init__(self, words):
        parts = pos_tag(words)
        self.fd = FreqDist(pos for _, pos in parts)

    def plot_to_file(self, filename):
        """Generate a plot of the previously-computed histogram and save it to the specified file.

            If the filename includes a valid image type extension, an image of that type will be created.
        """
        fig = pyplot.figure()
        self.fd.plot()
        pyplot.show()
        fig.savefig(filename)
