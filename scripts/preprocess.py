import pandas as pd
import re
from pathlib import Path

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.strip()
    text = re.sub(r"\s+", " ", text)

    # Arabic normalization
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "و", text)
    text = re.sub("ئ", "ي", text)
    text = re.sub("ـ", "", text)

    return text

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "kb.csv"
OUTPUT_PATH = BASE_DIR / "data" / "kb_clean.csv"

df = pd.read_csv(INPUT_PATH)

df["question"] = df["question"].apply(clean_text)
df["answer"] = df["answer"].apply(clean_text)

df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")
print(f"✅ Prétraitement terminé. Fichier créé: {OUTPUT_PATH}")