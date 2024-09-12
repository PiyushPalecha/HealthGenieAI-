def analyze_input(user_input):
    disease_data = {
        "flu": {
            "disease_name": "Influenza (Flu)",
            "symptoms": ["Fever", "Cough", "Sore throat", "Runny or stuffy nose", "Muscle or body aches"],
            "treatment": ["Rest, fluids, antiviral medications"],
            "medicine": "Oseltamivir (Tamiflu), Zanamivir (Relenza)",
            "specialized_doctor": "General Practitioner, Infectious Disease Specialist",
            "immediate_actions": ["Stay hydrated", "Rest", "Take over-the-counter pain relievers"],
            "causes": ["Influenza virus"]
        },
        "diabetes": {
            "disease_name": "Diabetes Mellitus",
            "symptoms": ["Increased thirst", "Frequent urination", "Extreme hunger", "Unexplained weight loss"],
            "treatment": ["Insulin therapy, dietary changes, exercise"],
            "medicine": "Insulin, Metformin",
            "specialized_doctor": "Endocrinologist",
            "immediate_actions": ["Monitor blood sugar levels", "Take prescribed medications"],
            "causes": ["Genetic factors", "Lifestyle factors"]
        },
        "hypertension": {
            "disease_name": "Hypertension",
            "symptoms": ["Headache", "Shortness of breath", "Nosebleeds", "Flushing", "Dizziness"],
            "treatment": ["Lifestyle changes, medications"],
            "medicine": "ACE inhibitors, Beta-blockers",
            "specialized_doctor": "Cardiologist",
            "immediate_actions": ["Monitor blood pressure", "Reduce salt intake"],
            "causes": ["Genetic factors", "Lifestyle factors"]
        },
        "asthma": {
            "disease_name": "Asthma",
            "symptoms": ["Shortness of breath", "Chest tightness", "Wheezing", "Coughing"],
            "treatment": ["Inhalers, medications"],
            "medicine": "Albuterol, Fluticasone",
            "specialized_doctor": "Pulmonologist",
            "immediate_actions": ["Use inhaler", "Avoid triggers"],
            "causes": ["Allergens", "Genetic factors"]
        },
        "covid-19": {
            "disease_name": "COVID-19",
            "symptoms": ["Fever", "Cough", "Fatigue", "Loss of taste or smell", "Shortness of breath"],
            "treatment": ["Supportive care, antiviral medications"],
            "medicine": "Remdesivir, Dexamethasone",
            "specialized_doctor": "Infectious Disease Specialist",
            "immediate_actions": ["Isolate", "Stay hydrated", "Rest"],
            "causes": ["SARS-CoV-2 virus"]
        },
        "migraine": {
            "disease_name": "Migraine",
            "symptoms": ["Severe headache", "Nausea", "Sensitivity to light", "Sensitivity to sound"],
            "treatment": ["Pain relievers, anti-nausea medications"],
            "medicine": "Sumatriptan, Rizatriptan",
            "specialized_doctor": "Neurologist",
            "immediate_actions": ["Rest in a dark, quiet room", "Take prescribed medications"],
            "causes": ["Genetic factors", "Environmental factors"]
        },
        "arthritis": {
            "disease_name": "Arthritis",
            "symptoms": ["Joint pain", "Stiffness", "Swelling", "Decreased range of motion"],
            "treatment": ["Medications, physical therapy"],
            "medicine": "NSAIDs, Corticosteroids",
            "specialized_doctor": "Rheumatologist",
            "immediate_actions": ["Rest affected joints", "Apply heat or cold"],
            "causes": ["Wear and tear", "Autoimmune disorders"]
        },
        "depression": {
            "disease_name": "Depression",
            "symptoms": ["Persistent sadness", "Loss of interest", "Fatigue", "Changes in appetite", "Sleep disturbances"],
            "treatment": ["Therapy, medications"],
            "medicine": "SSRIs, SNRIs",
            "specialized_doctor": "Psychiatrist",
            "immediate_actions": ["Seek support", "Engage in physical activity"],
            "causes": ["Genetic factors", "Environmental factors"]
        },
        "anxiety": {
            "disease_name": "Anxiety Disorders",
            "symptoms": ["Excessive worry", "Restlessness", "Fatigue", "Difficulty concentrating"],
            "treatment": ["Therapy, medications"],
            "medicine": "Benzodiazepines, SSRIs",
            "specialized_doctor": "Psychiatrist",
            "immediate_actions": ["Practice relaxation techniques", "Seek support"],
            "causes": ["Genetic factors", "Environmental factors"]
        },
        "allergies": {
            "disease_name": "Allergies",
            "symptoms": ["Sneezing", "Itchy eyes", "Runny nose", "Hives"],
            "treatment": ["Antihistamines, avoidance of allergens"],
            "medicine": "Loratadine, Cetirizine",
            "specialized_doctor": "Allergist",
            "immediate_actions": ["Avoid allergens", "Take antihistamines"],
            "causes": ["Allergens", "Genetic factors"]
        },
        "eczema": {
            "disease_name": "Eczema",
            "symptoms": ["Itchy skin", "Red patches", "Dry skin", "Cracked skin"],
            "treatment": ["Moisturizers, corticosteroids"],
            "medicine": "Hydrocortisone, Tacrolimus",
            "specialized_doctor": "Dermatologist",
            "immediate_actions": ["Moisturize skin", "Avoid irritants"],
            "causes": ["Genetic factors", "Environmental factors"]
        },
        "bronchitis": {
            "disease_name": "Bronchitis",
            "symptoms": ["Cough", "Mucus production", "Fatigue", "Shortness of breath"],
            "treatment": ["Rest, fluids, medications"],
            "medicine": "Cough suppressants, Bronchodilators",
            "specialized_doctor": "Pulmonologist",
            "immediate_actions": ["Stay hydrated", "Rest"],
            "causes": ["Viruses", "Bacteria"]
        },
        "pneumonia": {
            "disease_name": "Pneumonia",
            "symptoms": ["Cough", "Fever", "Chills", "Shortness of breath"],
            "treatment": ["Antibiotics, antiviral medications"],
            "medicine": "Amoxicillin, Azithromycin",
            "specialized_doctor": "Pulmonologist",
            "immediate_actions": ["Stay hydrated", "Rest"],
            "causes": ["Bacteria", "Viruses"]
        },
        "tuberculosis": {
            "disease_name": "Tuberculosis",
            "symptoms": ["Cough", "Weight loss", "Night sweats", "Fever"],
            "treatment": ["Antibiotics"],
            "medicine": "Isoniazid, Rifampin",
            "specialized_doctor": "Infectious Disease Specialist",
            "immediate_actions": ["Seek medical attention", "Isolate to prevent spread"],
            "causes": ["Mycobacterium tuberculosis"]
        },
        "hepatitis": {
            "disease_name": "Hepatitis",
            "symptoms": ["Fatigue", "Nausea", "Abdominal pain", "Jaundice"],
            "treatment": ["Antiviral medications, supportive care"],
            "medicine": "Interferon, Ribavirin",
            "specialized_doctor": "Hepatologist",
            "immediate_actions": ["Avoid alcohol", "Seek medical attention"],
            "causes": ["Hepatitis viruses"]
        },
        "hiv": {
            "disease_name": "HIV/AIDS",
            "symptoms": ["Fever", "Chills", "Rash", "Night sweats", "Muscle aches"],
            "treatment": ["Antiretroviral therapy"],
            "medicine": "Tenofovir, Emtricitabine",
            "specialized_doctor": "Infectious Disease Specialist",
            "immediate_actions": ["Seek medical attention", "Practice safe sex"],
            "causes": ["Human Immunodeficiency Virus (HIV)"]
        },
        "malaria": {
            "disease_name": "Malaria",
            "symptoms": ["Fever", "Chills", "Headache", "Nausea", "Muscle pain"],
            "treatment": ["Antimalarial medications"],
            "medicine": "Chloroquine, Artemisinin",
            "specialized_doctor": "Infectious Disease Specialist",
            "immediate_actions": ["Seek medical attention", "Avoid mosquito bites"],
            "causes": ["Plasmodium parasites"]
        },
          "hepatitis": {
    "disease_name": "Hepatitis",
    "symptoms": ["Fatigue", "Nausea", "Abdominal pain", "Jaundice"],
    "treatment": ["Antiviral medications, supportive care"],
    "medicine": "Interferon, Ribavirin",
    "specialized_doctor": "Hepatologist",
    "immediate_actions": ["Avoid alcohol", "Seek medical attention"],
    "causes": ["Hepatitis viruses"],
    "medicinal_plants": [
      "Milk thistle", "Dandelion", "Turmeric", "Neem", "Licorice root"
    ]
  },
  "hiv": {
    "disease_name": "HIV/AIDS",
    "symptoms": ["Fever", "Chills", "Rash", "Night sweats", "Muscle aches"],
    "treatment": ["Antiretroviral therapy"],
    "medicine": "Tenofovir, Emtricitabine",
    "specialized_doctor": "Infectious Disease Specialist",
    "immediate_actions": ["Seek medical attention", "Practice safe sex"],
    "causes": ["Human Immunodeficiency Virus (HIV)"],
    "medicinal_plants": [
      "Ashwagandha", "Tulsi (Basil)", "Neem", "Ginger", "Curcumin (from Turmeric)"
    ]
  },
  "malaria": {
    "disease_name": "Malaria",
    "symptoms": ["Fever", "Chills", "Headache", "Nausea", "Muscle pain"],
    "treatment": ["Antimalarial medications"],
    "medicine": "Chloroquine, Artemisinin",
    "specialized_doctor": "Infectious Disease Specialist",
    "immediate_actions": ["Seek medical attention", "Avoid mosquito bites"],
    "causes": ["Plasmodium parasites"],
    "medicinal_plants": [
      "Artemisia annua", "Neem", "Tulsi (Basil)", "Ginger", "Curcumin (from Turmeric)"
    ]
  },
  "heart disease": {
    "disease_name": "Heart Disease",
    "symptoms": ["Chest pain, shortness of breath, fatigue, irregular heartbeat"],
    "treatment": ["Lifestyle changes, medications, surgery"],
    "medicine": "Aspirin, statins, beta-blockers",
    "specialized_doctor": "Cardiologist",
    "immediate_actions": ["Seek medical attention immediately"],
    "causes": ["High blood pressure, high cholesterol, smoking, diabetes"],
    "medicinal_plants": [
      "Garlic", "Ginger", "Turmeric", "Basil", "Rosemary"
    ]
  },
  "stroke": {
    "disease_name": "Stroke",
    "symptoms": ["Sudden numbness or weakness, especially on one side of the body; sudden confusion, trouble speaking or understanding; sudden trouble seeing in   one or both eyes; sudden severe headache with no known"],
    "treatment": ["Emergency medical treatment, rehabilitation"],
    "medicine": "Blood thinners, antiplatelet agents",
    "specialized_doctor": "Neurologist",
    "immediate_actions": ["Call emergency services immediately"],
    "causes": ["Blood clots, bleeding in the brain"],
    "medicinal_plants": [
      "Garlic", "Ginger", "Turmeric", "Basil", "Rosemary"
    ]
  },
  "cancer": {
    "disease_name": "Cancer",
    "symptoms": ["Lump or mass, changes in bowel or bladder habits, unusual bleeding or discharge, sore that doesn't heal, changes in skin, persistent cough or hoarseness, unexplained weight loss, fatigue, fever, night sweats, or changes in appetite"],
    "treatment": ["Surgery, chemotherapy, radiation therapy, targeted therapy, immunotherapy"],
    "medicine": "Various depending on the type of cancer",
    "specialized_doctor": "Oncologist",
    "immediate_actions": ["Seek medical attention immediately"],
    "causes": ["Genetic factors, environmental factors, lifestyle factors"],
    "medicinal_plants": [
      "Turmeric, ginger, green tea, reishi mushroom, ginseng"
    ]
  },
  "gastroesophageal reflux disease (GERD)": {
    "disease_name": "Gastroesophageal Reflux Disease (GERD)",
    "symptoms": ["Heartburn, chest pain, acid reflux, difficulty swallowing, sore throat"],
    "treatment": ["Lifestyle changes, medications"],
    "medicine": "Antacids, proton pump inhibitors",
    "specialized_doctor": "Gastroenterologist",
    "immediate_actions": ["Avoid triggers like spicy foods, alcohol, and caffeine"],
    "causes": "Weakened lower esophageal sphincter, increased stomach acid production",
    "medicinal_plants": [
      "Ginger, licorice root, aloe vera, chamomile, fennel"
    ]
  },
  "kidney stones": {
    "disease_name": "Kidney Stones",
    "symptoms": ["Severe pain in the side or back, blood in the urine, nausea, vomiting, fever"],
    "treatment": ["Pain management, medications, procedures to remove stones"],
    "medicine": "Pain relievers, alpha-blockers",
    "specialized_doctor": "Urologist",
    "immediate_actions": "Drink plenty of fluids, take over-the-counter pain relievers",
    "causes": "Excess calcium, uric acid, or oxalate in urine",
    "medicinal_plants": [
      "Dandelion root, parsley, coriander, celery, watermelon"
    ]
  },
  "thyroid disease": {
    "disease_name": "Thyroid Disease",
    "symptoms": "Hypothyroidism: fatigue, weight gain, cold intolerance; Hyperthyroidism: weight loss, anxiety, heat intolerance",
    "treatment": ["Hormone replacement therapy"],
    "medicine": "Levothyroxine (hypothyroidism), anti-thyroid medications (hyperthyroidism)",
    "specialized_doctor": "Endocrinologist",
    "immediate_actions": "Monitor symptoms, take prescribed medications",
    "causes": "Autoimmune disorders, genetic factors, iodine deficiency",
    "medicinal_plants": [
      "Ashwagandha, guggul, turmeric, licorice root, seaweed"
    ]
  },
  "multiple sclerosis (MS)": {
    "disease_name": "Multiple Sclerosis (MS)",
    "symptoms": "Numbness, weakness, fatigue, vision problems, balance problems, spasticity",
    "treatment": ["Disease-modifying therapies, symptomatic treatment"],
    "medicine": "Interferon beta, glatiramer acetate",
    "specialized_doctor": "Neurologist",
    "immediate_actions": "Seek medical attention if symptoms worsen",
    "causes": "Autoimmune disorder",
    "medicinal_plants": [
      "Ginkgo biloba, turmeric, ginger, rosemary, valerian"
    ]
  },
  "Parkinson's disease": {
    "disease_name": "Parkinson's Disease",
    "symptoms": "Tremors, rigidity, slow movements, difficulty walking, balance problems",
    "treatment": ["Medications, physical therapy, speech therapy"],
    "medicine": "Levodopa, carbidopa",
    "specialized_doctor": "Neurologist",
    "immediate_actions": "Seek medical attention",
    "causes": "Loss of dopamine-producing neurons",
    "medicinal_plants": [
      "Ginkgo biloba, turmeric, ginger, rosemary, valerian"
    ]
  },
  "Alzheimer's disease": {
    "disease_name": "Alzheimer's Disease",
    "symptoms": "Memory loss, confusion, difficulty with tasks, changes in personality",
    "treatment": ["Medications, supportive care"],
    "medicine": "Donepezil, rivastigmine, galantamine",
    "specialized_doctor": "Neurologist",
    "immediate_actions": "Seek medical attention",
    "causes": "Abnormal buildup of proteins in the brain",
    "medicinal_plants": [
      "Ginkgo biloba, turmeric, ginger, rosemary, valerian"
    ]
  }

        # Add more diseases and their details here
    }

    # Normalize user input for case-insensitive matching
    normalized_input = user_input.lower()

    # Check for exact matches or partial matches
    for disease, details in disease_data.items():
        if disease in normalized_input or any(symptom in normalized_input for symptom in details["symptoms"]):
            return details

    # Handle unknown diseases with a more informative default response
    return {
        "disease_name": "Unknown",
        "symptoms": "N/A",
        "treatment": "N/A",
        "medicine": "N/A",
        "specialized_doctor": "N/A",
        "immediate_actions": "N/A",
        "causes": "N/A",
        "message": "Based on the provided information, we couldn't identify a specific disease. Please consult a healthcare professional for a proper diagnosis and treatment."
    }