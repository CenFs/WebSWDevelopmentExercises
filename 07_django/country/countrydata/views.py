from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render
from django.core import serializers
import json

from .models import Continent, Country

"""
testInvalidParameters (countrydata.tests.JsonTestCase) ... FAIL
testJsonCallback (countrydata.tests.JsonTestCase) ... FAIL
testJsonContinents (countrydata.tests.JsonTestCase) ... ok
testJsonCountries (countrydata.tests.JsonTestCase) ... FAIL
"""


def continent_json(request, continent_code):
    try:
        continent = Continent.objects.get(code=continent_code)
        countries_qs = continent.countries.all().values('code', 'name')
        if not countries_qs:
            raise Http404("Not implemented")
        else:
            countries_list = []
            for each in countries_qs:
                countries_list.append(each)
            countries_dict = {}
            for i in countries_list:
                countries_dict[i['code']] = i['name']
            # jsondata = serializers.serialize('json', countries)
            callback = request.GET.get('callback')
            if callback:
                data_callback = '%s(%s);' % (callback, countries_dict)
                return HttpResponse(data_callback, "text/javascript")
            # return JsonResponse(json.dumps(countries_dict), safe=False)
            return HttpResponse(json.dumps(countries_dict), "application/json")
    except:
        raise Http404("Not implemented")

def country_json(request, continent_code, country_code):
    try:
        this_country1 = Country.objects.filter(code=country_code)
        if not this_country1:
            raise Http404("Not implemented")
        else:
            for this_country2 in this_country1:
                continent_of_this_country = Continent.objects.get(id=this_country2.continent.id)
                if continent_of_this_country.code == continent_code:
                    country = Country.objects.filter(code=country_code).values('area', 'population', 'capital')
                    details = {}
                    for info in country:
                        details['area'] = info['area']
                        details['population'] = info['population']
                        details['capital'] = info['capital']
                    callback = request.GET.get('callback')
                    if callback:
                        data_callback = '%s(%s);' % (callback, details)
                        return HttpResponse(data_callback, "text/javascript")
                    return HttpResponse(json.dumps(details), "application/json")
            raise Http404("Not implemented")
    except:
        raise Http404("Not implemented")
