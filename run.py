"Main file to run cyber security data data science workflow."
import logging
from pathlib import Path

from src.input import read_santander_data
from src.transform import split_data, transform_data

data_folder = Path(".") / "data"
file_path = data_folder / "train.csv"

logging.basicConfig(
    level=logging.DEBUG, format="%(name)s :: %(levelname)-8s :: %(message)s"
)
logger = logging.getLogger()


def main():
    "Main function to run Santander data science workflow."
    logger.info("Running Santander Data Science Workflow: %s", file_path)
    data = read_santander_data(file_path)
    data = transform_data(data)
    X, y = data.drop(columns=["target"]), data["target"]
    X_train, y_train, X_test, y_test, X_val, y_val = split_data(X, y)
    logger.info(
        "Completed Running Santander Data Science Workflow, see outputs:"
    )
    return


if __name__ == "__main__":
    main()
