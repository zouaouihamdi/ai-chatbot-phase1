import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Charger dataset nettoyé
df = pd.read_csv("data/kb_clean.csv")

# Charger modèle pré-entraîné (Transfer Learning)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Encoder toutes les questions
questions = df["question"].tolist()
embeddings = model.encode(questions)

def get_best_answer(user_question):
    user_embedding = model.encode([user_question])
    
    similarities = cosine_similarity(user_embedding, embeddings)[0]
    best_index = np.argmax(similarities)
    
    best_score = similarities[best_index]
    best_answer = df.iloc[best_index]["answer"]
    
    return best_answer, best_score

# Test interactif
while True:
    user_input = input("Vous: ")
    if user_input.lower() == "exit":
        break
    
    answer, score = get_best_answer(user_input)
    print(f"Bot: {answer}")
    print(f"Confidence: {round(score*100,2)}%")