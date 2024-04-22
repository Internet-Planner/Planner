import re

def extract_rrule_data(recurrence):
    # Expression régulière pour extraire les données de récurrence
    match = re.match(r'\[RRULE:(?P<rrule>.+)\]', recurrence)
    if match:
        rrule_data = match.group('rrule')
        # Analyse des données de récurrence pour extraire les règles spécifiques
        rrule_rules = {}
        for rule in rrule_data.split(';'):
            key, value = rule.split('=')
            rrule_rules[key] = value
        return rrule_rules
    else:
        raise ValueError("Le format de 'recurrence' est incorrect.")