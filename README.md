# Weather-Api
This is a project that retrieves and formats the current weather information for a given city using an API called WeatherAPI. The API request is made by passing the name of the city to the API and receiving a JSON response containing information about the temperature, latitude, and longitude of the city.

The project allows for the option to choose between two output formats: XML or JSON. If the output format is XML, the response is formatted as an XML document using the ElementTree module. If the output format is JSON, the response is formatted as a JSON object.

The project is implemented in Python and uses the Django web framework to handle HTTP requests and responses. The project also uses the requests library to make HTTP requests and the xml.etree.ElementTree module to generate XML documents.
