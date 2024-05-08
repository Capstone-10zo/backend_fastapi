from tensorflow.keras.models import load_model

disease = ["cataract", "conjunctivitis", "entropion", "epiphora", "nuclear_sclerosis",
           "blepharoncus", "corneal_ulcer", "noncorneal_ulcer", "eye_cancer", "pigmentary_keratitis"]
disease_k = ["백내장", "결막염","안검내반증","유루증","핵경화", "안검염", "궤양성각막질환", "비궤양성각막질환",
             "안검종양", "색소침착성각막염"]

disease_lb = [['무', '비성숙', '성숙', '초기'], ['무', '유'], ['무', '유'], ['무', '유'],['무', '유'],
              ['무', '유'], ['무','상','하'], ['무','상','하'], ['무','유'], ['무', '유']]


model1 = load_model("model/model-cataract(백내장).h5")
model2 = load_model("model/model-conjunctivitis(결막염).h5")
model3 = load_model("model/model-entropion(안검내반증).h5")
model4 = load_model("model/model-epiphora(유루증).h5")
model5 = load_model("model/model-blepharoncus(안검염).h5")
model6 = load_model("model/model-nuclear_sclerosis(핵경화).h5")
model7 = load_model("model/model-nuclear_sclerosis(핵경화).h5")
model8 = load_model("model/model-nuclear_sclerosis(핵경화).h5")
model9 = load_model("model/model-nuclear_sclerosis(핵경화).h5")
model10 = load_model("model/model-nuclear_sclerosis(핵경화).h5")

model = [model1, model2, model3, model4, model5, model6,model7,model8,model9, model10]

models = dict()
disease_label = dict()
disease_kr = dict()

for i in range(len(disease)):
    models[disease[i]] = model[i]
    disease_kr[disease[i]] = disease_k[i]
    disease_label[disease[i]] = disease_lb[i]

print(disease_label)
print(disease_kr)