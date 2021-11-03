import os
import time

from azure.cognitiveservices.knowledge.qnamaker.authoring import QnAMakerClient
from azure.cognitiveservices.knowledge.qnamaker.runtime import QnAMakerRuntimeClient
from azure.cognitiveservices.knowledge.qnamaker.authoring.models import QnADTO, MetadataDTO, CreateKbDTO, OperationStateType, UpdateKbOperationDTO, UpdateKbOperationDTOAdd, EndpointKeysDTO, QnADTOContext, PromptDTO
from azure.cognitiveservices.knowledge.qnamaker.runtime.models import QueryDTO
from msrest.authentication import CognitiveServicesCredentials



subscription_key = '4487b2f054b54fc68d6aefae4af48f68'

authoring_endpoint = 'https://margie-qna-maker-joy.cognitiveservices.azure.com/'

runtime_endpoint = 'https://margie-qna-maker-joy.azurewebsites.net'

client = QnAMakerClient(endpoint=authoring_endpoint, credentials=CognitiveServicesCredentials(subscription_key))

def getEndpointKeys_kb(client):
    #print("Getting runtime endpoint keys...")
    keys = client.endpoint_keys.get_keys()
    #print("Primary runtime endpoint key: {}.".format(keys.primary_endpoint_key))

    return keys.primary_endpoint_key

def generate_answer(client, kb_id, runtimeKey, question):
    print ("Querying knowledge base...")

    authHeaderValue = "EndpointKey " + runtimeKey

    listSearchResults = client.runtime.generate_answer(kb_id, QueryDTO(question = question), dict(Authorization=authHeaderValue))

    for i in listSearchResults.answers:
        print(f"Answer ID: {i.id}.")
        print(f"Answer: {i.answer}.")
        print(f"Answer score: {i.score}.")


if __name__ == '__main__':

    question = input('Enter a query for Margie Travel: ')
    queryRuntimeKey  = getEndpointKeys_kb(client)
    runtimeClient = QnAMakerRuntimeClient(runtime_endpoint=runtime_endpoint, credentials=CognitiveServicesCredentials(queryRuntimeKey))

    kb_id = '80914be3-f45f-4e91-b4de-c35f66191f02'

    # answer = generate_answer(client=client, kb_id=kb_id, runtimeKey=queryRuntimeKey)

    runtimeClient = QnAMakerRuntimeClient(runtime_endpoint=runtime_endpoint, credentials=CognitiveServicesCredentials(queryRuntimeKey))
    generate_answer(client=runtimeClient,kb_id=kb_id,runtimeKey=queryRuntimeKey, question=question)




