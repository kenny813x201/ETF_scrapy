import boto3


class DynamoDB_connection():

	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('etf')

	def add_doc(self, item):
		self.table.put_item(Item=dict(item))
