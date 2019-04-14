from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[0-9]+")


class MRPagerankSimple(MRJob):

    SORT_VALUES = True

    def configure_args(self):
        super(MRPagerankSimple, self).configure_args()

        self.add_passthru_arg(
            '--iterations', dest='iterations', default=5, type=int,
            help='Choose number of iteration')

        self.add_passthru_arg(
            '--damping-factor', dest='damping_factor', default=0.85,
            type=float,
            help='Choose the damping factor value')

    def initial_process(self, _, line):
        """
        Maps node for outgoing links from origin_node to to_node
        """
        nodes = WORD_RE.findall(line)
        if(len(nodes) == 2):
            origin_node = nodes[0]
            to_node = nodes[1]
            yield origin_node, to_node

    def initialize_pagerank(self, origin_node, adj_list):
        """
        Initialize all adjacency matrix nodes to be sum up un later stage
        """
        adj_dict = {}
        for item in adj_list:
            adj_dict[item] = 1
        initial_pagerank = 1 / len(adj_dict)
        adj_dict = {k: initial_pagerank for k in adj_dict}

        for i in adj_dict:
            yield i, adj_dict[i]

    def combine_ranks(self, node, initial_rank):
        """
        Sums up initial incoming link pagerank values from other nodes
        """
        yield node, (1., sum(initial_rank))

    def iterate_pagerank(self, node, ranks):
        """
        Iteration function for converging the pagerank values
        """
        new_val, init_val = list(ranks)[0]
        new_val = (new_val * init_val * self.options.damping_factor) + \
            (1 - self.options.damping_factor)
        yield node, (new_val, init_val)

    def filter_step(self, node, ranks):
        """
        Utility function for mapping all nodes in one key to reduce them to same reducer
        """
        new_val, init_val = list(ranks)[0]
        yield None, (node, new_val)

    def final_step(self, _, pairs):
        """
        Final function for calculating top 10 pagerank nodes
        """
        top10 = {}
        for item in pairs:
            if len(top10) < 10:
                top10[item[0]] = item[1]
            else:
                if item[1] > min(top10.values()):
                    top10 = {key: val for key, val in top10.items()
                             if val != min(top10.values())}
                    top10[item[0]] = item[1]
        top10 = {w: top10[w]
                 for w in sorted(top10, key=top10.get, reverse=True)}

        for k, v in top10.items():
            yield k, v

    def steps(self):
        steps = [MRStep(mapper=self.initial_process,
                        reducer=self.initialize_pagerank),
                 MRStep(reducer=self.combine_ranks)]
        # Increase number of loops based on iteration number
        for i in range(self.options.iterations):
            steps.append(MRStep(reducer=self.iterate_pagerank))
        steps.append(MRStep(reducer=self.filter_step))
        steps.append(MRStep(reducer=self.final_step))
        return steps


if __name__ == "__main__":
    MRPagerankSimple.run()
