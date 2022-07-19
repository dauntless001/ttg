from django.db import models

Level = models.TextChoices("Level", ["NDI", "NDII", "HNDI", "HNDII"])
Semester = models.TextChoices("Semester", ["First", "Second"])
Type = models.TextChoices("Type", ["deposit", "withdrawal", "other"])
VenueType = models.TextChoices("VenueType", ["classroom", "examination"])