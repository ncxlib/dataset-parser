# ncxlib Dataset storage and loader

This repository provides a structured approach for loading, processing, and saving datasets in a binary format using Python. It is designed to work with popular datasets (such as MNIST) stored in binary formats and allows for easy serialization with pickle. The code processes images and labels into structured data, which can be loaded into memory as needed.

This repo is mainly for internal usage but also has perma links for preprocesssed and pickle loaded popular datasets.

## Storage Format
Each data file is named as ncxlib.<dataset-name>.data inside the data/<dataset-name>/ folder. Every pickle file contains data in the following structure once loaded:
```python
    {
        "X_train": list[],
        "X_test": list[],
        "y_train": list[],
        "y_test": list[],
    }
```

## Getting started
You can directly download the dataset using curl:
```shell
curl -o ncxlib.mnist.data <perma-link>
```

## Datasets

| Dataset | Description | Permanent Link
|---------|-------------|--------|
| **MNIST** | A dataset for handwritten number images and labels by the NIST foundation. | [Link](https://ncxlib.s3.us-east-1.amazonaws.com/data/mnist/ncxlib.mnist.data.gz)

