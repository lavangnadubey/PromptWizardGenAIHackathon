pip install --upgrade google-cloud-aiplatform

gcloud auth application-default login

import base64
import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting, Part


def multiturn_generate_content():
    model = GenerativeModel(    vertexai.init(project="", location="us-central1")

        "gemini-1.5-flash-001",
        system_instruction=[textsi_1]
    )
    chat = model.start_chat()
    print(chat.send_message(
        ["""I spent 20000 on bananas , 50000 on AC bill and 20000 on  new hanky"""],
        generation_config=generation_config,
        safety_settings=safety_settings
    ))
    print(chat.send_message(
        ["""I earn Rs80000 per month. I spent 200 on banana, 4000 on salon, 5000 on buying OTT subscripotion"""],
        generation_config=generation_config,
        safety_settings=safety_settings
    ))
    print(chat.send_message(
        ["""I earn Rs80000 per month. I spent 200 on banana, 4000 on salon, 5000 on buying OTT subscripotion"""],
        generation_config=generation_config,
        safety_settings=safety_settings
    ))
    print(chat.send_message(
        ["""I earn Rs80000 per month. I spent 200 on banana, 4000 on salon, 5000 on buying OTT subscripotion"""],
        generation_config=generation_config,
        safety_settings=safety_settings
    ))
    print(chat.send_message(
        ["""I earn Rs80000 per month. I spent 200 on banana, 4000 on salon, 5000 on buying OTT subscripotion"""],
        generation_config=generation_config,
        safety_settings=safety_settings
    ))
    print(chat.send_message(
        ["""I earn Rs80000 per month. I spent 200 on banana, 4000 on salon, 5000 on buying OTT subscripotion"""],
        generation_config=generation_config,
        safety_settings=safety_settings
    ))
    print(chat.send_message(
        ["""I earn Rs80000 per month. I spent 200 on banana, 4000 on salon, 5000 on buying OTT subscripotion"""],
        generation_config=generation_config,
        safety_settings=safety_settings
    ))
    print(chat.send_message(
        ["""I earn Rs80000 per month. I spent 200 on banana, 4000 on salon, 5000 on buying OTT subscripotion"""],
        generation_config=generation_config,
        safety_settings=safety_settings
    ))
    print(chat.send_message(
        ["""I earn Rs80000 per month. I spent 200 on banana, 4000 on salon, 5000 on buying OTT subscripotion"""],
        generation_config=generation_config,
        safety_settings=safety_settings
    ))
    print(chat.send_message(
        [text10_1],
        generation_config=generation_config,
        safety_settings=safety_settings
    ))
    print(chat.send_message(
        ["""I earn Rs80000 per month. I spent 200 on banana, 4000 on salon, 5000 on buying OTT subscripotion"""],
        generation_config=generation_config,
        safety_settings=safety_settings
    ))

text10_1 = """Make a pie chart of my budget: 50% for savings, 20% for investments, 15% for rent, and 15% for leisure."""
textsi_1 = """you are a helpful financial bot whose job is to categories expense into [\'shopping\' , \'education\' ,  \'travel\', \'food\' , \'health\' ,\'utility bills\' ,\'investment\', \'entertainment\' ] .
After categorization provide financial advice to me including how much proportion I can save maximum. Give advice what expenses I can cut off .
finish each answer with a visual representation -pie chart .
Give a link to download pdf file with all the details generated.
Currency is in INR"""

generation_config = {
    "max_output_tokens": 4338,
    "temperature": 0.7,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
]

multiturn_generate_content()