import requests, json, os

schoolYear = '202526'
course = 260      # LEI
os.makedirs('files', exist_ok=True)

for language in ['PT', 'ENG']:
    url = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'
    payload = {
        'language': language,
        'courseCode': course,
        'schoolYear': schoolYear
    }
    headers = {'content-type': 'application/json'}
    
    print(f"A recolher dados do curso ({language})...")
    response = requests.post(url, json=payload, headers=headers)
    response_dict = response.json()
    
    with open(os.path.join('files', f"ULHT{course}-{language}.json"), "w", encoding="utf-8") as f:
        json.dump(response_dict, f, indent=4)
    
    for uc in response_dict['courseFlatPlan']:
        url_uc = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails'
        payload_uc = {
            'language': language,
            'curricularIUnitReadableCode': uc['curricularIUnitReadableCode'],
        }
        print(f"  > A descarregar UC: {uc['curricularIUnitReadableCode']}")
        response_uc = requests.post(url_uc, json=payload_uc, headers=headers)
        response_uc_dict = response_uc.json()
        
        with open(os.path.join('files', f"{uc['curricularIUnitReadableCode']}-{language}.json"), "w", encoding="utf-8") as f:
            json.dump(response_uc_dict, f, indent=4)

print("Concluído! Verifica a pasta 'files'.")
