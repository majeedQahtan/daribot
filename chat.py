#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import ast
import gradio as gr
import tqdm as notebook_tqdm


# In[2]:


import pandas as pd


# In[3]:


#url = "https://experimental.willow.vectara.io/v1/chat/completions"
url = "https://api.vectara.io/exp/query-and-interpret"


# In[4]:


headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}


# In[6]:


def chatbot(input):
    if input:
        payload = json.dumps({
  "query": [
    {
      "query": "{}".format(input),
      "numResults": 5,
      "corpusKey": [
        {
          "customerId": 0,
          "corpusId": 2
        }
      ]
    }
  ]
})
        
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.json())
        reply_paraphrased = response.json()['responseSet'][0]['generated'][0]['text']
        reply = response.json()['responseSet'][0]['response'][0]['text']
        
        print(reply_paraphrased)
        
        if reply_paraphrased == "":
            return reply
        else :
            return reply_paraphrased

inputs = gr.inputs.Textbox(lines=7, label="دردش مع داري")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="داري شات بوت",
             #description="أسال ما تشاء",
             theme="compact").launch(share=True)


# In[ ]:





# In[ ]:




