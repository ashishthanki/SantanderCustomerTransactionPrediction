"Model Pipeline and defined model."
import logging

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

logger = logging.getLogger(__name__)


def model_pipeline(X: pd.DataFrame, y: pd.Series) -> Pipeline:
    pipeline = Pipeline(
        [
            ("standard_scaler", StandardScaler()),
            (
                "random_forest",
                RandomForestClassifier(
                    random_state=42, class_weight="balanced_subsample"
                ),
            ),
        ]
    )
    logger.debug("Created Pipeline \n%s. Fitting Pipeline.", pipeline)

    pipeline.fit(X, y)

    logger.debug("Pipeline Fitted.")

    return pipeline
