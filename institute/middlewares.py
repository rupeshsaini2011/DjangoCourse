from django.db import connection

class SchemaMiddleware:
  def __init__(self, get_response):
    self.get_response=get_response
  

  def __call__(self, request):
    host=request.get_host()
    print(host)
    if "localhost" in host:
      schema=host.split("localhost:8000")
      print(schema)
      schema=schema[0]
      if schema == "":
        schema="public"
      else:
        schema =schema.split(".")[0]
      print(schema)
      
      with connection.cursor() as cursor:
        cursor.execute(f"set search_path to {schema}")

    response=self.get_response(request)
    return response