import requests
from xml.etree import ElementTree
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


API_KEY = '31371bc5c3msh34f399b07961d46p192883jsn2ba7562e3194'


@csrf_exempt
def get_current_weather(request):
    # Retrieve the 'city' and 'output_format' parameters from the request
    city_name = request.POST.get('city')
    output_format = request.POST.get('output_format')
    
    # Set the querystring and headers for the API request
    querystring = {"q": city_name}
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    
    # Make the API request to fetch the weather data
    url = 'https://weatherapi-com.p.rapidapi.com/current.json'
    response = requests.get(url, headers=headers, params=querystring)
    
    # Return an error message if the API request was unsuccessful
    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to fetch weather data'})
    
    # Parse the weather data from the API response
    weather_data = response.json()
    temperature = str(weather_data['current']['temp_c']) + ' C'
    latitude = str(weather_data['location']['lat'])
    longitude = str(weather_data['location']['lon'])
    city = weather_data['location']['name'] + ' ' + weather_data['location']['country']
    
    # Format the weather data in the requested output format (XML or JSON)
    if output_format == 'xml':
        # Create an XML response using ElementTree
        root = ElementTree.Element("root")
        ElementTree.SubElement(root, "Temperature").text = temperature
        ElementTree.SubElement(root, "City").text = city
        ElementTree.SubElement(root, "Latitude").text = latitude
        ElementTree.SubElement(root, "Longitude").text = longitude
        
        # Convert the ElementTree response to a string and return as an HTTP response
        response = ElementTree.tostring(root, encoding='utf-8', method='xml', xml_declaration=True)
        return HttpResponse(response, content_type='application/xml')
    else:
        # Return a JSON response with the weather data
        return JsonResponse({
            'Weather': temperature,
            'Latitude': latitude,
            'Longitude': longitude,
            'City': city
        })
