import json
import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Books')

def lambda_handler(event, context):
    """
    Lambda function to update a book in the Books table in DynamoDB.

    Parameters:
    event (dict): The event dictionary containing the book details in the body.
    context (object): The context object containing runtime information.

    Returns:
    dict: The response dictionary with the status code and message.
    """
    # Parse the request body
    body = json.loads(event['body'])
    book_id = body['book_id']
    title = body['title']
    author = body['author']
    cover_image = body['cover_image']
    
    # Update the book details in the DynamoDB table
    table.update_item(
        Key={
            'book_id': book_id
        },
        UpdateExpression="set title=:t, author=:a, cover_image=:c",
        ExpressionAttributeValues={
            ':t': title,
            ':a': author,
            ':c': cover_image
        }
    )
    
    # Return a success response
    return {
        'statusCode': 200,
        'body': json.dumps('Book updated successfully!')
    }
