import pytest
import numpy as np
import matplotlib.pyplot as plt

import mlflow_extend.plotting as mplt


def assert_is_figure(obj):
    assert isinstance(obj, plt.Figure)


@pytest.mark.parametrize("cm", [[[1, 2], [3, 4]], np.array([[1, 2], [3, 4]])])
def test_confusion_matrix(tmpdir, cm):
    fig = mplt.corr_matrix(cm)
    assert_is_figure(fig)


@pytest.mark.parametrize("corr", [[[1, 2], [3, 4]], np.array([[1, 2], [3, 4]])])
def test_corr_matrix(tmpdir, corr):
    fig = mplt.corr_matrix(corr)
    assert_is_figure(fig)


@pytest.mark.parametrize("limit", [None, 10])
def test_feature_importance(tmpdir, limit):
    features = ["a", "b", "c"]
    importances = [1, 2, 3]
    importance_type = "gain"
    fig = mplt.feature_importance(features, importances, importance_type, limit)
    assert_is_figure(fig)