from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import pytz

# Create your views here.



def my_endpoint(request):
    slack_name = request.GET.get('slack_name', 'No Slack Name Provided')
    track = request.GET.get('track', 'No Track Provided')

    utc_now = datetime.now(pytz.utc)
    current_day = utc_now.strftime('%A')
    formatted_utc_now = utc_now.isoformat()

    data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": formatted_utc_now,
        "track": track,
        "github_file_url": "https://github.com/ClintonNwokocha/hng_internship/blob/main/hngapp/views.py",
        "github_repo_url": "https://github.com/ClintonNwokocha/hng_internship",
        "status_code": 200,
    }
    return JsonResponse(data)