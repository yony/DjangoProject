from django.db import models

class Site(models.Model):
    class SiteType(models.TextChoices):
        Beach = 'Beach', 'Beach'
        NaturalReserve = 'NaturalReserve', 'Natural Reserve'
        Restaurant = 'Restaurant', 'Restaurant'
        Hotel = 'Hotel', 'Hotel'
        SurfClub = 'SurfClub', 'Surf Club'
        DivingClub = 'DivingClub', 'Diving Club'
        Marina = 'Marina', 'Marina'
        YachtClub = 'YachtClub', 'Yacht Club'
        Other = 'Other', 'Other'

    type = models.CharField(max_length=20, choices=SiteType.choices)
    address = models.TextField()
    name = models.TextField()
    amenities = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
