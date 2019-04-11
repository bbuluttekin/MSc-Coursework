from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")


class MRWordCountStripes(MRJob):

    SORT_VALUES = True

    def configure_args(self):
        super(MRWordCountStripes, self).configure_args()

        self.add_passthru_arg(
            '--searchword', dest='searchword', default="my", type=str,
            help='Specify the word you want to count.')

    def mapper_words(self, _, line):
        line = line.split(",")[1]  # Strip away the joke ID
        keyword = None

        for word in WORD_RE.findall(line):
            word = word.lower()

            if keyword is not None:
                if keyword == self.options.searchword:
                    yield word, 1

            keyword = word

    def combiner_words(self, key, count):
        yield key, sum(count)

    def reducer_words(self, key, count):
        yield None, (key, sum(count))  # Key value pairs added to array.

    def ratio_calculation(self, _, word_count_pair):
        top10 = {}
        total_count = 0  # Total value of word my calculated from array.

        for key, value in word_count_pair:
            total_count += value

            if len(top10) < 10:
                top10[key] = float(value)
            else:
                if value > min(top10.values()):
                    top10 = {k: v for k, v in top10.items()
                             if v != min(top10.values())}
                    top10[key] = float(value)

        top10 = sorted(top10.items(), key=lambda x: -x[1])
        for k in top10:
            yield (self.options.searchword, k[0]), (k[1] / total_count)

    def steps(self):
        return [MRStep(mapper=self.mapper_words,
                       combiner=self.combiner_words,
                       reducer=self.reducer_words),
                MRStep(reducer=self.ratio_calculation)]


if __name__ == "__main__":
    MRWordCountStripes.run()
