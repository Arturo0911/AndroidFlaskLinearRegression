scikit-learn = "*"
flask = "*"
flask-script = "*"
pandas = "*"
numpy = "*"
seaborn = "*"
graphene = "*"
flask-graphql = "*"
pymongo = "*"
flask-pymongo = "*"
requests = "*"
flask-mongoengine = "*"
graphene-mongo = "*"
graphene-mongodb = "*"
flask-migrate = "*"




./gradlew downloadApolloSchema \
  --endpoint="http://127.0.0.1:5000/graphql" \
  --schema="schema.json"
