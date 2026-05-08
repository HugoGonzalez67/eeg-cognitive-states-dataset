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

## Suggested applications

This dataset and repository may be useful for studies involving:

EEG signal processing
Nonlinear dynamics-based EEG characterization
Chaotic descriptors and complexity measures
Cognitive-state classification
Machine learning applied to biosignals
Educational neuroscience
Human–machine interaction

## Dataset documentation

The Zenodo record includes documentation describing:

File structure
EEG channels
Sampling frequency
Temporal markers
Experimental groups
Anonymized subject-level metadata
Data dictionary

Personal identifiers were removed or anonymized before publication. The sex_code variable was retained as an anonymized demographic variable because it is relevant for group-level EEG analyses.

## License

The code in this repository is released under the MIT License.

The dataset hosted on Zenodo is released under the Creative Commons Attribution 4.0 International License (CC BY 4.0), unless otherwise specified in the Zenodo record.

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
## Contact

Hugo G. González-Hernández
hgonz@tec.mx 



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

