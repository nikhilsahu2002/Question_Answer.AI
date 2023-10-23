from django.db import models

class QARecord(models.Model):
    question = models.CharField(max_length=255)
    pdf_file = models.BinaryField()
    pdf_filename = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
