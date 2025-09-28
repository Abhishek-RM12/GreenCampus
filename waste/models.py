from django.db import models # type: ignore

class WasteReport(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='waste_reports/')
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.id} - {self.date_reported}"
