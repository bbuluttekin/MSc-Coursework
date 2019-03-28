from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
import re


WORD_RE = re.compile(r"[\w']+")


class WordCountPairs(MRJob):

    def reducer_init(self, key_word="my"):
        self.key_word = key_word

    def mapper_get_words(self, _, line):
        # yield each word in the line
        line = line.split(",")[1]
        words = WORD_RE.findall(line)
        for i in range(len(words) - 1):
            yield ((words[i].lower(), words[i+1].lower()), 1)

    def combiner_count_words(self, word, counts):
        # sum the words we've seen so far
        yield (word, sum(counts))

    def reducer_count_words(self, word, counts):
        # send all (num_occurrences, word) pairs to the same reducer.
        # num_occurrences is so we can easily use Python's max() function.
        top_10 = []
        if "my" == word[0]:
            yield word, sum(counts)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   combiner=self.combiner_count_words),
            MRStep(reducer=self.reducer_count_words)
        ]


if __name__ == "__main__":
    WordCountPairs().run()
