from rest_framework.decorators import api_view
from rest_framework.response import Response
import pymongo

# Endpoint to create a new collection
@api_view(['POST'])
def create_collection(request):
    collection_name = request.data.get('collection_name')

    if not isinstance(collection_name, str):
        return Response({'message': 'Collection name should be a string'}, status=400)

    url = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(url)
    db = client['newdatabase']

    try:
        db.create_collection(collection_name)
        return Response({'message': f'Collection {collection_name} created successfully'})
    except Exception as e:
        return Response({'message': f'Error creating collection: {str(e)}'}, status=500)

# Endpoint to add questions to a collection
@api_view(['POST'])
def add_questions(request):
    collection_name = request.data.get('collection_name')  # Get the collection/form name
    questions = request.data.get('questions')  # Get questions data from frontend

    # Connect to MongoDB and access the specified collection
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client['newdatabase']
    collection = db[collection_name]

    # Insert questions into the collection
    collection.insert_many(questions)

    return Response({'message': f'Questions added to {collection_name} collection successfully'})
