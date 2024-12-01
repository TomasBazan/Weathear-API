from rest_framework.response import Response


def check_response_for_errors(r):
    if r.status_code == 400:
        return Response({"message": "Bad Request, check your parameters"},
                        status=400)
    elif r.status_code == 401:
        return Response(
            {"message": "Internal server error while comunacting with the API"},
            status=401
        )
    elif r.status_code == 404:
        return Response({"message": "Not endpoint found"}, status=404)
    elif r.status_code == 429:
        return Response({"message": "Too many requests"}, status=429)
    elif r.status_code == 500:
        return Response({"message": "Internal third-party server error"},
                        status=500
                        )
    else:
        return Response(r.json())
