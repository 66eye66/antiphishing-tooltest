from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import PhishingRule, Whitelist, Blacklist, AlertThreshold

@login_required
@permission_required('admin_panel.view_phishingrule', raise_exception=True)
def admin_dashboard(request):
    rules = PhishingRule.objects.all()
    whitelist = Whitelist.objects.all()
    blacklist = Blacklist.objects.all()
    thresholds = AlertThreshold.objects.all()
    return render(request, 'admin_dashboard.html', {
        'rules': rules,
        'whitelist': whitelist,
        'blacklist': blacklist,
        'thresholds': thresholds
    })