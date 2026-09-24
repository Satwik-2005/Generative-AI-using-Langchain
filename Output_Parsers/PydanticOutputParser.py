from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import Field, BaseModel

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

class Person(BaseModel):
    name: str = Field(description="Name of the Person")
    age: int = Field(gt = 18, description="Age of the Person")
    city: str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = "Generate the name, age, city of a fictional {place} person \n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser
final_result = chain.invoke({'place': "Indian"})

print(final_result)