from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")


class MRWordCountStripes(MRJob):

    SORT_VALUES = True

    def __init__(self, *args, **kwargs):
        super(MRWordCountStripes, self).__init__(*args, **kwargs)
        self.w_array = {}
        self.w_combiner = {}
        self.w_reducer = {}
        self.total_count = 0

    def configure_args(self):
        super(MRWordCountStripes, self).configure_args()

        self.add_passthru_arg(
            '--searchword', dest='searchword', default="my", type=str,
            help='Specify the word you want to count.')

    def mapper(self, _, line):
        line = line.split(",")[1]  # Strip away the joke ID
        keyword = None

        for word in WORD_RE.findall(line):
            word = word.lower()

            if keyword is not None:
                if keyword == self.options.searchword:
                    yield word, 1
            keyword = word

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer_init(self):
        self.w_array = {}

    def reducer(self, key, values):
        if key not in self.w_array.values():
            self.w_array[key] = sum(values)
        else:
            self.w_array[key] += sum(values)

        # total_word_count = sum(self.w_array.values())

        # yield key, (sum(values), total_word_count)

    def reducer_final(self):
        total_word_count = sum(self.w_array.values())
        for key, val in self.w_array.items():
            yield key, (val, total_word_count)

    def combined_reducer(self, key, values):
        """
        top10 = {}
        word_count, reducer_count = values

        total_count += reducer_count

        if key not in top10.keys():
            top10[key] = word_count
        else:
            top10[key] += word_count

        for i, j in top10.items():
            yield i, j
            """
        w_val, total_val = values
        yield key, w_val, total_val

    def steps(self):
        return [MRStep(mapper=self.mapper,
                       combiner=self.combiner,
                       reducer_init=self.reducer_init,
                       reducer=self.reducer,
                       reducer_final=self.reducer_final),
                MRStep(reducer=self.combined_reducer)]


if __name__ == "__main__":
    MRWordCountStripes.run()
