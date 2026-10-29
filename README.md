# TTTC3213 Group Project

## Scenario
This project profiles an Amazon product-review dataset to identify data-quality issues before describing product satisfaction. The dataset is an educational sample and is not assumed to represent all Amazon customers.

## Team
- ZHU ZHENTAO — A206174
- BIAN CHUNBO — A206292
- HOU ZHENGYANG — A206407

## Dataset
- Source: [Amazon products reviews dataset uncleaned](https://www.kaggle.com/datasets/satyakidas07/amazon-products-reviews-dataset-uncleaned) by Satyaki Das.
- The notebook downloads the dataset with `kagglehub` and reads the `Amazon_Data_Raw` worksheet. Review the dataset page and its terms before reuse.
- The raw dataset and any Kaggle credentials are intentionally excluded from this repository. The notebook avoids displaying usernames and raw review text.

## Run the notebook
Use Python 3.10 or later. From the repository root, install dependencies and launch Jupyter:

```bash
python -m pip install -r requirements.txt
python -m jupyter notebook notebooks/member_a_work.ipynb
```

Run all cells from top to bottom. On first download, Kaggle may require account authentication or acceptance of dataset conditions; follow Kaggle's prompts and never commit credentials.

## Analysis coverage
The notebook documents the scenario and data source, missing-value handling, data-quality checks, outlier diagnostics, at least two labeled charts, privacy and bias risks, and conclusion and limitations.
