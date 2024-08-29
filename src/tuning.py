import logging
from typing import Dict

import optuna
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    precision_recall_fscore_support,
)
from sklearn.model_selection import cross_val_score

logger = logging.getLogger(__name__)
optuna.logging.set_verbosity(optuna.logging.WARNING)


def objective(trial):
    # Number of trees in random forest
    n_estimators = trial.suggest_int(
        name="n_estimators", low=100, high=500, step=100
    )

    # Number of features to consider at every split
    max_features = trial.suggest_categorical(
        name="max_features", choices=["auto", "sqrt"]
    )

    # Maximum number of levels in tree
    max_depth = trial.suggest_int(name="max_depth", low=10, high=110, step=20)

    # Minimum number of samples required to split a node
    min_samples_split = trial.suggest_int(
        name="min_samples_split", low=2, high=10, step=2
    )

    # Minimum number of samples required at each leaf node
    min_samples_leaf = trial.suggest_int(
        name="min_samples_leaf", low=1, high=4, step=1
    )

    params = {
        "n_estimators": n_estimators,
        "max_features": max_features,
        "max_depth": max_depth,
        "min_samples_split": min_samples_split,
        "min_samples_leaf": min_samples_leaf,
    }
    model = RandomForestClassifier(random_state=SEED, **params)

    cv_score = cross_val_score(model, X_train, y_train, n_jobs=4, cv=5)
    mean_cv_accuracy = cv_score.mean()
    return mean_cv_accuracy


def hyperparameter_tune(
    model, X_train, y_train, X_val, y_val
) -> Dict[str, float]:
    logger.debug("Hyperparameter tune.")
    study = optuna.create_study()
    study.optimize(objective, n_trials=5)

    best_model = model
    best_model.fit(X_train, y_train)
    logger.debug("Best parameters found: %s", study.best_params)
    return best_model
