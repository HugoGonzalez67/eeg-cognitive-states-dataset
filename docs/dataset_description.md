# Dataset Description

## Title

EEG Dataset for Nonlinear Dynamics-Based Characterization of Cognitive States in Engineering Students

## Overview

This dataset contains electroencephalographic (EEG) recordings acquired from engineering students using Muse 2 wearable dry-electrode EEG headsets. The dataset was collected to support research on nonlinear dynamics-based characterization and machine learning-based classification of cognitive states associated with different types of information processing during educational activities.

The dataset includes recordings from control and experimental groups. The experimental condition involved ASMR-based audiovisual stimulation. During the experiment, students watched videos containing relevant, irrelevant, and false information.

## Zenodo record

The primary dataset is publicly available on Zenodo:

- Concept DOI: https://doi.org/10.5281/zenodo.20089289
- Version 1.0.0 DOI: https://doi.org/10.5281/zenodo.20089290

## EEG acquisition

The EEG recordings were acquired using Muse 2 wearable dry-electrode headsets.

The recordings include EEG signals from four channels:

- TP9
- AF7
- AF8
- TP10

The nominal sampling frequency was 256 Hz.

## Experimental groups

The dataset includes two main groups:

- Control group
- Experimental group

The experimental group was exposed to ASMR-based audiovisual stimulation.

## Cognitive task structure

The experimental protocol involved audiovisual materials containing different types of information:

- Relevant information
- Irrelevant information
- False information

Temporal markers are included in the EEG files to indicate experimental segments and cognitive-task-related events.

## File structure

The Zenodo dataset includes raw EEG files in CSV format, as well as documentation files such as:

- `data_dictionary.csv`
- `metadata_subjects.csv`

The GitHub repository provides complementary documentation and scripts for reproducibility, preprocessing, metadata generation, and feature extraction.

## Data fields

The raw EEG CSV files include EEG channels and temporal information. Depending on the acquisition file, the main fields may include:

- `timestamps`
- `TP9`
- `AF7`
- `AF8`
- `TP10`
- `Marker0`

The `Marker0` field contains temporal markers associated with experimental segments or cognitive tasks.

## Subject-level metadata

Subject-level metadata are anonymized. Personal identifiers such as names, student IDs, email addresses, or institutional identifiers were removed before publication.

The `sex_code` variable was retained as an anonymized demographic variable because it is relevant for group-level EEG analyses. The H/M coding convention is documented in the dataset metadata.

## Suggested applications

This dataset may be useful for studies involving:

- EEG signal processing
- Nonlinear dynamics-based EEG characterization
- Chaotic descriptors and complexity measures
- Cognitive-state classification
- Machine learning applied to biosignals
- Educational neuroscience
- Human–machine interaction

## Suggested preprocessing

Suggested preprocessing steps may include:

1. Verification of timestamp consistency.
2. Inspection of raw EEG signals.
3. Artifact detection and rejection.
4. Filtering according to the research objective.
5. Segmentation using temporal markers.
6. Feature extraction from EEG segments.
7. Subject-independent validation for machine learning experiments, when applicable.

Researchers should document any preprocessing decisions before using the dataset for classification or statistical analysis.

## License

The dataset hosted on Zenodo is released under the Creative Commons Attribution 4.0 International License (CC BY 4.0), unless otherwise specified in the Zenodo record.

The code in the GitHub repository is released under the MIT License.

## Citation

If you use this dataset, please cite the Zenodo record:

```bibtex
@dataset{gonzalez_hernandez_2026_eeg,
  author       = {González-Hernández, Hugo G. and Galina Juárez, María Eugenia and Peña Cortés, Dafne Vania and Concha-Pérez, Elsa},
  title        = {EEG Dataset for Nonlinear Dynamics-Based Characterization of Cognitive States in Engineering Students},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.20089289},
  url          = {https://doi.org/10.5281/zenodo.20089289}
}
