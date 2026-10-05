import json
import os
import shutil
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK = ROOT / "customer_churn_analysis.ipynb"
DATA = ROOT / "data" / "Telco-Customer-Churn.csv"


@pytest.fixture(scope="module")
def raw_data():
    return pd.read_csv(DATA)


@pytest.fixture(scope="module")
def notebook_namespace(tmp_path_factory):
    """Not defterindeki tüm kod hücrelerini geçici bir dizinde çalıştırır."""
    workdir = tmp_path_factory.mktemp("notebook_run")
    (workdir / "data").mkdir()
    shutil.copy(DATA, workdir / "data" / DATA.name)

    cells = json.loads(NOTEBOOK.read_text(encoding="utf-8"))["cells"]
    namespace = {"__name__": "__notebook__"}

    previous_cwd = os.getcwd()
    os.chdir(workdir)
    try:
        for cell in cells:
            if cell["cell_type"] == "code":
                exec("".join(cell["source"]), namespace)
    finally:
        os.chdir(previous_cwd)
    return namespace


def test_dataset_shape(raw_data):
    assert raw_data.shape == (7043, 21)


def test_customer_ids_are_unique(raw_data):
    assert raw_data["customerID"].is_unique


def test_churn_labels_are_yes_or_no(raw_data):
    assert set(raw_data["Churn"].unique()) == {"Yes", "No"}


def test_total_charges_has_11_blank_records(raw_data):
    blank = raw_data["TotalCharges"].astype("string").str.strip().eq("")
    assert blank.sum() == 11


def test_notebook_has_code_cells():
    cells = json.loads(NOTEBOOK.read_text(encoding="utf-8"))["cells"]
    assert any(cell["cell_type"] == "code" for cell in cells)


def test_preprocessing_drops_the_blank_total_charges_rows(notebook_namespace):
    assert notebook_namespace["df_preprocessed"].shape[0] == 7032


def test_train_test_split_is_80_20_and_stratified(notebook_namespace):
    ns = notebook_namespace
    assert len(ns["X_train"]) == 5625
    assert len(ns["X_test"]) == 1407
    assert abs(ns["y_train"].mean() - ns["y_test"].mean()) < 0.01


def test_logistic_regression_reproduces_readme_metrics(notebook_namespace):
    ns = notebook_namespace
    assert round(ns["test_accuracy"] * 100, 2) == 80.45
    assert round(ns["majority_class_baseline_accuracy"] * 100, 2) == 73.42
    assert ns["test_accuracy"] > ns["majority_class_baseline_accuracy"]


def test_confusion_matrix_matches_readme(notebook_namespace):
    ns = notebook_namespace
    matrix = ns["confusion_matrix_values"]
    assert matrix.tolist() == [[917, 116], [159, 215]]


def test_notebook_saves_the_figures(notebook_namespace):
    assert notebook_namespace["figures_dir"].is_dir()
    assert any(notebook_namespace["figures_dir"].glob("*.png"))
