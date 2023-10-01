# django_app/common/utils.py
import sys
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image


def create_thumbnail(image, size=(300, 300), format="JPEG", quality=85):
    """
    Create a thumbnail of the specified image.

    Args:
        image (FileField/ImageField): The original image.
        size (tuple): The desired thumbnail size.
        format (str): The desired thumbnail format.
        quality (int): The desired quality of the thumbnail.

    Returns:
        InMemoryUploadedFile: The generated thumbnail.
    """
    img = Image.open(image)
    img.thumbnail(size, Image.ANTIALIAS)
    img = img.convert("RGB")

    output = BytesIO()
    img.save(output, format=format, quality=quality)
    output.seek(0)

    thumbnail_name = f"{image.name.split('.')[0]}_thumbnail.{format.lower()}"
    thumbnail = InMemoryUploadedFile(
        output,
        "ImageField",
        thumbnail_name,
        f"image/{format.lower()}",
        sys.getsizeof(output),
        None,
    )

    return thumbnail
