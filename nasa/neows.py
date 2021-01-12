#!/usr/bin/python3
import requests

## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update the date below, if you like
    startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)
    
    dates = []
    for x in neodata["near_earth_objects"]:
        dates.append(x)
    print(dates)
    #In the range speciified, which is the LARGEST asteroid?
    for x in dates:
        for roid_dict in neodata["near_earth_objects"][x]:
            roid_dict["estimated_diameter"]["miles"]["estimated_diameter_max"]



    #In the range specified, how many asteroids are labeled "Potentially hazardous" ?


    #What are the names of these "fatal" asteroids?


if __name__ == "__main__":
    main()

