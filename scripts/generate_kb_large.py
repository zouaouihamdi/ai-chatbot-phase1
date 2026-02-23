import pandas as pd

rows = []
_id = 1

def add(program, intent, lang, questions, answer, tags=""):
    global _id
    for q in questions:
        rows.append({
            "id": _id,
            "program": program,
            "intent": intent,
            "lang": lang,
            "question": q,
            "answer": answer,
            "tags": tags,
            "active": 1
        })
        _id += 1


# 1) journée détente (crique)
jc_price_fr = "Le tarif est de 100 DT par adulte. Enfant 5-12 ans : 50 DT. Moins de 4 ans gratuit."
jc_price_ar = "السعر 100 دينار للكبير و50 دينار للأطفال من 5 حتى 12 سنين وأقل من 4 سنين مجاني."
jc_schedule_fr = "Rendez-vous à 10h au port d’El Haouaria. Retour vers 19h."
jc_schedule_ar = "التجمع 10 صباحا في ميناء الهوارية والرجوع حتى 19 مساء."
jc_included_fr = "Coin privé face à la mer avec parasol, margoum, table et poufs. Déjeuner et boissons inclus."
jc_included_ar = "بلاصة خاصة قدام البحر فيها باراسول ومرقوم وطاولة وبوفات. الغداء والمشروبات داخلين."
jc_options_fr = "Options disponibles: masques de plongée, kayak et paddle (selon disponibilité)."
jc_options_ar = "فما خيارات: ماسك غطس، كاياك وبادل (حسب التوفر)."
jc_rules_fr = "Les boissons alcoolisées sont interdites."
jc_rules_ar = "المشروبات الكحولية ممنوعة."

# 2) balade en mer
bm_price_fr = "Le prix est de 350 DT par heure (bateau privé)."
bm_price_ar = "السوم 350 دينار للساعة (باتو برايفي)."
bm_capacity_fr = "Forfait groupe: jusqu’à 10 personnes."
bm_capacity_ar = "الفورفي حتى 10 أشخاص."
bm_duration_fr = "La durée est selon votre demande (1h, 2h, etc.)."
bm_duration_ar = "المدة على حساب طلبك (ساعة، ساعتين...)."
bm_included_fr = "Masques disponibles et eau fournie."
bm_included_ar = "فما ماسكات وماء متوفر."

# 3) plongée sous-marine
pl_price_fr = "Le tarif est de 100 DT par personne. Âge minimum: plus de 10 ans."
pl_price_ar = "السوم 100 دينار للشخص ولازم العمر أكثر من 10 سنين."
pl_included_fr = "Équipement inclus: combinaison, masque, palmes et bouteille."
pl_included_ar = "التجهيزات داخلين: كومبينازون، ماسك، زعانف وبوطيل."

# =========================
# (paraphrases)
# =========================

# General
general_fr = [
    "C’est quoi cette activité ?", "Pouvez-vous décrire l’activité ?", "Donnez-moi des détails sur le programme.",
    "Je veux des infos sur cette sortie.", "C’est quoi exactement ?"
]
general_ar = [
    "شنيا النشاط هذا؟", "اعطيني تفاصيل على البرنامج.", "نحب معلومات على الرحلة.", "شنوة البرنامج بالضبط؟", "فسرلي النشاط."
]

# Pricing
price_fr = [
    "Quel est le prix ?", "Combien ça coûte ?", "C’est combien le tarif ?", "Le prix est par personne ?",
    "Quel est le tarif adulte ?", "Quel est le tarif enfant ?", "Moins de 4 ans c’est gratuit ?",
    "Le prix inclut quoi ?", "Y a-t-il une promotion ?", "Donnez-moi le prix exact."
]
price_ar = [
    "قداش سومها؟", "السعر قداش؟", "بكداش؟", "السوم للشخص؟", "قداش للكبار؟",
    "قداش للصغار؟", "أقل من 4 سنين مجاني؟", "السعر يشمل شنو؟", "فما تخفيض؟", "اعطيني السوم الصحيح."
]

# Schedule / Time
schedule_fr = [
    "À quelle heure ça commence ?", "Heure du rendez-vous ?", "À quelle heure on finit ?",
    "وقتاش تبدا؟", "Quelle est l’heure de départ ?", "Quelle est l’heure du retour ?"
]
schedule_ar = [
    "وقتاش تبدا؟", "وقتاش التجمع؟", "وقتاش نرجعو؟", "قداش وقت البداية؟", "قداش وقت النهاية؟", "وقتاش نخرجو؟"
]

