from django.db import models
from django.contrib.auth import get_user_model
from django.templatetags.static import static
from PIL import Image

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Only process if an image exists
        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)

            # Crop the image to a 1:1 ratio
            min_side = min(img.width, img.height)
            img_cropped = img.crop((0, 0, min_side, min_side))

            # Resize the image
            output_size = (300, 300)  # Adjust this value as needed
            img_cropped.thumbnail(output_size)

            # Save the processed image
            img_cropped.save(img_path)

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return static('images/default.webp')
