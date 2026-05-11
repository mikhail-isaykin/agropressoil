from PIL import Image
import io
from django.core.files.base import ContentFile
from slugify import slugify


def convert_to_webp(image):
    img = Image.open(image).convert('RGB')
    output = io.BytesIO()
    img.save(output, format='WEBP', quality=85)
    output.seek(0)
    return ContentFile(output.read(), name=image.name.split('.')[0] + '.webp')

def generate_slug(title):
    return slugify(title)
