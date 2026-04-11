import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import TFC

def carregar_tfcs():
    file_path = 'data/tfcs.json'
    
    # Limpa os dados antigos
    TFC.objects.all().delete()

    with open(file_path, 'r', encoding='utf-8') as f:
        tfcs_data = json.load(f)
        
        for item in tfcs_data:
            TFC.objects.create(
                titulo=item['titulo'],
                autor=item['autor'],
                orientador=item['orientador'],
                ano=item['ano'],
                resumo=item.get('resumo', ''),
                curso=item.get('curso', '')
            )
    
    print(f"Sucesso: {TFC.objects.count()} TFCs carregados!")

if __name__ == '__main__':
    carregar_tfcs()