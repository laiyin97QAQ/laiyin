# -*- coding: utf-8 -*-
# @Time    : 9/16/2024 10:56 PM
# @Author  : WAN Yuwei
# @FileName: yinli.py
# @Email: yuweiwan2-c@my.cityu.edu.hk
# @Github: https://github.com/yuweiwan
# @Personal Website: https://yuweiwan.github.io/
import os
from openai import AzureOpenAI
import json

os.environ["AZURE_OPENAI_KEY"] = "e07957b2e03e42a08f2be47cd906ebf0"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://gd-canada-openai.openai.azure.com//"


def chatbot(question, prompt):
    # model = "gpt-35-0125"
    model = "gpt-4-1106"

    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        api_version="2024-02-01",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )

    response = client.chat.completions.create(
        model=model,  # model = "deployment_name".
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt + str(question)}
        ]
    )

    return response.choices[0].message.content



prompt = "Use short sentence to answer the question: "
question_list = ['What do you eat for lunch', 'who are you', 'when do you sleep', '你是一个好人吗']
for i in range(4):
    answer = chatbot(question_list[i], prompt)
    print(answer)