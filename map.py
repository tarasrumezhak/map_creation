import geocoder

def get_coords(location):
    '''
    (str) --> list
    This function takes the name of location as argument
    and returns the list of real numbers coordinates
    >>> get_coords("New York")
    [40.71455000000003, -74.00713999999994]
    '''
    coords = geocoder.arcgis(location)
    return coords.latlng

def set_value(answer):
    '''
    (str) --> bool
    Returns True if answer is "y"
    and returns False otherwise
    >>> set_value("y")
    True
    '''
    if answer == "y":
        return True
    else:
        return False

def info_request():
    '''
    (None) --> (bool, bool, str)
    Asks user which information will be shown,
    returns the tuple of user answers
    '''
    print("You can choose which information will be shown on map:")
    print("Do you want the map with statistic about film counts? (y/n): ")
    film_count = set_value(input())
    print("Do you want to see the most frequent city locations? (y/n): ")
    city = set_value(input())
    print("Please write the title of the film to see its locations: ")
    film = input()
    return (film_count, city, film)
