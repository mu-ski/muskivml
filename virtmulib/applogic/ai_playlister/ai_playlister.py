# import os
# import replicate

# os.environ["REPLICATE_API_TOKEN"] = "r8_Ov0OC3rWmSvfRhp6DHhh694DgF2UhT40dZEIt"
# os.environ["REPLICATE_POLL_INTERVAL"] = "0.05"

# output = replicate.run(
#   "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
#   input={
#     "debug": False,
#     "top_k": 50,
#     "top_p": 1,
#     "prompt": "How many stars are in out galaxy?",
#     "temperature": 0.5,
#     "system_prompt": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
#     "max_new_tokens": 500,
#     "min_new_tokens": -1,
# #    "max_length":128,
# #    "repetition_penalty":1
#   }
# )
# #print(output)


# full_response = ""

# for item in output:
#   full_response += item

# print(full_response)


# Response of above code::
# The number of stars in our galaxy, the Milky Way, is estimated to be between 200 and 400 billion. 
# However, it's important to note that this estimate is based on current scientific knowledge and may change as new discoveries are made. 
# Additionally, it's difficult to give an exact number because some stars are too distant or too faint to be detected by current telescopes.


import os
import pkgutil
from langchain.llms.replicate import Replicate
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import LLMChain
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)

path = "virtmulib.applogic.ai_playlister"
setup = None
try :
    setup = pkgutil.get_data(path, "llm-setup-secret")
except FileNotFoundError:
    setup = pkgutil.get_data(path, "llm-setup")
setup = setup.decode('utf-8')


# from dotenv import load_dotenv

# Load environment variables
# load_dotenv()            
REPLICATE_API_TOKEN = "r8_Ov0OC3rWmSvfRhp6DHhh694DgF2UhT40dZEIt"

os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

#llm_model ="meta/llama-2-7b-chat:13c3cdee13ee059ab779f0291d29054dab00a47dad8261375654de5540165fb0"
llm_model ="meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3"
#llm_model ="meta/llama-2-13b-chat:f4e2de70d66816a838a89eeeb621910adffb0dd0baba3976c96980970978018d"

temperature = 0.80
top_p = 0.9
max_length = 128
#top_k = 50
max_new_tokens = 800
min_new_tokens = -1
repetition_penalty = 1
debug = False



llm = Replicate(
    model=llm_model,
    #replicate_api_token=REPLICATE_API_TOKEN,
    streaming=False,
    model_kwargs={
        "temperature": temperature, "max_length": max_length, "top_p": top_p,
        "max_new_tokens": max_new_tokens, "min_new_tokens": min_new_tokens, 
        "repetition_penalty": repetition_penalty, "debug": debug,
        #"top_k": top_k
    },
)


prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            setup
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question},")
    ]
)

memory = ConversationBufferWindowMemory(
    memory_key="chat_history", return_messages=True, k=2,key="question"
)

conversation = LLMChain(llm=llm, prompt=prompt, verbose=True, memory=memory)

chat_history = []

#user_query = st.text_input('You:', '')
#user_query = 'How many stars are in the solar system?'

user_query = """
Top artists: Mos Def, Laika, Miles Davis, 
Top songs: Herbie Hancock - Maiden Voyage, Laika - Praire Dog
What music means to me: Music is what I listen to when I need to discover new feelings and new imagination
Liked Music: I like many kinds of music, as long as its creative, emotional, and midtempo. I like world music, I like african american music in general.
Music not liked: I typically don't like rock music, but there are exceptions, typically open-minded artists that are self-conscious of the role of the west in colonalism.
Playlist request: It is a nice sunny sunday in december and I would like to listen to some creative and relaxed world music
"""
#if user_query:
#user_response = {"role": "user", "content": user_query}
#chat_history.append(user_response)

response = conversation({"question": user_query})
bot_response = response["text"]
bot_response = {"role": "bot", "content": bot_response}
chat_history.append(bot_response)

response = bot_response['content']

from ast import literal_eval

print(literal_eval(response))



# Response of above code::
# Ah, a question that has puzzled astronomers for centuries!
# The solar system, as you know, consists of eight planets: 
# Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. 
# However, there are no stars in the solar system. The sun, which is the center of our solar system, is actually a star itself! 
# So, the answer to your question is: there are zero stars in the solar system!