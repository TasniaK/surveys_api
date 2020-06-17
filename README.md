# surveys_api
A python (3.7) flask app that stores data about surveys and responses to surveys.

## Using this API

### Setup
If you want to run this locally, git clone the repo, and then `make run`.

### Surveys
The `/surveys` endpoint can either be used to create a new survey or list all current surveys.

Example post request to `/surveys` to create a survey
```shell
curl -d '{"name": "Opinions about apples", "available_places": 30, "user_id": 5438}' -H "Content-Type: application/json" -X POST http://127.0.0.1/surveys
```

Example get request to `/surveys` to list all surveys
```shell
curl -X GET http://127.0.0.1/surveys
```


### Survey Responses
The `/survey-responses` endpoint can be used to create a survey response.

Example post request to `/survey-responses` to create a survey response
```shell
curl -d '{"survey_id": 7944, "user_id": 6211}' -H "Content-Type: application/json" -X POST http://127.0.0.1/survey-responses
```


### Testing

Enter the image:
```shell
make docker-enter
```

Add `make`:
```shell
apk add make
```

Then run:
```shell
make test
```

## Process used
