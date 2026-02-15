from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a simple note on  {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Genrate 5 short question answer quiz from : {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided note and quiz into single document \n note -> {note} and quiz -> {quiz}',
    input_variables=['note','quiz']
)

model1 = ChatOpenAI()
model2 = ChatOpenAI()


parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'note': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain


text = '''
A prompt is a natural language input—such as a question, instruction, or text snippet—submitted to a generative AI model to initiate a response. Prompts serve as the foundational mechanism for human-AI interaction, guiding models to generate text, code, images, or data analysis. The effectiveness of a prompt directly determines the relevance and quality of the AI's output, with more descriptive, context-rich prompts producing better results. 
Google Cloud
Google Cloud
 +4
Core Components of an Effective Prompt
Well-structured prompts often include the following elements: 
Parloa
Parloa
 +2
Directive: A specific command or question (e.g., "Summarize," "Write," "Analyze").
Context: Background information that helps the model understand the scenario.
Role (Persona): Assigning a persona (e.g., "Act as a Python expert") to guide the tone and expertise level.
Input Data: The specific content to be processed (e.g., the text to be summarized).
Output Formatting: Guidelines for how the output should look (e.g., "in a table," "using bullet points," "within 100 words"). 
Google Cloud
Google Cloud
 +6
'''
result = chain.invoke({'text':text})
print(result)
chain.get_graph().print_ascii()