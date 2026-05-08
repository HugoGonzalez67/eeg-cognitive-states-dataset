# EEG Cognitive States Dataset

This repository contains documentation and processing scripts associated with an EEG dataset acquired from engineering students using Muse 2 wearable EEG headsets.

The dataset is intended to support research on cognitive-state characterization using EEG signal processing, nonlinear dynamic descriptors, chaotic features, and machine learning methods.

## Dataset

The primary EEG dataset is hosted on Zenodo and includes recordings from Muse 2 EEG channels:

- TP9
- AF7
- AF8
- TP10

The signals were sampled at 256 Hz and include temporal markers associated with experimental segments and cognitive tasks.

Zenodo DOI: 10.5281/zenodo.20089290

## Repository structure

```text
scripts/
  preprocess_eeg.py
  segment_markers.py
  extract_nonlinear_features.py
  classify_cognitive_states.py

notebooks/
  example_preprocessing.ipynb

docs/
  dataset_description.md
  data_dictionary.md
