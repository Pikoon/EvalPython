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
    #1 = Defaut, 2 = Responsable, 3 = Gestionnaire
    role = models.IntegerChoices(
        1,
        2,
        3,
    )

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
    #1 = Planifiée, 2=En cours, 3 = Réalisée, 4=En pause, 5=Validée
    statut = models.IntegerChoices(
        1,
        2,
        3,
        4,
        5,
    )
    assigned = models.ManyToManyField(
        Employe,
        through="Assignee",
        through_fields=("group", "employe")
    )
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
