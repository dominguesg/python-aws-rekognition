import boto3
import time


def stop_model(model_arn):

    client=boto3.client('rekognition')

    print('Stopping model:' + model_arn)

    #Stop the model
    try:
        response=client.stop_project_version(ProjectVersionArn=model_arn)
        status=response['Status']
        print ('Status: ' + status)
    except Exception as e:  
        print(e)  

    print('Done...')
    
def main():
    
    model_arn='arn:aws:rekognition:us-east-2:738018119147:project/light-ml-1/version/light-ml-1.2023-08-16T15.42.01/1692211322338'
    stop_model(model_arn)

if __name__ == "__main__":
    main() 