"""
Test suite for analysis functionality.

Note: ResourceWarnings from the olga module and sklearn version warnings may appear.
To suppress these warnings, run the test with:
    python -W ignore::ResourceWarning -W ignore::UserWarning test/test_analysis.py -v
"""

import warnings
# Suppress ResourceWarnings from olga module's unclosed file handles
warnings.filterwarnings("ignore", category=ResourceWarning)
# Suppress scikit-learn version warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*scikit-learn.*")
warnings.filterwarnings("ignore", message=".*Trying to unpickle estimator.*")

from base import TestBase
from clustcr import datasets, Clustering, ClusterAnalysis, ModelTraining


class ClusteringTest(TestBase):

    def setUp(self):
        self.cdr3 = datasets.test_cdr3().junction_aa
        self.epitopes = datasets.test_epitopes()[["junction_aa", "epitope"]]
        self.clustering_result = Clustering().fit(self.cdr3)

    def make_features(self):
        return self.clustering_result.compute_features(compute_pgen=True)

    def test_feature_generation(self):
        self.make_features()

    def test_pca(self):
        ClusterAnalysis(self.make_features()).pca()

    def test_prediction(self):
        ClusterAnalysis(self.make_features()).predict_quality()

#    def test_train_model(self):
#        model = ModelTraining(self.clustering_result.clusters_df, self.epitopes)
#        fitted = model.fit_data()
#        model.evaluate()
#        model.save(fitted, 'test.pkl')


if __name__ == '__main__':
    import unittest
    unittest.main()
