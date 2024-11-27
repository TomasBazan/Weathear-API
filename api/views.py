from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import os


@api_view(['GET'])
def get_mock(request):
    file_path = os.path.join(os.path.dirname(__file__), 'constants.json')
    with open(file_path, 'r') as file:
        data = json.load(file).get('data')
        print(data.get('queryCost'))
        """ data_for_user = {
            "direccion": data.get("resolvedAddress"),
            "zona-horaria": data.get("timezone"),
            "icono": data.get("icon"),
            "descripcion": data.get("description"),
            "maxima-temperatura": data.get("tempmax"),
            "minima-temperatura": data.get("tempmin"),
            "temperatura": data.get("temp"),
            "sensacion-termica": data.get("feelslike"),
            "humedad": data.get("humidity"),
            "probabilidad-de-presipitaciones": data.get("precipprob"),
        }
 """
        return Response(data)


