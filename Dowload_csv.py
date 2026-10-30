import glob
import os
import shutil
import kagglehub
import pandas as pd

DATASET = "marcelbiezunski/serie-a-matches-dataset-2020-2025"
LOCAL_CSV = "matches_seriea.csv"  # local copy of the file

def get_csv_path():
    if os.path.isfile(LOCAL_CSV):
        print("Dataset già presente")
        return LOCAL_CSV

    folder = kagglehub.dataset_download(DATASET)
    print("Dataset scaricato in:", folder)

    csv_files = glob.glob(os.path.join(folder, "**", "*.csv"), recursive=True)
    print("CSV trovati:", csv_files)

    if not csv_files:
        raise FileNotFoundError(f"Nessun CSV trovato in {folder}")

    # Coping the file 
    shutil.copy(csv_files[0], LOCAL_CSV)
    return LOCAL_CSV

