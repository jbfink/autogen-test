import autogen  # start importing the autogen list

config_list = [
    {
        "model": "mistral-instruct-7b",  # the name of your running model
        "api_base": "http://127.0.0.1:8081/v1",  # the local address of the api server
        "api_type": "open_ai",
        "api_key": "sk-1111111111111111111111111111111111111111111",  # some nonsense 'cos we don't want openai, no no
    }
]
# create an ai AssistantAgent named "assistant"
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={
        "seed": 42,  # seed for caching and reproducibility
        "config_list": config_list,  # a list of OpenAI API configurations
        "temperature": 0,  # temperature for sampling
        "request_timeout": 400,  # timeout
    },  # configuration for autogen's enhanced inference API which is compatible with OpenAI API
)

# create a human UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config=False,
    
)

# the assistant receives a message from the user_proxy, which contains the task description
user_proxy.initiate_chat(
    assistant,
    message="""Create a posting schedule with captions in instagram for a week and store it in a .csv file.""",
)
