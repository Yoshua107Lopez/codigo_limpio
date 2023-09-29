from decimal import Decimal, InvalidOperation
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import JsonResponse
from django.views import View
from .models import data
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import OperationalError


class dataView(View):
    @method_decorator(csrf_exempt, name='dispatch')
    def get(self, request, id=0):
        if id > 0:
            try:
                datos = data.objects.get(id=id)
            except datos.DoesNotExist:
                return JsonResponse({'message': 'data no encontrada...'}, status=404)
            return JsonResponse({'message': "CORRECTO", "data": datos.to_dict()})
        else:
            dataes = list(datos.objects.all().values())
            return JsonResponse({'dataes': dataes})

    def post(self, request):
        jd = json.loads(request.body)
        try:
            total = Decimal(jd['total'])
            nombre_cliente = jd['nombre_cliente']
        except InvalidOperation:
            return JsonResponse({'message': 'El campo `total` debe ser un número decimal válido.'}, status=400)
        except KeyError as e:
            return JsonResponse({'message': f'Falta el campo {e}.'}, status=400)

        if not nombre_cliente:
            return JsonResponse({'message': 'El campo "nombre_cliente" es obligatorio.'}, status=400)

        datos = data(nombre_cliente=nombre_cliente, total=total)
        datos.save()
        return JsonResponse({'message': 'Success', 'id': data.id})

    def put(self, request, id):
        jd = json.loads(request.body)
        total = jd.get('total', None)
        nombre_cliente = jd['nombre_cliente']

        datos = get_object_or_404(data, id=id)

        if total is None:
            return JsonResponse({'message': 'El campo "total" es obligatorio.'}, status=400)

        try:
            total = Decimal(total)
        except InvalidOperation:
            return JsonResponse({'message': 'El campo `total` debe ser un número decimal válido.'}, status=400)

        if not nombre_cliente:
            return JsonResponse({'message': 'El campo "nombre_cliente" es obligatorio.'}, status=400)

        datos.nombre_cliente = nombre_cliente
        datos.total = total
        datos.save()
        return JsonResponse({'message': 'Éxito, se editó la data', 'id': data.id})

    def delete(self, request, id):
        datos = get_object_or_404(data, id=id)
        try:
            datos.delete()
        except OperationalError:
            return JsonResponse({'message': 'Error al eliminar la data.'}, status=500)
        return JsonResponse({'message': 'Éxito, se eliminó la data', 'id': data.id})