# Included
included_fr = [
    "Qu’est-ce qui est inclus ?", "C’est quoi اللي داخل في السعر ?", "Le déjeuner est inclus ?",
    "On aura un coin privé ?", "Est-ce qu’il y a parasol et poufs ?", "Les boissons sont incluses ?"
]
included_ar = [
    "شنو شامل؟", "شنو داخل في السعر؟", "الغداء داخل؟", "المشروبات داخلين؟",
    "فما بلاصة خاصة؟", "فما باراسول وبوفات؟"
]

# Options
options_fr = [
    "Y a-t-il des activités en option ?", "Kayak disponible ?", "Paddle disponible ?", "Masque de plongée disponible ?",
    "On peut faire kayak ou paddle ?"
]
options_ar = [
    "فما أنشطة زيادة؟", "كاياك موجود؟", "بادل موجود؟", "فما ماسك غطس؟", "نجم نعمل كاياك ولا بادل؟"
]

# Rules
rules_fr = [
    "L’alcool est autorisé ?", "On peut ramener de l’alcool ?", "Boissons alcoolisées ?"
]
rules_ar = [
    "الكحول مسموح؟", "نجم نجيب كحول؟", "المشروبات الكحولية ممنوعة؟"
]

# Duration
duration_fr = [
    "C’est combien de temps ?", "Quelle est la durée ?", "C’est par heure ?", "On peut réserver 2 heures ?"
]
duration_ar = [
    "قداش مدة؟", "بالساعة؟", "نجم نحجز ساعتين؟", "نختار قداش سوايع؟"
]

# Capacity
capacity_fr = [
    "Combien de personnes ?", "C’est pour combien de personnes ?", "Capacité du bateau ?", "Jusqu’à combien ?"
]
capacity_ar = [
    "قداش أشخاص؟", "الباتو يشيل قداش؟", "الفورفي حتى قداش؟", "حتى شحال من شخص؟"
]

# =========================
# Generate dataset
# =========================

# journée crique
add("journee_crique", "general", "fr", general_fr, jc_included_fr, "journee")
add("journee_crique", "general", "ar", general_ar, jc_included_ar, "journee")
add("journee_crique", "pricing", "fr", price_fr, jc_price_fr, "prix")
add("journee_crique", "pricing", "ar", price_ar, jc_price_ar, "prix")
add("journee_crique", "schedule", "fr", schedule_fr, jc_schedule_fr, "horaire")
add("journee_crique", "schedule", "ar", schedule_ar, jc_schedule_ar, "horaire")
add("journee_crique", "included", "fr", included_fr, jc_included_fr, "inclus")
add("journee_crique", "included", "ar", included_ar, jc_included_ar, "inclus")
add("journee_crique", "options", "fr", options_fr, jc_options_fr, "options")
add("journee_crique", "options", "ar", options_ar, jc_options_ar, "options")
add("journee_crique", "rules", "fr", rules_fr, jc_rules_fr, "regles")
add("journee_crique", "rules", "ar", rules_ar, jc_rules_ar, "regles")

# balade mer
add("balade_mer", "general", "fr", general_fr, "Balade en mer en bateau privé à Haouaria avec pauses baignade.", "balade")
add("balade_mer", "general", "ar", general_ar, "بالادة في البحر بباتو برايفي في الهوارية مع توقفات للسباحة.", "balade")
add("balade_mer", "pricing", "fr", price_fr, bm_price_fr, "prix")
add("balade_mer", "pricing", "ar", price_ar, bm_price_ar, "prix")
add("balade_mer", "duration", "fr", duration_fr, bm_duration_fr, "duree")
add("balade_mer", "duration", "ar", duration_ar, bm_duration_ar, "duree")
add("balade_mer", "capacity", "fr", capacity_fr, bm_capacity_fr, "capacite")
add("balade_mer", "capacity", "ar", capacity_ar, bm_capacity_ar, "capacite")
add("balade_mer", "included", "fr", included_fr, bm_included_fr, "inclus")
add("balade_mer", "included", "ar", included_ar, bm_included_ar, "inclus")

# plongée
add("plongee", "general", "fr", general_fr, "Plongée sous-marine à El Haouaria pour explorer les grottes avec encadrement.", "plongee")
add("plongee", "general", "ar", general_ar, "غطس تحت البحر في الهوارية لاكتشاف المغارات مع تأطير.", "plongee")
add("plongee", "pricing", "fr", price_fr, pl_price_fr, "prix")
add("plongee", "pricing", "ar", price_ar, pl_price_ar, "prix")
add("plongee", "included", "fr", included_fr, pl_included_fr, "equipement")
add("plongee", "included", "ar", included_ar, pl_included_ar, "equipement")

df = pd.DataFrame(rows)


df.to_csv("data/kb.csv", index=False, encoding="utf-8-sig")
print("✅ kb.csv generated with", len(df), "rows")