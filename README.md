#List Sum RestAPI Endpoint

## Usage

All responses will have the form of a JSON response with a tag of 'Total' followed the sum result


```json
{
  "Total": "Sum integer value of the list passed"
}
```

##Responses Overview

###GET List Sum Result

**Definition**
`GET /total`

**Response**
 - `200 OK` on success
 
 NB: If list elements were [1, 2, 3], response of
 
 ```json
{
  "Total": "6"
}
```