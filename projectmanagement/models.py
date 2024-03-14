from django.db import models


# Create your models here.
class Dates(models.Model):
    debut = models.DateField
    fin = models.DateField

    def __str__(self):
        return self.debut


class Employe(models.Model):
    name = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    absence = models.ForeignKey(
        Dates,
        models.SET_NULL,
        blank=True,
        null=True
    )
    role = models.TextChoices({
        "def": "Defaut",
        "resp": "Responsable",
        "gest": "Gestionnaire"
    })

    def __str__(self):
        return self.name


class Tache(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    dates = models.ForeignKey(
        Dates,
        models.SET_NULL,
        blank=True,
        null=True
    )
    duree = models.DurationField()
    statut = models.TextChoices({
        "plan": "Planifiée",
        "run": "En cours",
        "fini": "Réalisée",
        "pause": "En pause",
        "ok": "Validée"
    }
    )
    # assignee = models.ManyToManyField(
    #    Employe,
    #    through="Assignee",
    #    through_fields=("group", "employe")
    # )
    etat_avancement = models.FloatField()
    priorite = models.IntegerChoices({
        1,
        2,
        3
    })

    super_tache = models.ForeignKey(
        'self',
        models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nom


class Projets(models.Model):
    nom = models.CharField(max_length=255)
    statut = models.TextChoices({
        "pause": "En pause",
        "plan": "Planifié",
        "run": "En cours",
        "ok": "Livré"
    })
    etat_avancement = models.FloatField
    date = models.ForeignKey(
        Dates,
        models.SET_NULL,
        blank=True,
        null=True
    )
    responsable = models.ForeignKey(
        Employe,
        models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nom
