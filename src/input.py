"Reads Santander Data files."
import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


def read_santander_data(file_path: Path) -> pd.DataFrame:
    "Reads Santander data and returns a DataFrame with correct data types."
    logger.debug("Loading Data: %s", file_path)
    data = pd.read_csv(
        file_path,
    )
    logger.debug("Read Data shape: %s", data.shape)
    return data
