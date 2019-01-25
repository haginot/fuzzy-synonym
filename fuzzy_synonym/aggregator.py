from typing import List
import pandas as pd


class Aggregator:
    def __init__(self):
        self.raw_tags = None
        self.unique_tags = None
        self.tags_counts_series = None
        self.observed_tagged_length = None
        self.count_vector = None
        self.count_vector_df = None
        self.tags_weighted_counts = None

    def fit(self, tags: List[List[str]]):
        self.raw_tags = tags
        self.unique_tags = set().union(*tags)
        self.tags_counts_series = pd.Series([tag for tags in self.raw_tags for tag in tags]).value_counts()
        self.observed_tagged_length = pd.Series([len(t) for t in self.raw_tags], name='length')
        self.count_vector = [[s in t for s in self.unique_tags] for t in self.raw_tags]
        self.count_vector_df = pd.DataFrame(self.count_vector, columns=list(self.unique_tags))
        self.tags_weighted_counts = [(self.tags_counts_series.loc[t]/self.observed_tagged_length[self.count_vector_df.loc[:, t]].sum().length)
                                     for t in self.unique_tags]

    def transform(self):
        pass

    def observed_size(self):
        return len(self.raw_tags)

    def unique_size(self):
        return len(self.unique_tags_set)

