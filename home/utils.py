from django.shortcuts import render , HttpResponse

def transform_text(text):
    text = text.lower()
    return text