from PIL import Image as Img
from io import BytesIO
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.conf import settings
import os

@csrf_exempt
def custom_upload(request):
    if request.method == 'POST' and 'upload' in request.FILES:
        file_obj = request.FILES['upload']
        img = Img.open(file_obj)
        img = img.resize((800, 600), Img.LANCZOS)  # Пример сжатия
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        file_path = default_storage.save(f'uploads/{file_obj.name}', buffer)
        url = os.path.join(settings.MEDIA_URL, file_path)
        return JsonResponse({'url': url})
    return JsonResponse({'error': {'message': 'Invalid request'}}, status=400)