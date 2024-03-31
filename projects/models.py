from django.db import models
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Image for project: {self.project.title}"

    def save(self, *args, **kwargs):
        # Open the uploaded image
        img = Image.open(self.image)

        # Convert image to RGB (in case it's in another format)
        if img.mode in ("RGBA", "P", "LA"):
            img = img.convert("RGB")

        # Resize/crop logic using Image.Resampling.LANCZOS
        target_size = (800, 600)
        img.thumbnail(target_size, Image.Resampling.LANCZOS)

        # Save the formatted image to a BytesIO object
        output = BytesIO()
        img.save(output, format='JPEG', quality=90)
        output.seek(0)

        # Change the ImageField value to be the newly modified image data
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(ProjectImage, self).save(*args, **kwargs)
