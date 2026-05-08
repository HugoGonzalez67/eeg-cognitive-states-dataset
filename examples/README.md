# Examples

This folder is intended to contain small examples demonstrating how to use the documentation and scripts associated with the EEG Cognitive States Dataset.

The raw EEG dataset is not stored in this GitHub repository. The primary dataset is hosted on Zenodo:

- Concept DOI: https://doi.org/10.5281/zenodo.20089289
- Version 1.0.0 DOI: https://doi.org/10.5281/zenodo.20089290

## Purpose

The examples in this folder may include:

- Minimal synthetic EEG-like CSV files.
- Example metadata files.
- Demonstrations of filename parsing.
- Demonstrations of marker-based segmentation.
- Example workflows for preprocessing and feature extraction.

## Important note

Any files included in this folder should be small, anonymized, and intended only for demonstration purposes.

Do not upload raw EEG recordings or subject-identifiable data to this GitHub repository. Raw data should remain hosted on Zenodo.

## Suggested example structure

```text
examples/
├── README.md
├── sample_metadata_subjects.csv
└── sample_eeg_file.csv
## Example filename convention

A typical EEG filename may follow this structure:

```text
EEG_01_H_EXP_2024-10-31-12_25_25.csv
```

This filename can be interpreted as:

| Segment | Example | Meaning |
|---|---|---|
| Prefix | `EEG` | EEG recording file. |
| Subject number | `01` | Internal subject number. |
| Sex code | `H` | H/M demographic code. |
| Group | `EXP` | Experimental group. |
| Date and time | `2024-10-31-12_25_25` | Acquisition date and time. |

For public documentation and analysis, researchers should use anonymized subject identifiers such as `sub-001`, `sub-002`, etc.

## License

Example scripts and files in this repository are released under the MIT License, unless otherwise specified.

The full dataset hosted on Zenodo is released under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
