from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import uuid
import re


class QR_code(models.Model):
    data = models.CharField(max_length=255)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    qr_code = models.ImageField(upload_to="qr_code", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=1
        )
        qr.add_data(self.data)
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        qr_image.save(buffer, 'PNG')
        safe_data = re.sub(r'[^a-zA-Z0-9_-]', '_', self.data[:50])
        file_name = f"qr_{safe_data}.png"
        self.qr_code.save(file_name, File(buffer), save=False)

        return super().save(*args, **kwargs)

