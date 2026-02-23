import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "kb.csv"

df = pd.read_csv(INPUT_PATH)

print("✅ Total lignes:", len(df))
print("\n✅ Répartition par programme:")
print(df["program"].value_counts())

print("\n✅ Répartition par langue:")
print(df["lang"].value_counts())

print("\n✅ Répartition par intent:")
print(df["intent"].value_counts())