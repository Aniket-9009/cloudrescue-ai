import boto3
from botocore.exceptions import ClientError

session = boto3.Session(
    profile_name="cloudrescue",
    region_name="ap-south-1"
)

bedrock = session.client("bedrock-runtime")

MODEL_ID = "apac.amazon.nova-micro-v1:0"

try:
    response = bedrock.converse(
        modelId=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": (
                            "You are CloudRescue AI, an AWS networking assistant. "
                            "Explain in 3 short sentences why SSH connection "
                            "to an EC2 instance might fail."
                        )
                    }
                ]
            }
        ],
        inferenceConfig={
            "maxTokens": 150,
            "temperature": 0.3
        }
    )

    answer = response["output"]["message"]["content"][0]["text"]

    print("\nCloudRescue AI Response:\n")
    print(answer)

except ClientError as error:
    print("\nAWS Error:")
    print(error.response["Error"]["Code"])
    print(error.response["Error"]["Message"])
