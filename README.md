# EEG Cognitive States Dataset

This repository contains documentation and processing scripts associated with an EEG dataset acquired from engineering students using Muse 2 wearable dry-electrode EEG headsets.

The dataset supports research on cognitive-state characterization using EEG signal processing, nonlinear dynamics-based descriptors, chaotic features, and machine learning methods.

## Dataset

The primary EEG dataset is publicly available on Zenodo:

- Concept DOI: https://doi.org/10.5281/zenodo.20089289
- Version 1.0.0 DOI: https://doi.org/10.5281/zenodo.20089290

The dataset includes EEG recordings from Muse 2 EEG channels:

- TP9
- AF7
- AF8
- TP10

The signals were sampled at 256 Hz and include temporal markers associated with experimental segments and cognitive tasks.

The dataset includes recordings from control and experimental groups. The experimental condition involved ASMR-based audiovisual stimulation. During the experiment, students watched videos containing relevant, irrelevant, and false information.

## Important note

This repository does not store the raw EEG data files. The raw dataset is hosted on Zenodo. This repository provides documentation and scripts to support reproducibility, preprocessing, metadata generation, and feature extraction.

## Repository structure

```text
eeg-cognitive-states-dataset/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── docs/
│   ├── data_dictionary.md
│   └── dataset_description.md
├── scripts/
│   ├── generate_metadata_from_filenames.py
│   ├── preprocess_eeg.py
│   ├── segment_markers.py
│   └── extract_nonlinear_features.py
├── notebooks/
│   └── example_preprocessing.ipynb
└── examples/
    └── README.md
