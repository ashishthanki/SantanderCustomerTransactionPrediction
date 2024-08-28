"Transformation functions."
import logging

import pandas as pd

logger = logging.getLogger(__name__)


def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    logger.info("Transforming data")
    data = change_dtypes(data)
    data = remove_constant_columns(data)
    logger.info("Transformed data successfully.")
    return data


def change_dtypes(data: pd.DataFrame) -> pd.DataFrame:
    """Returns a DataFrame with changed column data types.

    Args:
        data (pd.DataFrame): Data to perform.

    Returns:
        pd.DataFrame: Modified DataFrame.
    """
    logger.debug("Changing DataFrame dtypes")
    for column_name in data.columns:
        if ("date" in column_name) or ("time" in column_name):
            logger.debug("Changing column name %s to datetime.", column_name)
            data[column_name] = pd.to_datetime(data[column_name])
        if "bytes" in column_name:
            logger.debug("Changing column name %s to integer.", column_name)
            data[column_name] = data[column_name].astype(int)
        # convert to category if distinct values are less than 20
        if data[column_name].nunique() < 25:
            logger.debug("Changing column name %s to category.", column_name)
            data[column_name] = data[column_name].astype("category")
    return data


def remove_constant_columns(data: pd.DataFrame) -> pd.DataFrame:
    """Remove columns from the DataFrame that have constant values.

    Args:
        data (pd.DataFrame): Data to remove constant value columns.

    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    constant_columns = [col for col in data.columns if data[col].nunique() == 1]
    logger.debug("Removing columns %s as they are constant.", constant_columns)
    data = data.drop(columns=constant_columns)
    return data
