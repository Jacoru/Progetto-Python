import glob
import os
import shutil
import kagglehub
import pandas as pd

DATASET = "marcelbiezunski/serie-a-matches-dataset-2020-2025"
LOCAL_CSV = "matches_seriea.csv"  # copia locale nella cartella del progetto

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

    # Copio il primo CSV nella cartella del progetto, così la prossima volta è già presente
    shutil.copy(csv_files[0], LOCAL_CSV)
    return LOCAL_CSV

df = pd.read_csv(get_csv_path())
print(df.head())