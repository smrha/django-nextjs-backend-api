from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from .models import WaitlistEntry
from .schemas import WaitlistEntryListSchema, WaitlistEntryDetailSchema

router = Router()

@router.get("", response=List[WaitlistEntryListSchema])
def list_waitlist_entries(request):
    qs = WaitlistEntry.objects.all()
    return qs

@router.get("/{entry_id}", response=WaitlistEntryDetailSchema)
def list_waitlist_entries(request, entry_id):
    obj = get_object_or_404(WaitlistEntry, id=entry_id)
    return obj