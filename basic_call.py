import boto3, json

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')

message_list = []

initial_message = {
    "role": "user",
    "content": [
        { "text": "How are you today?" } 
    ],
}

message_list.append(initial_message)

response = bedrock.converse(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=message_list,
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 0
    },
)

#Step 1:
response_message = response['output']['message']
print(json.dumps(response_message, indent=4))

#Step 2:
#message_list.append(response_message)
#print(json.dumps(message_list, indent=4))

