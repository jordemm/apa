from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

def validate_nascita(value):
    try:
        if value > datetime.now().date():
            raise ValidationError(
                _('attenzione alla data inserita'),
                params={'value': value}, )
    except:
        raise ValidationError(
            _('controllate la data'),
            params={'value': value},)


import json

def generate_codici_catastale_txt_file():
    with open('comuni.json', 'r') as data_file:
        json_data = data_file.read()
    array = json.loads(json_data)

    file = open('codice_fiscale/codici_catastali_updated.txt', 'w')
    for obj in array:
        nome = obj['nome'].lower()
        siglia = obj['sigla'].lower()
        codici_castatale = obj['codiceCatastale'].lower()
        riga = nome + ',' + codici_castatale + ',' + siglia + '\n'
        file.write(riga)

    file_old = open('codice_fiscale/codici_catastali.txt')

#compare both the newly generated file with the old one and add the lines that
# are present in the old but arent present in the new
    f, n = 0, 0;
    for line in file_old:
        found = False

        for obj in array:
            if line.split(',')[0].lower() == obj['nome'].lower():
                found = True
                f += 1
                break
        if not found:
            n += 1
            file.write(line.lower())
            found = False
    file.close()
    file_old.close()
    print (f, n)

if __name__ == '__main__':
    generate_codici_catastale_txt_file()