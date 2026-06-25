from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DiseasePrediction
from .forms import DiseasePredictionForm
from .predictor import predict_disease

@login_required
def predict(request):
    if request.method == 'POST':
        form = DiseasePredictionForm(request.POST, request.FILES)
        if form.is_valid():
            prediction_record = form.save(commit=False)
            
            # Run ML prediction
            crop_name = prediction_record.crop
            crop_type = crop_name # It's now directly 'Tomato', 'Potato', or 'Rice'
            
            result = predict_disease(request.FILES['image'], crop_type)
            
            prediction_record.disease_name = result['disease_name']
            prediction_record.confidence = result['confidence']
            prediction_record.recommended_solution = result['recommended_solution']
            prediction_record.save()
            
            messages.success(request, "Analysis complete!")
            return redirect('prediction_history')
    else:
        form = DiseasePredictionForm()
        
    return render(request, 'disease_prediction/predict.html', {'form': form})

@login_required
def prediction_history(request):
    predictions = DiseasePrediction.objects.all().order_by('-prediction_date')
    return render(request, 'disease_prediction/history.html', {'predictions': predictions})
