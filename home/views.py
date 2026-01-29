from django.shortcuts import render , HttpResponse
import os
import joblib
from django.conf import settings
from .utils import transform_text

MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    'home',             
    'savedModels',
    'spam_model.joblib'
)

VECTORIZER_PATH = os.path.join(
    settings.BASE_DIR,
    'home',
    'savedModels',
    'vectorizer.joblib'
)

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# view function
def spam_check(request):
    result = None

    if request.method == "POST":
        msg = request.POST.get("message")

        msg = transform_text(msg)
        vector = vectorizer.transform([msg])
        pred = model.predict(vector)[0]

        result = "🚨 SPAM MESSAGE" if pred == 1 else "✅ NOT SPAM"

    return render(request, "home.html", {"result": result})


