# README

## Overview

This repository contains the Jupyter notebooks and associated files used for my thesis. The thesis work primarily involved processing datasets and training models using Jupyter notebooks. Below, you'll find a description of the main folders and files, along with their specific purposes.

## Folder Structure and Description

### Dataset-creation

This folder is dedicated to preprocessing the datasets and training and evaluating the models.

#### Notebooks
- **`notebooks/apply_degradations.ipynb`**: Applies implemented degradations to the stump dataset.
- **`notebooks/apply_degradations_lego.ipynb`**: Applies implemented degradations to the lego dataset.
- **`notebooks/run_models.ipynb`**: Contains examples for training models.
- Similar files like **`run_models_nerfacto_stump_opt_off.ipynb`** also exist for training specific model configurations.

### Results

This folder handles the processing of rendered images and the creation of plots and tables.

#### Subfolders
- **`Results/jsons`**: Stores JSON files with metrics for all trained models.
- **`Results/metrics`**: Contains all preprocessed metrics in `.npy` format, which are used for generating plots.

#### Files
- **`Results/create_appendix_table.ipynb`** and **`sort_tables.ipynb`**: Responsible for creating tables that are included in the `Appendix.pdf`.
- **`Results/heatmap_stump_one_row_v4_CLUSTER_lego.ipynb`**: Generates heatmaps with relative decreases across metrics using the saved `.npy` files.


