from django import forms

class PDFUploadForm(forms.Form):
    question = forms.CharField(max_length=255, label='Ask a question', required=True)
    pdf_file = forms.FileField(label='Upload a PDF file', required=True)
