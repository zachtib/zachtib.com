from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.admin.models import User
from resume.models import Resume, Degree, Job, Project, Skill, Extracurricular

def index(request):
    r = get_object_or_404(Resume, pk=1)
    d = Degree.objects.filter(resume=r).order_by('-graddate')
    j = Job.objects.filter(resume=r).order_by('-startdate')
    p = Project.objects.filter(resume=r).order_by('-begindate')
    s = Skill.objects.filter(resume=r)
    e = Extracurricular.objects.filter(resume=r)
    return render_to_response('resume/index.html',
                                {   'resume': r,
                                    'degrees': d,
                                    'jobs': j,
                                    'projects': p,
                                    'skills': s,
                                    'extras': e,
                                })
