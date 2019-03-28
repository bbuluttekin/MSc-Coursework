from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")


class MRWordCountPairs(MRJob):

    SORT_VALUES = True

    def configure_args(self):
        super(MRWordCountPairs, self).configure_args()

        self.add_passthru_arg(
            '--searchword', dest='searchword', default="my", type=str,
            help='Specifiy the word you want to count.')

    def mapper_words(self, _, line):
        line = line.split(",")[1]  # Strip away the joke ID
        keyword = None

        for word in WORD_RE.findall(line):
            word = word.lower()

            if keyword is not None:
                if keyword == self.options.searchword:
                    yield (keyword, '*'), 1
                    yield (keyword, word), 1

            keyword = word

    def combiner_words(self, key, count):
        yield key, sum(count)

    def reducer_words(self, key, count):
        counts = sum(count)

        keyword, next_word = key

        if next_word == "*":
            yield keyword, ("A:", counts)  # Uses sorting A comes before B
        else:
            yield keyword, ("B:", (next_word, counts))

    def ratio_calculation(self, prev_word, value):

        total_value = None
        top10 = {}

        for value, data in value:
            if value == 'A:':
                total_value = data
            else:
                assert value == 'B:'
                word, count = data
                # A comes before B, so total_value should already be set
                percent = count / total_value

                if len(top10) < 10:
                    top10[(prev_word, word)] = percent
                else:
                    if percent > min(top10.values()):
                        top10 = {key: val for key, val in top10.items()
                                 if val != min(top10.values())}
                        top10[(prev_word, word)] = percent
                # yield (prev_word, word), percent
        top10 = sorted(top10.items(), key=lambda x: -x[1])
        for key in top10:
            # yield the key value pairs which is a tuple now
            yield key[0], key[1]

    def steps(self):
        return [MRStep(mapper=self.mapper_words,
                       combiner=self.combiner_words,
                       reducer=self.reducer_words),
                MRStep(reducer=self.ratio_calculation)]


if __name__ == "__main__":
    MRWordCountPairs.run()
