import pickle
import numpy as np
import pandas as pd


def disease(value):
    result = None
    if value == 15:
        result = "Fungal infection"
    elif value == 4:
        result = "Allergy"
    elif value == 16:
        result = "GERD"
    elif value == 9:
        result = "Chronic cholestasis"
    elif value == 14:
        result = "Drug Reaction"
    elif value == 33:
        result = "Peptic ulcer diseae"
    elif value == 1:
        result = "AIDS"
    elif value == 12:
        result = "Diabetes "
    elif value == 17:
        result = "Gastroenteritis"
    elif value == 6:
        result = "Bronchial Asthma"
    elif value == 23:
        result = "Hypertension "
    elif value == 30:
        result = "Migraine"
    elif value == 7:
        result = "Cervical spondylosis"
    elif value == 32:
        result = "Paralysis (brain hemorrhage)"
    elif value == 28:
        result = "Jaundice"
    elif value == 29:
        result = "Malaria"
    elif value == 8:
        result = "Chicken pox"
    elif value == 11:
        result = "Dengue"
    elif value == 37:
        result = "Typhoid"
    elif value == 40:
        result = "hepatitis A"
    elif value == 19:
        result = "Hepatitis B"
    elif value == 20:
        result = "Hepatitis C"
    elif value == 21:
        result = "Hepatitis D"
    elif value == 22:
        result = "Hepatitis E"
    elif value == 3:
        result = "Alcoholic hepatitis"
    elif value == 36:
        result = "Tuberculosis"
    elif value == 10:
        result = "Common Cold"
    elif value == 34:
        result = "Pneumonia"
    elif value == 13:
        result = "Dimorphic hemmorhoids(piles)"
    elif value == 18:
        result = "Heart attack"
    elif value == 39:
        result = "Varicose veins"
    elif value == 26:
        result = "Hypothyroidism"
    elif value == 24:
        result = "Hyperthyroidism"
    elif value == 25:
        result = "Hypoglycemia"
    elif value == 31:
        result = "Osteoarthristis"
    elif value == 5:
        result = "Arthritis"
    elif value == 0:
        result = "(vertigo) Paroymsal  Positional Vertigo"
    elif value == 2:
        result = "Acne"
    elif value == 38:
        result = "Urinary tract infection"
    elif value == 35:
        result = "Psoriasis"
    elif value == 27:
        result = "Impetigo"
    else:
        result = 'Some Found mistake please try again...'
    return result


def model(lst):
    features = ['itching',
                'skin_rash',
                'nodal_skin_eruptions',
                'continuous_sneezing',
                'shivering',
                'chills',
                'joint_pain',
                'stomach_pain',
                'acidity',
                'ulcers_on_tongue',
                'muscle_wasting',
                'vomiting',
                'burning_micturition',
                'spotting_ urination',
                'fatigue',
                'weight_gain',
                'anxiety',
                'cold_hands_and_feets',
                'mood_swings',
                'weight_loss',
                'restlessness',
                'lethargy',
                'patches_in_throat',
                'irregular_sugar_level',
                'cough',
                'high_fever',
                'sunken_eyes',
                'breathlessness',
                'sweating',
                'dehydration',
                'indigestion',
                'headache',
                'yellowish_skin',
                'dark_urine',
                'nausea',
                'loss_of_appetite',
                'pain_behind_the_eyes',
                'back_pain',
                'constipation',
                'abdominal_pain',
                'diarrhoea',
                'mild_fever',
                'yellow_urine',
                'yellowing_of_eyes',
                'acute_liver_failure',
                'swelling_of_stomach',
                'swelled_lymph_nodes',
                'malaise',
                'blurred_and_distorted_vision',
                'phlegm',
                'throat_irritation',
                'redness_of_eyes',
                'sinus_pressure',
                'runny_nose',
                'congestion',
                'chest_pain',
                'weakness_in_limbs',
                'fast_heart_rate',
                'pain_during_bowel_movements',
                'pain_in_anal_region',
                'bloody_stool',
                'irritation_in_anus',
                'neck_pain',
                'dizziness',
                'cramps',
                'bruising',
                'obesity',
                'swollen_legs',
                'swollen_blood_vessels',
                'puffy_face_and_eyes',
                'enlarged_thyroid',
                'brittle_nails',
                'swollen_extremeties',
                'excessive_hunger',
                'extra_marital_contacts',
                'drying_and_tingling_lips',
                'slurred_speech',
                'knee_pain',
                'hip_joint_pain',
                'muscle_weakness',
                'stiff_neck',
                'swelling_joints',
                'movement_stiffness',
                'spinning_movements',
                'loss_of_balance',
                'unsteadiness',
                'weakness_of_one_body_side',
                'loss_of_smell',
                'bladder_discomfort',
                'foul_smell_of urine',
                'continuous_feel_of_urine',
                'passage_of_gases',
                'internal_itching',
                'toxic_look_(typhos)',
                'depression',
                'irritability',
                'muscle_pain',
                'altered_sensorium',
                'red_spots_over_body',
                'belly_pain',
                'abnormal_menstruation',
                'dischromic _patches',
                'watering_from_eyes',
                'increased_appetite',
                'polyuria',
                'family_history',
                'mucoid_sputum',
                'rusty_sputum',
                'lack_of_concentration',
                'visual_disturbances',
                'receiving_blood_transfusion',
                'receiving_unsterile_injections',
                'coma',
                'stomach_bleeding',
                'distention_of_abdomen',
                'history_of_alcohol_consumption',
                'fluid_overload.1',
                'blood_in_sputum',
                'prominent_veins_on_calf',
                'palpitations',
                'painful_walking',
                'pus_filled_pimples',
                'blackheads',
                'scurring',
                'skin_peeling',
                'silver_like_dusting',
                'small_dents_in_nails',
                'inflammatory_nails',
                'blister',
                'red_sore_around_nose',
                'yellow_crust_ooze']
    mod = pickle.load(open('./model/desease_model.pickle', 'rb'))

    # data frame
    arr = np.array([lst])
    df = pd.DataFrame(arr, columns=features)

    y_pred = mod.predict(df)
    result = disease(y_pred)
    return result

