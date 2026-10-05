from django.http import JsonResponse
from .models import Service


def home(request):
    return JsonResponse({
        "message": "CloudNexus backend is running!"
    })


def services(request):
    data = list(
        Service.objects.values(
            'id',
            'name',
            'status',
            'created_at'
        )
    )

    return JsonResponse(data, safe=False)

def add_service(request):
    service = Service.objects.create(
        name="Frontend",
        status="running"
    )

    return JsonResponse({
        "message": "Service added!",
        "id": service.id,
        "name": service.name,
        "status": service.status
    })