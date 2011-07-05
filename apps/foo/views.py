from django.http import HttpResponse
import json
import os

from .search_indexes import site
from haystack.query import SearchQuerySet


RESPONSES = {
    "account": [
        { "value": '1-amanda', "label": 'Amanda' },
        { "value": '1-aron',   "label": 'Aron' },
        { "value": '3-eric',   "label": 'Eric' },
        { "value": '4-jeremy', "label": 'Jeremy' },
        { "value": '5-samuel', "label": 'Samuel' },
        { "value": '6-scott',  "label": 'Scott' }
    ],

    "filter": ['published', 'unpublished', 'draft'],
    "access": ['public', 'private', 'protected'],
    "title": [
        'Pentagon Papers',
        'CoffeeScript Manual',
        'Laboratory for Object Oriented Thinking',
        'A Repository Grows in Brooklyn'
    ],

    'city': [
        'Cleveland',
        'New York City',
        'Brooklyn',
        'Manhattan',
        'Queens',
        'The Bronx',
        'Staten Island',
        'San Francisco',
        'Los Angeles',
        'Seattle',
        'London',
        'Portland',
        'Chicago',
        'Boston'
    ],

    'state': [
      "Alabama", "Alaska", "Arizona", "Arkansas", "California",
      "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida",
      "Georgia", "Guam", "Hawaii", "Idaho", "Illinois",
      "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
      "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
      "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
      "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
      "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
      "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
      "Texas", "Utah", "Vermont", "Virginia", "Virgin Islands",
      "Washington", "West Virginia", "Wisconsin", "Wyoming"
    ],

    'country': [
      "China", "India", "United States", "Indonesia", "Brazil",
      "Pakistan", "Bangladesh", "Nigeria", "Russia", "Japan",
      "Mexico", "Philippines", "Vietnam", "Ethiopia", "Egypt",
      "Germany", "Turkey", "Iran", "Thailand", "D. R. of Congo",
      "France", "United Kingdom", "Italy", "Myanmar", "South Africa",
      "South Korea", "Colombia", "Ukraine", "Spain", "Tanzania",
      "Sudan", "Kenya", "Argentina", "Poland", "Algeria",
      "Canada", "Uganda", "Morocco", "Iraq", "Nepal",
      "Peru", "Afghanistan", "Venezuela", "Malaysia", "Uzbekistan",
      "Saudi Arabia", "Ghana", "Yemen", "North Korea", "Mozambique",
      "Taiwan", "Syria", "Ivory Coast", "Australia", "Romania",
      "Sri Lanka", "Madagascar", "Cameroon", "Angola", "Chile",
      "Netherlands", "Burkina Faso", "Niger", "Kazakhstan", "Malawi",
      "Cambodia", "Guatemala", "Ecuador", "Mali", "Zambia",
      "Senegal", "Zimbabwe", "Chad", "Cuba", "Greece",
      "Portugal", "Belgium", "Czech Republic", "Tunisia", "Guinea",
      "Rwanda", "Dominican Republic", "Haiti", "Bolivia", "Hungary",
      "Belarus", "Somalia", "Sweden", "Benin", "Azerbaijan",
      "Burundi", "Austria", "Honduras", "Switzerland", "Bulgaria",
      "Serbia", "Israel", "Tajikistan", "Hong Kong", "Papua New Guinea",
      "Togo", "Libya", "Jordan", "Paraguay", "Laos",
      "El Salvador", "Sierra Leone", "Nicaragua", "Kyrgyzstan", "Denmark",
      "Slovakia", "Finland", "Eritrea", "Turkmenistan"
    ],
}


def values(request, *args, **kwargs):
    category = request.GET.get("category", False)
    searchTerm = request.GET.get("searchTerm", False)

    if category is False or not searchTerm:
        return HttpResponse("")
    kwargs = {category: searchTerm, }
    q = SearchQuerySet(site=site).autocomplete(**kwargs)
    return HttpResponse(json.dumps([getattr(a, category) for a in q]))


def facets(request, *args, **kwargs):
    field_names = []
    for index in site.get_indexes().values():
        field_names += index.fields.keys()
    return HttpResponse(json.dumps(field_names))
