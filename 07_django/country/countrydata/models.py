from django.db import models


class Continent(models.Model):
    name = models.CharField(unique=True, max_length=255)
    code = models.CharField(unique=True, max_length=10)
    country = models.ForeignKey('Country', related_name='continents', null=True)

    #def __init__(self):
        #self.countries = Country.objects.filter(continent_id=self.id)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ['name']


class Country(models.Model):
    name = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    code = models.CharField(unique=True, max_length=10)
    population = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    continent = models.ForeignKey(Continent, related_name='countries')

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ['name']

'''
sql = 'SELECT * FROM countrydata_continent'
for i in Continent.objects.raw(sql):
    Continent.objects.filter(id=i.id).update(countries=Country.objects.filter(continent_id=i.id))
'''