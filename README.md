# EEG Cognitive States Dataset

This repository contains documentation and processing scripts associated with an EEG dataset acquired from engineering students using Muse 2 wearable EEG headsets.

The dataset is intended to support research on cognitive-state characterization using EEG signal processing, nonlinear dynamic descriptors, chaotic features, and machine learning methods.

## Dataset

The primary EEG dataset is hosted on Zenodo and includes recordings from Muse 2 EEG channels:

- TP9
- AF7
- AF8
- TP10

The signals were sampled at 256 Hz and include temporal markers associated with experimental segments and cognitive tasks. The experimental condition involved ASMR-based audiovisual stimulation, and students watched videos containing relevant, irrelevant, and false information.

Zenodo DOI: https://doi.org/10.5281/zenodo.20089289
Version 1.0.0 DOI: https://doi.org/10.5281/zenodo.20089290

## Important note

This repository does not store the raw EEG data files. The raw dataset is hosted on Zenodo. This repository provides documentation and scripts to support reproducibility, preprocessing, metadata generation, and feature extraction.

## Citation

If you use this dataset or the associated scripts, please cite the Zenodo record:

```bibtex
@dataset{gonzalez_hernandez_2026_eeg,
  author       = {González-Hernández, Hugo Gustavo and Galina Juárez, María Eugenia and Peña Cortés, Dafne Vania and Concha-Pérez, Elsa},
  title        = {EEG Dataset for Nonlinear Dynamics-Based Characterization of Cognitive States in Engineering Students},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.20089289},
  url          = {https://doi.org/10.5281/zenodo.20089289}
}

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
