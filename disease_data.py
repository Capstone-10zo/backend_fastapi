disease_k = ["궤양성각막질환", "무", "백내장(비성숙)", "백내장(성숙)", "백내장(초기)", "안검내반증", "안검종양", "유루증", "핵경화"]
disease = ["corneal_ulcer", "None", "cataract", "cataract", "cataract", "entropion", "eye_cancer", "epiphora", "nuclear_sclerosis"]

disease_label = dict()

for i in range(len(disease_k)):
    disease_label[disease_k[i]] = disease[i]
