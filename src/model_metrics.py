"File used to calculate model metrics for Binary Classification"
from typing import Mapping

import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.pipeline import Pipeline


def calculate_model_metrics(
    model: Pipeline, X: pd.DataFrame, y: pd.Series
) -> Mapping[str, float]:
    "Calculates Model metric binary scores."
    y_pred = model.predict(X)

    f1_metric = f1_score(y_pred=y_pred, y_true=y, average="binary")
    precision = precision_score(y_pred=y_pred, y_true=y, average="binary")
    recall = recall_score(y_pred=y_pred, y_true=y, average="binary")
    accuracy = accuracy_score(y_pred=y_pred, y_true=y)

    return dict(
        f1_metric=float(f1_metric),
        precision=float(precision),
        recall=float(recall),
        accuracy=float(accuracy),
    )
