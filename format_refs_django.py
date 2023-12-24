import os
import re

def regex_django_references(directory):

    static_load_str = "{% load static %}"

    if not os.path.isdir(directory):
        print(f"El directorio proporcionado '{directory}' no existe.")
        return               

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)

                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                #Regex para referencias de archivos
                content = re.sub(r'href="(/?[^https:][^http:][^ftp:][^"#?]+)\.(?!html)([a-z]{2,5})"', 
                                 'href="{% static \'\g<1>.\g<2>\' %}"', content)
                #Regex para fuentes de archivos
                content = re.sub(r'src="(/?[^https:][^http:][^ftp:][^"#?]+)\.(?!html)([a-z]{2,5})"', 
                                 'src="{% static \'\g<1>.\g<2>\' %}"', content)
                #Regex para templates 
                content = re.sub(r'href="(/?[^https:][^http:][^ftp:][^"#?]+)\.html"', 
                                 'href="{% url \'\g<1>\' %}"', content)

                #Regex para cebeceras
                if static_load_str not in content:
                    content = re.sub(r'<head>', r'\1\n\t' + static_load_str, content)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

                print(f"Cambios realizados correctamente en {filepath}")

def find_html_references(directory):
    view_names = set()

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Buscar referencias a archivos .html
                matches = re.findall(r'href="(/?[^https:][^http:][^ftp:][^"#?]+)\.html"', content)
                for match in matches:
                    view_names.add(match)

    return view_names

def get_views_filepath(directory):   
    views_filepaths = []
    roots= []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == ('views.py') :
                views_filepaths.append(os.path.join(root, file))
                roots.append(root)
                
    if len(views_filepaths) > 1:
        print("Se esperaba solo un archivo views.py")

    return views_filepaths[0], roots[0]

def update_views(views_filepath, view_names):
    with open(views_filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for view_name in view_names: 
        if f'def {view_name}(request):' not in content:

            f.write(f"\n\ndef {view_name}(request):\n")
            f.write(f"    return render(request, '{view_name}.html')\n")

directory = input("Introduce la ruta del directorio de las plantillas HTML: ").strip()
regex_django_references(directory)
