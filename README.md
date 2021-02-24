EASi Django API

To get this thing up and running...

```
brew install python3
python3 manage.py migrate
python3 manage.py loaddata systems
python3 manage.py runserver
```

From there, you can play with graphQL by visiting `http://localhost:8000/graphql`

Sample query:
```
query {
  allAccessibilityRequests{
    name
    id
    system {
      name
    }
    dates {
      date
      score
    }
  }
}
```