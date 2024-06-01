# About
Server side event example on Django and Graphql


# To install
```
pip3 install django graphene-django
```

# To run server
```
python3 manage.py makemigrations sse_app
python3 manage.py migrate
python3 manage.py runserver
```

# To view the server-sent events in action
```
http://127.0.0.1:8000/events/
```

# To access GraphQL Playground
```
http://127.0.0.1:8000/graphql/
```

# To add example modal
```
mutation {
  createMyModel(name: "Test Name", description: "Test Description") {
    myModel {
      id
      name
      description
    }
  }
}
```


# To query all modal
```
query MyQuery {
  allModels {
    description
    id
    name
  }
}
```