# TODO

Para cache de redis voy a ejecutar una imagend de docker y me voy a conectar desde el servidor a la cache de redis donde voy a almacenar los datos cacheados, deberia hacer un docker-compose y ver como hacer algo tipo playbook 





## API Request Types
All requests to the Timeline Weather API use the following the form:

https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/[location]/[date1]/[date2]?key=YOUR_API_KEY 

location (required) – is the address, partial address or latitude,longitude location for which to retrieve weather data. You can also use US ZIP Codes. 

date1 (optional) – is the start date for which to retrieve weather data. If a date2 value is also given, then it represents the first date for which to retrieve weather data. If no date2 is specified then weather data for a single day is retrieved, and that date is specified in date1. All dates and times are in local time of the location specified. Dates should be in the format yyyy-MM-dd.

Instead of an exact date, you can specify a dynamic date period. 

You can also request the information for a specific time for a single date by including time into the date1 field using the format yyyy-MM-ddTHH:mm:ss. For example 2020-10-19T13:00:00.

date2 (optional) – is the end date for which to retrieve weather data. This value may only be used when a date1 value is given. When both date1 and date2 values are given, the query is inclusive of date2 and the weather data request period will end on midnight of the date2 value. All dates and times are in local time of the specified location and should be in the format yyyy-MM-dd.

When no date1 or date2 is specified, the request will retrieve the forecast at the requested location for the next 15 days.

## Date Range Request Example
The following will retrieve the weather data for London, UK from October 1st, 2020 to December 31st, 2020 (inclusive).

https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London,UK/2020-10-01/2020-12-31?key=YOUR_API_KEY 

## Specific Time Request Example
The following will retrieve the weather data for London, UK for the 15th December 2020 and will request the current conditions property be populated using the conditions at 13:00 local time (1pm local time).

https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London,UK/2020-12-15T13:00:00?key=YOUR_API_KEY 

## Dynamic period Request Example
Rather the specify and date range, you can also specify and dynamic period. A request based on a dynamic period will automatically adjust based on the period. In this example, we will use the dynamic period value “last30days” to retrieve data for the most recent 30 days.

https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London,UK/last30days?key=YOUR_API_KEY 

## Typical JSON response format
All Timeline Weather API requests return response JSON in the same format. Here is an example for Reston, VA on 11/12/2020:
``` JSON
{
     "latitude" : 38.9697,
     "longitude" : -77.385,
     "resolvedAddress" : "Reston, VA, United States",
     "address" : " Reston,VA",
     "timezone" : "America/New_York",
     "tzoffset" : -5, 
     "description":"Cooling down with a chance of rain on Friday.", 
     "days" : [{ //array of days of weather data objects
         "datetime":"2020-11-12",
         "datetimeEpoch":1605157200,
         "temp" : 59.6,
         "feelslike" : 59.6,
         ...
         "stations" : {
         },
         "source" : "obs",
         "hours" : [{  //array of hours of weather data objects  
             "datetime" : "01:00:00",
             ...
         },...]
     },...],
     "alerts" : [{
             "event" : "Flash Flood Watch",
             "description" : "...",
             ...
         }
     ],
     "currentConditions" : {
         "datetime" : "2020-11-11T22:48:35",
         "datetimeEpoch" : 160515291500,
         "temp" : 67.9,
         ...
     }
}
```
