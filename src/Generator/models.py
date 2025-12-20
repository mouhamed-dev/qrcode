from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
import uuid
import re


class QR_code(models.Model):
    data = models.CharField(max_length=255)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    qr_code = models.ImageField(upload_to="qr_code", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to="logos", null=True, blank=True)


    def save(self, *args, **kwargs):
        is_new = self.pk is None

        if is_new:
            super().save(*args, **kwargs)

        # QR config
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=1)
        qr.add_data(self.data)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        if self.logo:
            try:
                logo = Image.open(self.logo.path)

                qr_w, qr_h = qr_image.size
                logo_size = int(qr_w * 0.20)

                logo = logo.resize((logo_size, logo_size))
                pos = ((qr_w - logo_size) // 2, (qr_h - logo_size) // 2)

                if logo.mode in ("RGBA", "LA"):
                    qr_image.paste(logo, pos, logo)
                else:
                    qr_image.paste(logo, pos)
            except FileNotFoundError:
                pass 
    
        buffer = BytesIO()
        qr_image.save(buffer, 'PNG')
        safe_data = re.sub(r'[^a-zA-Z0-9_-]', '_', self.data[:50])
        file_name = f"qr_{safe_data}.png"
        self.qr_code.save(file_name, File(buffer), save=False)
        super().save(update_fields=['qr_code'])
