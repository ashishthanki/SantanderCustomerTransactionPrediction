"Transformation functions."
import logging
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

logger = logging.getLogger(__name__)


def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    logger.info("Transforming data")
    data
    logger.info("Transformed data successfully.")
    return data


def split_data(
    X: pd.DataFrame, y: pd.Series
) -> Tuple[
    pd.DataFrame, pd.Series, pd.DataFrame, pd.Series, pd.DataFrame, pd.Series
]:
    logger.debug("Splitting data into train, test and validation sets.")
    X_train, X_test_val, y_train, y_test_val = train_test_split(
        X, y, random_state=42, test_size=0.4
    )
    X_test, y_test, X_val, y_val = train_test_split(
        X_test_val, y_test_val, random_state=42, test_size=0.5
    )
    logger.debug("Split data into train, test and validation sets.")

    return (X_train, y_train, X_test, y_test, X_val, y_val)
