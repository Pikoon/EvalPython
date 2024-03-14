from django.db import models
class Dates(models.Model):
    debut = models.DateField
    fin = models.DateField

#planifiée, en cours, réalisée, en pause, validée
class Tache(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    dates = models.ForeignKey(Dates, on_delete=models.CASCADE)
    duree = models.DurationField()
    statut = {
        "plan" : "Planifiée",
        "run" : "En cours",
        "fini" : "Réalisée",
        "pause" : "En pause",
        "ok" : "Validée"
    }
    etat_avancement = models.FloatField()
    priorite = models.IntegerField()
    super_tache = models.ForeignKey('self', on_delete=models.CASCADE)

#en pause, planifié, en cours, livré
class Projets(models.Model):
    nom = models.CharField(max_length=255)
    statut = {
        "pause" : "En pause",
        "plan" : "Planifié",
        "run" : "En cours",
        "ok" : "Livré"
    }
    etat_avancement = models.FloatField
    date = models.ForeignKey(Dates, on_delete=models.CASCADE)

class Employe(models.Model):
    name = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    absence = models.ForeignKey(Dates, on_delete=models.CASCADE)

class Responsable(Employe):
    projet = models.ForeignKey(Projets, on_delete=models.CASCADE)
