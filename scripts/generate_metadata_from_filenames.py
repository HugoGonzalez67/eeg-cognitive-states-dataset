#!/usr/bin/env python3
"""
Generate metadata_subjects.csv from Muse 2 EEG filenames.

Expected filename examples:
  EEG_01_H_EXP_2024-10-31-12_25_25.csv
  EEG_05_M_EXP_2024-11-20-13_27_09.csv

Usage:
  python generate_metadata_from_filenames.py /path/to/csv_folder

Output:
  metadata_subjects.csv
"""
from pathlib import Path
import csv
import re
import sys

GROUP_MAP = {
    "EXP": "experimental",
    "EXPERIMENTAL": "experimental",
    "CTRL": "control",
    "CONTROL": "control",
    "CON": "control",
}

def parse_filename(filename: str):
    stem = Path(filename).stem
    parts = stem.split("_")
    if len(parts) < 4 or parts[0].upper() != "EEG":
        return None

    original_subject_number = parts[1]
    sex_code = parts[2].upper()
    group_code = parts[3].upper()
    group = GROUP_MAP.get(group_code, group_code.lower())

    rest = "_".join(parts[4:])
    acquisition_datetime = ""
    match = re.match(r"(\d{4}-\d{2}-\d{2})(?:[-_](\d{1,2})[_-](\d{1,2})[_-](\d{1,2}))?", rest)
    if match:
        date = match.group(1)
        if match.group(2):
            acquisition_datetime = f"{date} {int(match.group(2)):02d}:{int(match.group(3)):02d}:{int(match.group(4)):02d}"
        else:
            acquisition_datetime = date

    return {
        "original_subject_number": original_subject_number,
        "sex_code": sex_code,
        "group": group,
        "acquisition_datetime": acquisition_datetime,
    }

def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    files = sorted(folder.glob("*.csv"))

    rows = []
    for i, file in enumerate(files, start=1):
        parsed = parse_filename(file.name)
        if parsed is None:
            continue
        rows.append({
            "subject_id": f"sub-{i:03d}",
            "original_file": file.name,
            "group": parsed["group"],
            "sex_code": parsed["sex_code"],
            "device": "Muse 2",
            "sampling_rate_hz": "256",
            "channels": "TP9;AF7;AF8;TP10",
            "acquisition_datetime": parsed["acquisition_datetime"],
            "dataset_version": "1.0.0",
            "notes": "",
        })

    output = folder / "metadata_subjects.csv"
    fieldnames = [
        "subject_id",
        "original_file",
        "group",
        "sex_code",
        "device",
        "sampling_rate_hz",
        "channels",
        "acquisition_datetime",
        "dataset_version",
        "notes",
    ]
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {output}")

if __name__ == "__main__":
    main()
