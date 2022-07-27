from django.shortcuts import render
from .forms import *
from .filters import *
from django.http import JsonResponse
from .models import EgpPointsSurvey

def egp_points_survey_create(request):
    form = InsertAtricleForm()
    if request.method == 'POST':
        form_insert_atricle = InsertAtricleForm(request.POST)
        egp_point_id = form_egp_points_survey['egp_point'].value()
        date = form_egp_points_survey['date'].value()
        eps_data = EgpPointsSurvey(egp_point_id=egp_point_id, date=date, objectid=next_objectid('egp_points_survey'))
        form_egp_points_survey = EgpPointsSurveyForm(data=request.POST, instance=eps_data)
        if form_egp_points_survey.is_valid():
            form_egp_points_survey.save()
    else:
        form_egp_points_survey = EgpPointsSurveyForm()
        form_field = FileFieldForm()
    return render(request, "egp_points_survey/egp_points_survey.html",
                  context={'form_insert_atricle': form_insert_atricle, 'form_field': form_field})