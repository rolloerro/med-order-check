MAX_DOSE = {
    "paracetamol": 4000,
    "ibuprofen": 3200,
}

def check_dose(med):
    max_dose = MAX_DOSE.get(med.name.lower())
    if not max_dose:
        return None

    daily_dose = med.dose_mg * med.frequency_per_day
    if daily_dose > max_dose:
        return f"Превышена суточная доза {med.name}: {daily_dose} мг"
    return None
