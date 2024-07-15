import json
import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Books')

def lambda_handler(event, context):
    """
    Lambda function to delete a book from the Books table in DynamoDB.

    Parameters:
    event (dict): The event dictionary containing the book ID in the query string parameters.
    context (object): The context object containing runtime information.

    Returns:
    dict: The response dictionary with the status code and message.
    """
    # Get the book ID from the query string parameters
    book_id = event['queryStringParameters']['book_id']
    
    # Delete the book from the DynamoDB table
    table.delete_item(
        Key={
            'book_id': book_id
        }
    )
    
    # Return a success response
    return {
        'statusCode': 200,
        'body': json.dumps('Book deleted successfully!')
    }
