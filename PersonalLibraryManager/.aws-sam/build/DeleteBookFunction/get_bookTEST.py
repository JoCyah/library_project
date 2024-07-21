import json
import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Books')

def lambda_handler(event, context):
    """
    Lambda function to retrieve a book from the Books table in DynamoDB.

    Parameters:
    event (dict): The event dictionary containing the book ID in the query string parameters.
    context (object): The context object containing runtime information.

    Returns:
    dict: The response dictionary with the status code and book details.
    """
    # Get the book ID from the query string parameters
    
    
    message = 'Hello World!'
    if 'queryStringParameters' in event:
        if event['queryStringParameters'] is not None:
            if 'book_id' in event['queryStringParameters']:
                if event['queryStringParameters']['book_id'] is not None:
                    book_id = event['queryStringParameters']['book_id']
                    message = book_id
    
    # Retrieve the book from the DynamoDB table
    #response = table.get_item(
     #   Key={
      #      'book_id': book_id
       # }
    #)
    response = message
    # Return the book details in the response
    return {
        'statusCode': 200,
        'body': response
    }
