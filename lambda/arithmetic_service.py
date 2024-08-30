import json
from functools import reduce
from http import HTTPStatus

def handler(event, context):
    try:
        path = event['path']
        query_string = event.get('queryStringParameters', {})

        if not query_string or 'numbers' not in query_string:
            return response("No query parameters provided or 'numbers' parameter missing", HTTPStatus.BAD_REQUEST)

        # Convert the 'numbers' query parameter to a list of integers
        try:
            numbers = list(map(int, query_string['numbers'].split(',')))
        except ValueError:
            return response("Invalid input. Please provide numeric values.", HTTPStatus.BAD_REQUEST)

        # Handle arithmetic operations based on the path
        if path == "/v1/add":
            result = sum(numbers)
        elif path == "/v1/subtract":
            result = reduce(lambda x, y: x - y, numbers)
        elif path == "/v1/multiply":
            result = reduce(lambda x, y: x * y, numbers)
        elif path == "/v1/divide":
            if 0 in numbers[1:]:
                return response("Division by zero error", HTTPStatus.BAD_REQUEST)
            result = reduce(lambda x, y: x // y, numbers)
        else:
            return response("Invalid operation", HTTPStatus.NOT_FOUND)

        return response({"result": result}, HTTPStatus.OK)
    
    except Exception as e:
        return response(f"Internal server error: {str(e)}", HTTPStatus.INTERNAL_SERVER_ERROR)

def response(message, status_code):
    return {
        "statusCode": status_code,
        "body": json.dumps(message),
        "headers": {
            "Content-Type": "application/json"
        }
    }
