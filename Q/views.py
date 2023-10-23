import PyPDF2
import openai
import io
from django.shortcuts import render
from django.http import JsonResponse
from .forms import PDFUploadForm

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

def extract_text_from_pdf(pdf_data):
    # Extract text from PDF binary data
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_data))
    pdf_text = ""
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()
    return pdf_text

def question_answering(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.cleaned_data['question']
            pdf_file = form.cleaned_data['pdf_file']

            pdf_data = pdf_file.read()
            pdf_text = extract_text_from_pdf(pdf_data)

            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=f"Document: {pdf_text}\nQuestion: {question}\nAnswer:",
                max_tokens=50
            )

            answer = response.choices[0].text.strip()

            # Return the answer as JSON
            return JsonResponse({'answer': answer})

    # Handle the case where the form is not valid or no data is entered
    form = PDFUploadForm()
    return render(request, 'index.html', {'form': form})
