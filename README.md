# List Sum RestAPI Endpoint

## Auto-generated Swagger Docs

Run flask service and see root directory for automatically generated swagger documentation

## Usage

All responses will have the form of a JSON response with a tag of 'Total' followed the sum result


```json
{
  "Total": "Sum integer value of the list passed"
}
```

## Responses Overview

### GET Default List Sum Result

**Definition**
`GET /total`

**Response**
 - `200 OK` on success
 - `400 BAD` on invalid list being passed
 
 NB: Default list function ```numbers = list(range(10000001))``` provides sum result as seen below
 
 ```json
{
  "Total": "50000005000000"
}
```

### POST New List and Return Sum

**Definition**
`POST /total`
 
**Arguments**
 - `"List":list` a list of integers to be summed
 
  ```json
{
  "List": "[1, 2, 3]"
}
```
 
 **Response**
 - `200 OK` on success
 - `400 BAD` on invalid list being passed

 
 ```json
{
  "Total": "6"
}
```

## Assumptions
List passed is assumed to only contain integers and no floats. Although, basic error handling has been put in place.
