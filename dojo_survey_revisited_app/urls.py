from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('survey', views.survey),
    path('result', views.result),
]

# echo "# dojo_survey_revisited" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/jcambray10/dojo_survey_revisited.git
# git push -u origin main