import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from farmers.models import Farmer
from crops.models import Crop
import pandas as pd

@login_required
def export_crops_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="crops_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Crop Name', 'Soil Type', 'Land Area', 'Sowing Date', 'Status'])

    if hasattr(request.user, 'farmer'):
        crops = Crop.objects.filter(farmer=request.user.farmer).values('crop_name', 'soil_type', 'land_area', 'sowing_date', 'status')
        for crop in crops:
            writer.writerow([crop['crop_name'], crop['soil_type'], crop['land_area'], crop['sowing_date'], crop['status']])

    return response

@login_required
def export_farmer_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="farmer_report.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    
    if hasattr(request.user, 'farmer'):
        farmer = request.user.farmer
        p.setFont("Helvetica-Bold", 20)
        p.drawString(100, 750, "Farmer Risk Intelligence Report")
        
        p.setFont("Helvetica", 12)
        p.drawString(100, 700, f"Name: {farmer.name}")
        p.drawString(100, 680, f"Phone: {farmer.phone}")
        p.drawString(100, 660, f"Location: {farmer.village}, {farmer.district}, {farmer.state}")
        p.drawString(100, 640, f"Total Land Size: {farmer.land_size} acres")
        
        p.drawString(100, 600, "Crops:")
        y = 580
        for crop in farmer.crops.all():
            p.drawString(120, y, f"- {crop.crop_name} ({crop.land_area} acres, Status: {crop.status})")
            y -= 20
            
    p.showPage()
    p.save()
    return response

@login_required
def reports_dashboard(request):
    from django.shortcuts import render
    return render(request, 'reports/dashboard.html')
