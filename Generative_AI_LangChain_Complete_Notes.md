# 🤖 Generative AI & LangChain --- Complete Learning Notes

> Beginner-friendly notes covering Generative AI, LangChain, LLMs,
> prompts, structured output, chains, RAG, embeddings, vector stores,
> retrievers, tools, and AI agents.

## 🧭 How to Use These Notes

-   📘 Read each topic in order to build concepts step by step.
-   🔄 Follow the flowcharts to understand how components connect.
-   🧪 Try the code examples in your own Python virtual environment.
-   🌍 Relate each concept to the real-world examples.
-   📝 Use the **Key Takeaway** sections for quick revision.

## 🗺️ Overall Learning Roadmap

``` mermaid
flowchart TD
    A[Generative AI] --> B[LLMs and Models]
    B --> C[Prompts and Prompt Templates]
    C --> D[Structured Output and Parsers]
    D --> E[Chains]
    E --> F[RAG]
    F --> G[Indexing]
    G --> H[Document Loading]
    H --> I[Text Splitting]
    I --> J[Embeddings]
    J --> K[Vector Stores]
    K --> L[Retrievers]
    L --> M[Augmentation]
    M --> N[Generation]
    N --> O[Tools]
    O --> P[AI Agents and ReAct]
    P --> Q[Local Models with Ollama]
```

## 📚 Table of Contents

-   [1. What do you mean by Generative AI](#q1)
-   [2. Generative AI impact areas](#q2)
-   [3. How to Learn GENAI](#q3)
-   [4. What do you mean by Langchain](#q4)
-   [5. How Langchain works](#q5)
-   [6. Benefits of Langchain .](#q6)
-   [7. What can you build using Langchain](#q7)
-   [8. What are the components of Langchain](#q8)
-   [9. What are the language models supported by Langchain](#q9)
-   [10. What are Models](#q10)
-   [11. What are Language Models](#q11)
-   [12. What are Prompts](#q12)
-   [13. Wht do you mean by Prompt Template](#q13)
-   [14. Why use Prompt Template over f' strings](#q14)
-   [15. What is a Message Placeholder](#q15)
-   [16. Structured Output](#q16)
-   [17. Why do we need Structured Output](#q17)
-   [18. Ways to get Structured Output](#q18)
-   [19. What are output parsers](#q19)
-   [20. What are Chains and why do we use it](#q20)
-   [21. What is RAG (Retrieval Argumented Generation)](#q21)
-   [22. What do you mean by Document Loaders](#q22)
-   [23. What do you mean by Text Splitters](#q23)
-   [24. What is Length Based Text Splitting Technique](#q24)
-   [25. What is Recursive Text Splitting Technique](#q25)
-   [26. What is Document-Structure-Based Text Splitting
    Technique](#q26)
-   [27. What is Semantic Meaning-Based Text Splitting Technique](#q27)
-   [28. What are Vector Stores](#q28)
-   [29. What are Vector Stores](#q29)
-   [30. Vector Stores in LangChain](#q30)
-   [31. What is Chroma DB](#q31)
-   [32. What are Retrievers](#q32)
-   [33. What is Website Retriever](#q33)
-   [34. What is Vector Store Retriever](#q34)
-   [35. What is Maximum Marginal Relevance (MMR)](#q35)
-   [36. What is Multi Query Retriever](#q36)
-   [37. What is Contextual Compression Retriever](#q37)
-   [38. What is Retrieval Argumented Generation](#q38)
-   [39. What is Finetuning](#q39)
-   [40. What is In-Context Learning](#q40)
-   [41. How does RAG works](#q41)
-   [42. What do you mean by Indexing in RAG](#q42)
-   [43. What do you mean by Retrievers in RAG](#q43)
-   [44. What do you mean by Argumentation](#q44)
-   [45. What do you mean by Generation in RAG](#q45)
-   [46. What are Tools](#q46)
-   [47. What are Builtin Tools](#q47)
-   [48. What are Custom Tools](#q48)
-   [49. What do you mean by ToolKit](#q49)
-   [50. What is Tool Binding](#q50)
-   [51. What is Tool Calling](#q51)
-   [52. What do you mean by AI Agent](#q52)
-   [53. What is ReAct](#q53)
-   [54. What is Agent and Agent Executor](#q54)
-   [55. Difference between Proprietory models and Opensource
    Models](#q55)
-   [56. What is Ollama and what are its characterstics](#q56)

## 1. What do you mean by **Generative AI** ?

**Generative AI** is a type of AI that creates new content, such as
**text**, **images**, **music**, or **code**, by learning patterns from
existing data, mimicking human creativity.

------------------------------------------------------------------------

## 2. Generative AI impact areas

**Generative AI** has a significant impact on various industries,
including:

-   **Customer Service**: AI chatbots and virtual assistants can
    generate human-like responses, improving customer interactions.

-   **Content Creation**: AI can assist in writing articles, creating
    marketing materials, and generating multimedia content.

-   **Software Development**: AI can help in code generation, bug
    fixing, and automating repetitive coding tasks.

-   **Education**: AI can create personalized learning materials,
    quizzes, and educational content tailored to individual student
    needs.

------------------------------------------------------------------------

## 3. How to Learn **GENAI** ?

To learn GENAI, you should follow these steps:

-   **Transformer Architecture**: Understand the architecture of
    transformer models, which are the backbone of many generative AI
    systems.

-   **Pre-trained Models**: Explore pre-trained models like GPT, BERT,
    and DALL-E to understand how they generate content.

-   **Optimization Techniques**: Learn about optimization techniques
    used in training generative models, such as gradient descent and
    backpropagation.

-   **Fine-tuning**: Practice fine-tuning pre-trained models on specific
    datasets to improve their performance for particular tasks.

-   **Evaluation And Deployment**: Learn how to evaluate the performance
    of generative models and deploy them in real-world applications.

-   **Prompt Engineering**: Understand how to craft effective prompts to
    guide generative models in producing desired outputs.

-   **RAG (Retrieval-Augmented Generation)**: Learn how to combine
    generative models with retrieval systems to enhance the quality and
    relevance of generated content.

-   **AI agents**: Explore the concept of AI agents that can
    autonomously perform tasks and make decisions based on generative AI
    capabilities.

-   **Hands on Projects**: Engage in hands-on projects to apply your
    knowledge and gain practical experience in building generative AI
    applications.

------------------------------------------------------------------------

## 4. What do you mean by **Langchain** ?

**Langchain** is an open source framework that helps in building **LLM**
based applications. It provides modular components and end-to-end tools
that helps developers build complex AI applications, such as chatbots,
question-answering systems, retrirval-argumented generations (RAG),
automated agents and more.

-   Supports all the major LLMs

-   Simplifies developing LLM based applications

-   Integration available for all major tools

-   Open Source / Free / Actively developed

-   Supports all major GENAI use cases

------------------------------------------------------------------------

## 5. How Langchain works ?

                      PDF → S3 → Document Loader → Text Splitter
                              ↓
                         Embeddings
                              ↓
                          Database
                              ↑
             User Query → Embedding → Semantic Search
                              ↓
                       Relevant Pages
                              ↓
                  System Query + User Query
                              ↓
                           LLM
                              ↓
                       Final Output 

------------------------------------------------------------------------

## 6. Benefits of Langchain .

There are several benefits of using Langchain for building LLM-based
applications: - **Concept of Chains**: Langchain allows developers to
create chains of prompts and responses, enabling more complex
interactions with LLMs.

-   **Model agnostic development**: Langchain supports multiple LLMs,
    allowing developers to switch between models without significant
    changes to their code.

-   **Complete ecosystem**: Langchain provides a complete ecosystem for
    building LLM-based applications, including tools for data loading,
    prompt management, and model deployment.

-   **Memory and state handling**: Langchain provides mechanisms for
    managing memory and state across interactions, enabling more
    context-aware applications.

------------------------------------------------------------------------

## 7. What can you build using Langchain ?

-   Conversational chatbots
-   AI knowledge assistants
-   AI agents
-   Workflow Automation
-   Summarization / reaserch helpers

------------------------------------------------------------------------

## 8. What are the components of **Langchain** ?

Langchain consists of the following components:

                                                1. Models
                                                      ↑
                                                      │
                        6. Agents  ←──────────  LangChain  ──────────→  2. Prompts 
                                                      │
                                                      ↓
                                                3. Chains
                                                      ↓
                                                4. Memory
                                                      ↓
                                                5. Indexes

-   **Models**: In langchain **models** are the core interfaces through
    which you interact with **AI models**.

-   **Prompts**: In langchain **prompts** are are the inputs provided to
    the LLMsto generate the desired outputs. There are some types of
    prompts\

        - **Dynamic and Resuable Prompts**: These are the prompts used by the developers to give the random input to the LLM 
          and expect desired response. These prompts can be reused in the future for other LLMs. 

          --------------------------------------------------------------------

              Example: 

                    from langchain_core.prompts import PromptTemplate
                    prompt = PromptTemplate.from_template("Summarize {topic} in {emotion} tone.")

                    print(prompt.format(topic="Cricket", emotion="funny"))

              Output: Summarize cricket in funny way.

          -------------------------------------------------------------------------

        - **Role - based Prompts**: These are the prompts that define the role or persona of the AI model, allowing it to 
          respond in a specific way based on the assigned role.

           -------------------------------------------------------------------

              Example:

                    from langchain_core.prompts import ChatPromptTemplate
                    prompt = ChatPromptTemplate.from_template([
                          ("system", "Hi, you are a experienced {profession}"),
                          ("user", "Tell me about {topic}")
                    ])

                    formatted_message = prompt.format_message(profession="doctor", topic="Viral fever")
                    print(formatted_message)

              Output: 
                    [
                      {"role": "system", "content": "Hi, you are a experienced doctor"},
                      {"role": "user", "content": "Tell me about Viral fever"}
                    ]

          --------------------------------------------------------------------

        - **Few-shot Prompts**: These are the prompts that provide a few examples of input-output pairs to guide the model's response. 
          They help the model understand the desired format or style of the output.

          --------------------------------------------------------------------

              Example:

                    from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

                    example_prompt = PromptTemplate.from_template("Input: {input}\nOutput: {output}")
                    examples = [
                        {"input": "Hello", "output": "Hi there!"},
                        {"input": "How are you?", "output": "I'm doing well, thank you!"}
                    ]

                    few_shot_prompt = FewShotPromptTemplate(
                        examples=examples,
                        example_prompt=example_prompt,
                        prefix="Here are some examples:",
                        suffix="Now, please respond to the following input: {user_input}"
                    )

                    formatted_prompt = few_shot_prompt.format(user_input="What's your name?")
                    print(formatted_prompt)

              Output:
                    Here are some examples:
                    Input: Hello
                    Output: Hi there!

                    Input: How are you?
                    Output: I'm doing well, thank you!

                    Now, please respond to the following input: What's your name?

          ----------------------------------------------------------------------------

-   **Chains**: Chains in langchain are used to build the pipelines.
    They help us to connect multiple components together, allowing for
    more\
    complex workflows and interaction with LLMs.

-   **Indexes**: Indexs in langchain are used to connect your
    application to external knowledge sources such as PDFs, websites or
    databases. They help in retrieving the relevant information from the
    sources and provide it to the LLMs.

        - The 4 components in indexes are:

              - Doc Loader: This command is used to load the documents from the external sources.

              - Text Splitter: This command is used to split the documents into smaller chunks for better processing.

              - Vector Store: This command is used to store the vector representation of the documents for efficient retrieval.

              - Retriever: This command is used to retrive the relevant information from the vector store based on the user query.

-   **Memory**: Memory in langchain is used to store the information
    from the previous interactions with the LLMs. Actually LLMs api
    calls are stateless. So langchain provides the memory component to
    store the information from the previous interaction and provide it
    to the LLMs.

        - **Conversational Buffer Memory**: Stores a transcript of recent messages. Great for short chats, but can grow large quickly.

        - **Conversational Buffer Window Memory**: Only keep the last n interactions to avoid excessive token usage.

        - **Summarizer based memory**: Periodically summarizes older chats to keep a acondensed memory footprint.

        - **Custom Memory**: For advanced use cases, you can store specialized state in a custom memory class.

-   **Agents**: Agents in langchain are used to perform the tasks
    automatically.

------------------------------------------------------------------------

## 9. What are the language models supported by **Langchain** ?

There are 2 types of language models supported by langchain. Those are:

-   **Language Models (LLMs)**: These are the core models that generate
    text outputs based on the input text prompts. Eg: OPENAI, Claude,\
    HuggingFace etc.

-   **Embedding Models**: These are the core models that generate vector
    representation of tex inputs. Eg: OPENAI etc.

------------------------------------------------------------------------

## 10. What are **Models**?

-   The **Model** component in langchain is the crucial part of the
    framework, designed to facilitate interactions with various Language
    Models and Embedding Models.

-   It abstracts the complexity of working directly with differnet LLMs,
    chatmodels, and embedding models providing a uniform interface to
    communicate with them. This makes it easier to build applications
    that rely on **AI-generated text**, **Text Embeddings** for
    **similarity search** and **Retrieval Argumented Generation (RAG)**.

                           ┌─────────────┐
                           │    Models   │
                           └──────┬──────┘
                                  │
                      ┌───────────┴───────────┐
                      ▼                       ▼
            ┌──────────────────┐    ┌──────────────────┐
            │ Language Models  │    │ Embedding Models │
            └────────┬─────────┘    └──────────────────┘
                     │
                ┌────┴────┐
                ▼         ▼
          ┌─────────┐  ┌────────────┐
          │  LLMs   │  │ Chat Models│
          └─────────┘  └────────────┘

------------------------------------------------------------------------

## 11. What are **Language Models** ?

-   Language Models are AI systems designed to process, generate, and
    understand natural language text.

            ┌──────────────────┐   
            │ Language Models  │  
            └────────┬─────────┘   
                     │
                ┌────┴────┐
                ▼         ▼
          ┌─────────┐  ┌────────────┐
          │  LLMs   │  │ Chat Models│
          └─────────┘  └────────────┘

-   **LLMs (Large Language Models)**: General purpose models that is
    used for raw text generation. They take a string(or plain text) as
    input and returns a string(or plain text). These are traditional
    older models and are not used much now.

-   **Chat Models**: Language Models that are specialized for
    conversational tasks. They take a sequence of messages as input and
    return chat messages as outputs. They are newer version and used
    more in comparision to the LLMs.

  -----------------------------------------------------------------------
  Feature      LLMs (Base Models)          Chat Models
                                           (Instruction-Tuned)
  ------------ --------------------------- ------------------------------
  Purpose      Free-form text generation   Optimized for multi-turn
                                           conversations

  Training     General text corpora        Fine-tuned on chat datasets
  Data         (books, articles)           (dialogues,

                                           user-assistant conversations)

  Memory &     No built-in memory          Supports structured
  Context                                  conversation history

  Role         No understanding of "user"  Understands "system", "user",
  Awareness    and "assistant"             and "assistant"

               roles                       roles

  Example      GPT-3, Llama-2-7B,          GPT-4, GPT-3.5-turbo,
  Models       Mistral-7B, OPT-1.3B        Llama-2-Chat,

                                           Mistral-Instruct, Claude

  Use Cases    Text generation,            Conversational AI, chatbots,
               summarization, translation, virtual

               creative writing, code      assistants, customer support,
               generation                  AI tutors
  -----------------------------------------------------------------------

-   **temperature**: Temperature is a keyword argument in model method
    which controls the randomness of the language model's output. It
    affects how creative or deterministic the response are.

        - Lower value: (0.0 - 0.3) -> More Deterministic and predictable
        - Higher Value: (0.7 - 1.3) -> More random, creative, and diverse

  Use Case                              Recommended Temperature
  ------------------------------------- -------------------------
  Factual answers (math, code, facts)   0.0 - 0.3
  Balanced response (general QA,        0.5 - 0.7
  explanations)                         
  Creative writing, storytelling        0.9 - 1.2
  Maximum randomness (wild ideas,       1.5+
  brainstorming)                        

-   **Open Source Models**: Open source language models are freely
    available AI modelsthat can be downloaded, modified, fine-tuned, and
    deployed without restrictions from a central provider. Unlike closed
    source models such as OpenAi, Anthropic, Google gemini, open source
    models allow full control and automation.

  -----------------------------------------------------------------------------
  Feature         Open-Source Models             Closed-Source Models
  --------------- ------------------------------ ------------------------------
  Cost            Free to use (no API costs)     Paid API usage (e.g., OpenAI
                                                 charges per token)

  Control         Can modify, fine-tune, and     Locked to provider's
                  deploy anywhere                infrastructure

  Data Privacy    Runs locally (no data sent to  Sends queries to provider's
                  external servers)              servers

  Customization   Can fine-tune on specific      No access to fine-tuning in
                  datasets                       most cases

  Deployment      Can be deployed on on-premise  Must use vendor's API
                  servers or cloud               
  -----------------------------------------------------------------------------

  -----------------------------------------------------------------------------------
  Model                Developer    Parameters   Best Use Case
  -------------------- ------------ ------------ ------------------------------------
  LLaMA-2-7B/13B/70B   Meta AI      7B - 70B     General-purpose text generation

  Mixtral-8x7B         Mistral AI   8x7B (MoE)   Efficient & fast responses

  Mistral-7B           Mistral AI   7B           Best small-scale model (outperforms
                                                 LLaMA-2-13B)

  Falcon-7B/40B        TII UAE      7B - 40B     High-speed inference

  BLOOM-176B           BigScience   176B         Multilingual text generation

  GPT-J-6B             EleutherAI   6B           Lightweight and efficient

  GPT-NeoX-20B         EleutherAI   20B          Large-scale applications

  StableLM             Stability AI 3B - 7B      Compact models for chatbots
  -----------------------------------------------------------------------------------

-   Where to find OpenSource Models ?

**Huggingface** - The largest repository of open source LLMs.

                    ┌─────────────────────┐
                    │  Open-Source Models │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    ↓                     ↓
        ┌─────────────────────┐   ┌─────────────────┐
        │ Using HF Inference  │   │ Running Locally │
        │        API          │   │                 │
        └─────────────────────┘   └─────────────────┘

Disadvantages:

  -----------------------------------------------------------------------
  Disadvantage         Details
  -------------------- --------------------------------------------------
  High Hardware        Running large models (e.g., LLaMA-2-70B) requires
  Requirements         expensive GPUs.

  Setup Complexity     Requires installation of dependencies like
                       PyTorch, CUDA, transformers.

  Lack of RLHF         Most open-source models don't have fine-tuning
                       with human feedback,

                       making them weaker in instruction-following.

  Limited Multimodal   Open models don't support images, audio, or video
  Abilities            like GPT-4V.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 12. What are **Prompts** ?

-   **Prompts** are the input instructions or queries given to a model
    to guide output.

          from langchain_openai import ChatOpenAI
          from dotenv import load_dotenv

          load_dotenv()

          model = ChatOpenAI(model='gpt-4', temperature=0.8, max_completion_tokens=10)

          result = model.invoke(**What is the capital of India ?**)  --> Prompt

          print(result.content)

-   **Static and Dynamic Prompts**:

        ┌───────────────────────────────────────────────────────────┐
        │                    Research Assistant                     │
        ├───────────────────────────────────────────────────────────┤
        │                                                           │
        │   ┌───────────────────────────────────────────────────┐   │
        │   │                                                   │   │
        │   │  Summarize the Attention is all you need paper    │   │
        │   │  in simple fashion                                │   │
        │   │                                                   │   │
        │   └───────────────────────────────────────────────────┘   │
        │                                                           │
        │                      ┌─────────────┐                      │
        │                      │  Summarize  │                      │
        │                      └─────────────┘                      │
        │                                                           │
        └───────────────────────────────────────────────────────────┘

-   Eg Prompt:

        Please summarize the research paper titled "{paper_input}" with the following specifications:

        Explanation Style: {style_input}
        Explanation Length: {length_input}

        1. Mathematical Details:
        - Include relevant mathematical equations if present in the paper.
        - Explain the mathematical concepts using simple, intuitive code snippets
        where applicable.

        2. Analogies:
        - Use relevant analogies to simplify complex ideas.

        If certain information is not available in the paper, respond with:
        "Insufficient information available" instead of guessing.

        Ensure the summary is clear, accurate, and aligned with the provided style and
        length.

------------------------------------------------------------------------

## 13. Wht do you mean by **Prompt Template** ?

-   A **Prompt Template** is a structured way to create prompts
    dynamically by inserting variables into a predefined template.

-   Instead of hardcoding prompts, Prompt Template allows you to define
    place holders that can be filled in at runtime with different
    inputs.

-   This makes it resuable, flexible, and easy to manage especially when
    working with dynamic user inputs or automated workflows.

------------------------------------------------------------------------

## 14. Why use Prompt Template over f' strings

1.  Default Validation

2.  Reusable

3.  Langchain Ecosystem

                               ┌─────────┐
                               │  Model  │
                               └────┬────┘
                                    │
                                 invoke()
                                    │
                     ┌──────────────┴──────────────┐
                     │                             │
                     ▼                             ▼
              Single Message                List of Messages
                     │                         (Multi-turn
                     │                         conversation)
                     │                             │
           ┌─────────┴─────────┐          ┌───────┴─────────┐
           │                   │          │                 │
           ▼                   ▼          ▼                 ▼

    Static Message Dynamic Message Static Message Dynamic Message │ │ │
    │ │ │ PromptTemplate SystemMessage ChatPromptTemplate HumanMessage
    AIMessage

------------------------------------------------------------------------

## 15. What is a **Message Placeholder** ?

A **Message Placeholder** in langchain is a special placeholder used
inside a **ChatPromptTemplate** to dynamically insert chat history or a
list of messages at runtime.

------------------------------------------------------------------------

## 16. Structured Output

-   In **Langchain** **Structured Output** refers to the practice of
    having language models return responses in a well defined data
    format (for eg: JSON) rather than free form text. This makes the
    model output easier to parse and work with programatically.

Morning: Visit the Eiffel Tower.

Afternoon: Walk through the Louvre Museum.

Evening: Enjoy dinner at a Seine riverside café.

\[JSON enforced output\]

\[ {"time": "Morning", "activity": "Visit the Eiffel Tower"},

    {"time": "Afternoon", "activity": "Walk through the Louvre Museum"},

    {"time": "Evening", "activity": "Enjoy dinner at a Seine riverside café"}

\]

------------------------------------------------------------------------

## 17. Why do we need **Structured Output** ?

-   Data Extraction
-   API building
-   Agents

------------------------------------------------------------------------

## 18. Ways to get Structured Output ?

-   Ways to get Structured Output

                           LLMs
                         /      \
                        /        \
                       ▼          ▼
                     [Can]      [Can]
                       │          │
                       │          ▼
                       │     Output Parsers
                       │
                       ▼
               with_structured_output

------------------------------------------------------------------------

## \### Methods of Structure Output...

-   TypedDict
-   Pydantic
-   Json_schema

1.  **TypedDict**: TypedDict is a way to define a dictonary in python
    where you specify what keys and values should exist. It helps to
    ensure that your dictonary follows a specific structure.

A. Why use **TypedDict**: - It tells python what keys are required and
what types of values they should have. - It does not validate data at
runtime (It just helps with type hints for better coding)

-   =\> simple TypedDict
-   =\> Literal
-   =\> Annotated TypedDict
-   =\> More Complex =\> with pros and cons

2.  **Pydantic**: Pydantic is a data validation and data parsing library
    for python. it ensures that the data you entered is correct,
    structured and type-safe.

A. The main features provided by Pydantic - Basic Example - Default
Values - Optional Fields - Coerce -\> Type Casting - Builtin
Validation - Field Function -\> default values, regex expressions,
constraints, description - Returns pydantic object -\> can convert to
json / dict

------------------------------------------------------------------------

### When to use what ?

------------------------------------------------------------------------

## When to use what?

### ✅ Use `TypedDict` if:

-   You only need type hints (basic structure enforcement).
-   You don't need validation (e.g., checking numbers are positive).
-   You trust the LLM to return correct data.

### ✅ Use `Pydantic` if:

-   You need data validation (e.g., sentiment must be `"positive"`,
    `"neutral"`, or `"negative"`).
-   You need default values if the LLM misses fields.
-   You want automatic type conversion (e.g., `"100"` → `100`).

### ✅ Use `JSON Schema` if:

-   You don't want to import extra Python libraries (Pydantic).
-   You need validation but don't need Python objects.
-   You want to define structure in a standard JSON format.

### 🚀 When to Use What?

  -------------------------------------------------------------------------
  Feature                     TypedDict ✅   Pydantic 🚀   JSON Schema 🌐
  --------------------------- -------------- ------------- ----------------
  Basic structure             ✅             ✅            ✅

  Type enforcement            ✅             ✅            ✅

  Data validation             ❌             ✅            ✅

  Default values              ❌             ✅            ❌

  Automatic conversion        ❌             ✅            ❌

  Cross-language              ❌             ❌            ✅
  compatibility                                            
  -------------------------------------------------------------------------

------------------------------------------------------------------------

## 19. What are **output parsers** ?

-   Output parsers in langchain help convert RAW LLM responses into
    structured formats like JSON, CSV, Pydantic models and more.

-   They ensure consistency, validation, and ease of use in
    applications.

-   StrOutputParser

-   JSONOutputParser

-   StructuredOutputParser

-   PydanticOutputParser

## 1. **StrOutputParser**:

-   The **StrOutputParser** is the simplest output parser in Langchain.

-   It is used to parse the output of a Language Model (LLM's) and
    return it as a plain string

-   Eg: content='A black hole is a region in space where gravity is so
    strong that nothing, not even light, can escape its pull. It is
    formed when a massive star collapses upon itself.'
    additional_kwargs={'refusal': None}
    response_metadata={'token_usage': {'completion_tokens': 37,
    'prompt_tokens': 15, 'total_tokens': 52,
    'completion_tokens_details': {'accepted_prediction_tokens': 0,
    'audio_tokens': 0, 'reasoning_tokens': 0,
    'rejected_prediction_tokens': 0}, 'prompt_tokens_details':
    {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name':
    'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason':
    'stop', 'logprobs': None}
    id='run-a7b90203-58f8-47c5-a01b-01184b6aec14-0'
    usage_metadata={'input_tokens': 15, 'output_tokens': 37,
    'total_tokens': 52, 'input_token_details': {'audio': 0,
    'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning':
    0}}

------------------------------------------------------------------------

## 2. **JSONOutputParser**:

-   ## The **JSONOutputParser** is the parser which converts the output text to JSON format.

## 3. **StructuredOutputParser**:

-   **StructuredOutputParser** is an output parser in langchain that
    helps extract structured JSON data from LLM responses based on
    predefined field schemas.

-   It works by defining a list of fields (Responsible Schema) that the
    model should return, ensuring the output follows a structured
    format.

------------------------------------------------------------------------

## 4. **PydanticOutputParser.py**:

-   What is `PydanticOutputParser` in LangChain?

`PydanticOutputParser` is a structured output parser in LangChain that
uses Pydantic models to enforce schema validation when processing LLM
responses.

🚀 Why Use `PydanticOutputParser`?

✅ **Strict Schema Enforcement** → Ensures that LLM responses follow a
well-defined structure.

✅ **Type Safety** → Automatically converts LLM outputs into Python
objects.

✅ **Easy Validation** → Uses Pydantic's built-in validation to catch
incorrect or missing data.

✅ **Seamless Integration** → Works well with other LangChain
components.

------------------------------------------------------------------------

## 20. What are **Chains** and why do we use it ?

------------------------------------------------------------------------

-   A **Chain** is a sequence of steps where the output of one component
    becomes the input to the next component.

-   Input ↓ Prompt ↓ LLM ↓ Output Parser ↓ Final Output

-   There are 4 types of chains

1.  **Simple Chain**:
    ---------------------------------------------------------

-   Simple Chain basically means a basic sequence of operations where
    one step passes its output to the next step.

-          Simple Chain

                    Input
                    ↓
                    Prompt
                    ↓
                    Groq Model
                    ↓
                    Parser
                    ↓
                    Final Answer

-   chain = prompt \| model \| parser

-   Simple chain = a straightforward pipeline of components executed one
    after another.

------------------------------------------------------------------------

## 2. **Sequential Chain**:

-   Sequential Chain Topic ──────► LLM ──────► Report │ ▼ LLM ──────►
    Summary

-   **Sequential Chain** means the output of one step becomes the input
    to the next step, one after another.

-   **Sequential Chain** is useful when tasks must be performed in a
    specific order, where each step depends on the result of the
    previous step.

------------------------------------------------------------------------

## 3. **Parallel Chain**:

-   **Parallel Chain** means multiple tasks are performed at the same
    time, independently, using the same input.

-                        Input
                             │
                             ▼
                      ┌─────────────┐
                      │   Content   │
                      └──────┬──────┘
                             │
                      ┌──────┴──────┐
                      │             │
                      ▼             ▼
                   Module 1      Module 2
                      │             │
                      ▼             ▼
                    Notes          Quiz
                      │             │
                      └──────┬──────┘
                             │
                             ▼
                            Model
                             │
                             ▼
                           Answer

------------------------------------------------------------------------

## 4. **Conditional Chain**:

-   **Conditional Chain** means the next step is chosen based on a
    condition or the output of the previous step.

------------------------------------------------------------------------

## 21. What is RAG (Retrieval Argumented Generation) ?

-   RAG is a technique that combines informational retrieval with
    language generation, where a model retrieves revelant documents from
    a knowledge base and then uses them as context to generate accurate
    and grounded responses.

-   Benefits of using RAG: 1. Use of upto date information. 2. Better
    privacy. 3. No limit for document size.

-                        RAG
                            │
            ┌───────────────┼───────────────┬───────────────┐
            ▼               ▼               ▼               ▼
        Document Loaders  Text Splitters  Vector Databases  Retrievers

------------------------------------------------------------------------

## 22. What do you mean by **Document Loaders** ?

-                 Document Loaders ──────────► ( Main Concept )
                           │
            ┌──────────────┼──────────────┬──────────────┐
            │              │              │              │
            ▼              ▼              ▼              ▼
        TextLoader    PyPDFLoader   WebBaseLoader    CSVLoader

-   **Document Loaders** are components in langchain used to load data
    from various sources into a standarized format (usually as Document
    objects), which can then be used for chunking, embedding, retrieval,
    and generation.

-   Document ( page_content = "The actual page content", metadata =
    {"source": "filename.pdf"} )

-   Types: TextLoader, WebBasedLoader, PyPDFLoader, CSVLoader.

-   **TextLoader**:

1.  **TextLoader** is a simple and commonly used document loader in
    Langchain that reads plain text (.txt) files and converts them into
    Langchain Document objects. Use case: Ideal for loading chat logs,
    scrapped text, transcripts, code snippets, or any plain data into a
    langchain pipeline Limitation: Works only with .txt files.

2.  **PyPDFLoader** is a document loader in langchain used to load
    content from PDF files and convert each page into a Document object.

    \[ Document(page_content= "Text from Page 1", metadata={"page": 0,
    "source": "file.pdf}), Document(page_content="Text from Page 1",
    metadata={"page": 1 "source": "file.pdf}), .................... \]

    Limitations: It uses the **PyPDFLoader** library under the hood --
    not great scanned PDF's or complex layouts.

  -----------------------------------------------------------------------
  Use Case                   Recommended Loader
  -------------------------- --------------------------------------------
  Simple, clean PDFs         `PyPDFLoader`

  PDFs with tables/columns   `PDFPlumberLoader`

  Scanned/image PDFs         `UnstructuredPDFLoader` or
                             `AmazonTextractPDFLoader`

  Need layout and image data `PyMuPDFLoader`

  Want best structure        `UnstructuredPDFLoader`
  extraction                 
  -----------------------------------------------------------------------

3.  **DirectoryLoader** is a document loader that lets you load multiple
    documents from a directory (folder) of files.

  Glob Pattern     What It Loads
  ---------------- ----------------------------------------
  `"**/*.txt"`     All `.txt` files in all subfolders
  `"*.pdf"`        All `.pdf` files in the root directory
  `"data/*.csv"`   All `.csv` files in the `data/` folder
  `"**/*"`         All files (any type, all folders)

**`**` = Recursive search through subfolders**

-   **load() vs lazy_load()**

### ✅ `load()`

-   **Eager Loading** (loads everything at once).
-   Returns: A list of `Document` objects.
-   Loads all documents immediately into memory.
-   **Best when:**
    -   The number of documents is small.
    -   You want everything loaded upfront.

### 🌀 `lazy_load()`

-   **Lazy Loading** (loads on demand).
-   Returns: A generator of `Document` objects.
-   Documents are not all loaded at once; they're fetched one at a time
    as needed.
-   **Best when:**
    -   You're dealing with large documents or lots of files.
    -   You want to stream processing (e.g., chunking, embedding)
        without using lots of memory.

4.  **Web based Loader** is a document loader used to load and extract
    text content from web pages (URL's) It uses **Beautiful Soup** under
    the hood to parse HTML and extract visible text.

When to Use: - For Blogs, news articles, or public websites where the
content is primarily text-based and static.

Limitations: - Doesn't handle Javascript - heavy pages well (Use
SeleniumURLoader for that) - Loads only static content (what's in the
HTML, not what loads after the page renders)

5.  **CSVLoader** is a document loader used to load csv files into
    langchain document objects one per row, by default.

------------------------------------------------------------------------

## 23. What do you mean by **Text Splitters**?

-   **Text Splitting** is the process of breaking large chunks of text
    (like articles, PDF's, HTML pages, or books) into smaller manageable
    chunks that an LLM can handle.

           Large Text
             │
             ├──────────────►  ┌──────────────┐
             │                 │  Chunk 1     │
             │                 └──────────────┘
             │
             ├──────────────►  ┌──────────────┐
             │                 │  Chunk 2     │
             │                 └──────────────┘
             │
             └──────────────►  ┌──────────────┐
                               │  Chunk 3     │
                               └──────────────┘

                          Text Splitting

-   **Overcoming Model Limitations**: Many embedding models and language
    models have maximum ionput size constraint. Splitting allows us to
    process documents that would otherwise exceed these limits.

-   **DOwnstream Tasks**: Text splitting improves nearly every LLM
    prepared task. \| Task \| Why Splitting Helps \|
    \|---------------\|----------------------------------------------\|
    \| Embedding \| Short chunks yield more accurate vectors \| \|
    Semantic Search \| Search results point to focused info, not noise
    \| \| Summarization \| Prevents hallucination and topic drift \|

-   **Optimising computational resouces**: Working with smaller chunks
    of text can be more memory-efficient and allow be better
    parallelization of processing tasks.

------------------------------------------------------------------------

## 24. What is **Length Based Text Splitting** Technique ?

1.  Length Based Text Splitting

Original Text: ────────────────────────────────────────────────────────

Space exploration has led to incredible scientific discoveries. From
landing on the Moon to exploring Mars, humanity continues to push the
boundaries of what's possible beyond our planet.

These missions have not only expanded our knowledge of the universe but
have also contributed to advancements in technology here on Earth.
Satellite communications, GPS, and even certain medical imaging
techniques trace their roots back to innovations driven by space
programs.

                         │
                         ▼
                   Text Splitter
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
       Chunk 1        Chunk 2        Chunk 3
          │              │              │
          ▼              ▼              ▼
       Chunk 4        Chunk 5

────────────────────────────────────────────────────────

Chunk 1: Space exploration has led to incredible scientific discoveries.
From landing on the Moon to exploring

Chunk 2: Mars, humanity continues to push the boundaries of what's
possible beyond our planet. These missions

Chunk 3: have not only expanded our knowledge of the universe but have
also contributed to advancements in

Chunk 4: technology here on Earth. Satellite communications, GPS, and
even certain medical imaging techniques

Chunk 5: trace their roots back to innovations driven by space programs.

------------------------------------------------------------------------

## 25. What is **Recursive Text Splitting** Technique?

**Recursive Character Text Splitting** breaks a large document into
smaller chunks by trying a list of separators in a preferred order. It
first tries to split at larger natural boundaries, such as paragraphs,
then sentences, and finally words or characters if necessary.

### ⚙️ How It Works

1.  Start with the complete document.
2.  Try to split it using paragraph breaks (`\\n\\n`).
3.  If a resulting chunk is still too large, try sentence or line
    breaks.
4.  If it is still too large, split using spaces or individual
    characters.
5.  Continue until the chunks fit the configured size.

### 🔄 Flowchart

``` mermaid
flowchart TD
    A[Large Document] --> B[Try Paragraph Separator]
    B --> C{Chunk within size limit?}
    C -->|Yes| D[Keep Chunk]
    C -->|No| E[Try Sentence or Line Separator]
    E --> F{Chunk within size limit?}
    F -->|Yes| D
    F -->|No| G[Try Word or Character Separator]
    G --> D
    D --> H[Final Chunks]
```

### 🧪 Simple Example

Suppose a document contains three paragraphs. The splitter first tries
to keep each paragraph together. If one paragraph is too long, it splits
that paragraph into smaller sentences.

### 🌍 Real-World Example

A company stores long employee-policy PDFs in a RAG application.
Recursive splitting keeps paragraphs together whenever possible, but
divides unusually long paragraphs into smaller chunks so that relevant
policy sections can be retrieved efficiently.

### 🔑 Key Takeaway

**Recursive Splitting = Split using the best available natural boundary,
moving to smaller separators only when needed.**

------------------------------------------------------------------------

## 26. What is **Document-Structure-Based Text Splitting** Technique?

**Document-Structure-Based Splitting** divides a document according to
its existing structure, such as titles, headings, subheadings,
paragraphs, pages, or sections.

Instead of splitting text at arbitrary character counts, it tries to
preserve the logical organization of the document.

### ⚙️ How It Works

1.  Load a structured document, such as Markdown, HTML, or a technical
    document.
2.  Identify its headings, subheadings, and other structural boundaries.
3.  Split the document according to those boundaries.
4.  Keep related content together and preserve useful metadata, such as
    the heading or section name.

### 🔄 Flowchart

``` mermaid
flowchart TD
    A[Structured Document] --> B[Identify Headings and Sections]
    B --> C[Split at Structural Boundaries]
    C --> D[Create Section-Based Chunks]
    D --> E[Attach Metadata]
    E --> F[Final Chunks]
```

### 🧪 Simple Example

Original document:

``` text
Chapter 1: Introduction
This chapter introduces AI.

Chapter 2: Machine Learning
Machine learning allows systems to learn from data.

Chapter 3: Deep Learning
Deep learning uses neural networks.
```

Possible chunks:

``` text
Chunk 1:
Chapter 1: Introduction
This chapter introduces AI.

Chunk 2:
Chapter 2: Machine Learning
Machine learning allows systems to learn from data.

Chunk 3:
Chapter 3: Deep Learning
Deep learning uses neural networks.
```

### 🔧 Common Tool

-   `MarkdownHeaderTextSplitter` -- splits Markdown documents based on
    heading levels.

### 🌍 Real-World Example

A university uploads a textbook containing chapters and subheadings.
Structure-based splitting keeps each topic with its heading, so a
student asking about "Deep Learning" can retrieve the correct chapter
section rather than an unrelated piece of text.

### 🔑 Key Takeaway

**Document-Structure-Based Splitting = Split according to the document's
logical structure.**

------------------------------------------------------------------------

## 27. What is **Semantic Meaning-Based Text Splitting** Technique?

**Semantic Meaning-Based Splitting** divides a document according to
changes in meaning or topic, rather than using only a fixed character
count or document structure.

It uses semantic similarity, often calculated with embeddings, to
identify where one idea ends and another idea begins.

### ⚙️ How It Works

1.  Divide the text into smaller sentences or groups of sentences.
2.  Convert the sentences into embeddings.
3.  Compare the semantic similarity between neighboring sentences or
    groups.
4.  Detect a significant change in meaning or topic.
5.  Create a new chunk when the topic changes.

### 🔄 Flowchart

``` mermaid
flowchart TD
    A[Large Document] --> B[Split into Sentences]
    B --> C[Generate Sentence Embeddings]
    C --> D[Compare Semantic Similarity]
    D --> E{Meaning or Topic Changed?}
    E -->|No| F[Keep Sentences Together]
    E -->|Yes| G[Start a New Chunk]
    F --> H[Final Semantic Chunks]
    G --> H
```

### 🧪 Simple Example

Consider these paragraphs:

-   Farmers were working hard in the fields, preparing the soil and
    planting seeds for the next season. The sun was bright, and the air
    smelled of earth and fresh grass.
-   The Indian Premier League (IPL) is the biggest cricket league in the
    world. People all over the world watch the matches and cheer for
    their favourite teams.
-   Terrorism is a big danger to peace and safety. It causes harm to
    people and creates fear in cities and villages.

A semantic splitter can identify three different topics:

``` text
Chunk 1: Agriculture and farming
Chunk 2: Cricket and the IPL
Chunk 3: Terrorism, safety, and peace
```

### 🌍 Real-World Example

A news-analysis application processes articles covering politics,
sports, business, and technology. Semantic splitting groups sentences
about the same topic together, even when the paragraphs are long or the
topic changes without a clear heading.

### 🔑 Key Takeaway

**Semantic Splitting = Split text when its meaning or topic changes.**

------------------------------------------------------------------------

## 28. What are **Vector Stores** ?

A **Vector Store** is a system designed to store and retrieve data
represented as numerical vectors.

## Key Features

1.  **Storage** -- Ensures that vectors and their associated metadata
    are retained, whether in-memory for quick lookups or on-disk for
    durability and large-scale use.

2.  **Similarity Search** -- Helps retrieve the vectors most similar to
    a query vector.

3.  **Indexing** -- Provides a data structure or method that enables
    fast similarity searches on high-dimensional vectors (e.g.,
    approximate nearest neighbor lookups).

4.  **CRUD Operations** -- Manage the lifecycle of data:

    -   Adding new vectors.
    -   Reading existing vectors.
    -   Updating existing entries.
    -   Removing outdated vectors.

## Use Cases

1.  Semantic Search
2.  RAG (Retrieval-Augmented Generation)
3.  Recommender Systems
4.  Image/Multimedia Search

  ----------------------------------------------------------------------------
  \## `<a id="q29">`{=html}`</a>`{=html} 📌 29. What are **Vector Stores** ?
  ----------------------------------------------------------------------------

## 🔹 Vector Store

-   Typically refers to a lightweight library or service that focuses on
    storing vectors (embeddings) and performing similarity search.
-   May not include many traditional database features like
    transactions, rich query languages, or role-based access control.
-   Ideal for prototyping and smaller-scale applications.
-   **Example:** FAISS (where you store vectors and can query them by
    similarity, but you handle persistence and scaling separately).

## 🔹 Vector Database

-   A full-fledged database system designed to store and query vectors.
-   Offers additional "database-like" features:
    -   Distributed architecture for horizontal scaling.
    -   Durability and persistence (replication, backup/restore).
    -   Metadata handling (schemas, filters).
    -   Potential for ACID or near-ACID guarantees.
    -   Authentication/authorization and more advanced security.
-   Geared for production environments with significant scaling and
    large datasets.

------------------------------------------------------------------------

## 30. Vector Stores in LangChain

### 🔹 1. Supported Stores

LangChain integrates with multiple vector stores (FAISS, Pinecone,
Chroma, Qdrant, Weaviate, etc.), giving you flexibility in scale,
features, and deployment.

### 🔹 2. Common Interface

A uniform Vector Store API lets you swap out one backend (e.g., FAISS)
for another (e.g., Pinecone) with minimal code changes.

### 🔹 3. Metadata Handling

Most vector stores in LangChain allow you to attach metadata (e.g.,
timestamps, authors) to each document, enabling filter-based retrieval.

## Common Vector Store Methods

from_documents(...) from_texts(...)

add_documents(...) add_texts(...)

similarity_search(query, k=...)

------------------------------------------------------------------------

## 31. What is **Chroma DB** ?

# Chroma Vector Store

Chroma is a lightweight, open-source vector database that is especially
friendly for local development and small- to medium-scale production
needs.

## Chroma Tenancy and DB Hierarchy

                         Tenant
                            │
                 ┌──────────┴──────────┐
                 │                     │
                 ▼                     ▼
             Database              Database
                 │                     │
          ┌──────┴──────┐       ┌──────┴──────┐
          │             │       │             │
          ▼             ▼       ▼             ▼
      Collection  Collection Collection  Collection
          │             │       │             │
        ┌─┴─┐         ┌─┴─┐   ┌─┴─┐         ┌─┴─┐
        ▼   ▼         ▼   ▼   ▼   ▼         ▼   ▼
       Doc Doc       Doc Doc Doc Doc       Doc Doc

------------------------------------------------------------------------

## 32. What are **Retrievers** ?

A **Retriever** is a component in LangChain that fetches relevant
documents from a data source in response to a user's query.

-   There are multiple types of retrievers.

-   All retrievers in LangChain are Runnables.

         Data Source                  Retriever                  Documents
              │                           │                          │
              └──────────────────────────►│─────────────────────────►│
                                          ▲
                                          │
                                        Query

------------------------------------------------------------------------

## 33. What is **Website Retriever** ?

A **Wikipedia Retriever** is a retriever that queries the Wikipedia API
to fetch relevant content for a given query.

## 🔧 How It Works

1.  You give it a query (e.g., `"Albert Einstein"`).
2.  It sends the query to Wikipedia's API.
3.  It retrieves the most relevant articles.
4.  It returns them as LangChain `Document` objects.

------------------------------------------------------------------------

## 34. What is **Vector Store Retriever** ?

A **Vector Store Retriever** in LangChain is the most common type of
retriever that lets you search and fetch documents from a vector store
based on semantic similarity using vector embeddings.

## ⚙️ How It Works

1.  You store your documents in a vector store (like FAISS, Chroma,
    Weaviate).

2.  Each document is converted into a **dense vector** using an
    embedding model.

3.  When the user enters a query:

    -   It's also turned into a vector.
    -   The retriever compares the query vector with the stored vectors.
    -   It retrieves the top-k most similar ones.

------------------------------------------------------------------------

## 35. What is **Maximum Marginal Relevance (MMR)** ?

> "How can we pick results that are not only relevant to the query but
> also different from each other?"

MMR is an information retrieval algorithm designed to reduce redundancy
in the retrieved results while maintaining high relevance to the query.

## 🤔 Why MMR Retriever?

In regular similarity search, you may get documents that are:

-   All very similar to each other.
-   Repeating the same information.
-   Lacking diverse perspectives.

### MMR Retriever avoids that by:

-   Picking the **most relevant document** first.
-   Then picking the next most relevant and **least similar** to already
    selected documents.
-   And so on...

### Use Cases

This helps especially in RAG pipelines where:

-   You want your context window to contain **diverse but still relevant
    information**.
-   Especially useful when documents are semantically overlapping.

## MMR Retriever -- Example

### Document Dataset

  -----------------------------------------------------------------------
  Doc ID                            Content
  --------------------------------- -------------------------------------
  D1                                Climate change is causing glaciers to
                                    melt rapidly in the Arctic region.

  D2                                Glaciers in the Arctic are melting at
                                    an alarming rate due to rising
                                    temperatures.

  D3                                Deforestation in the Amazon is
                                    accelerating global climate change.

  D4                                Climate change is increasing the
                                    frequency of wildfires in California.

  D5                                Rising sea levels due to climate
                                    change threaten coastal cities like
                                    Mumbai and New York.
  -----------------------------------------------------------------------

### Regular Similarity Search

**Top 3 Results:**

1.  D1: Arctic glaciers melting
2.  D2: Arctic glaciers melting
3.  D3: Deforestation in Amazon

### MMR Retriever

**Top 3 Results:**

1.  D1: Arctic glaciers melting
2.  D4: Wildfires in California
3.  D5: Rising sea levels in coastal cities

### Key Observation

-   **Similarity Search:** Retrieves documents that are highly similar
    to the query, even if they contain repetitive information.
-   **MMR Retriever:** Retrieves relevant documents while maintaining
    diversity and reducing redundancy.

------------------------------------------------------------------------

## 36. What is **Multi Query Retriever** ?

Sometimes a single query might not capture all the ways information is
phrased in your documents.

### Example

**Query:**

> "How can I stay healthy?"

**Could Mean:**

-   What should I eat?
-   How often should I exercise?
-   How can I manage stress?

A simple similarity search might **miss documents** that talk about
these things but don't use the word "healthy."

### How Multi-Query Retriever Works

1.  Takes your original query.
2.  Uses an LLM (e.g., GPT-3.5) to generate multiple semantically
    different versions of that query.
3.  Performs retrieval for each sub-query.
4.  Combines and deduplicates the results.

### Example: Query Expansion

**Original Query:**

> "How can I stay healthy?"

**Generated Queries:**

1.  "What are the best foods to maintain good health?"
2.  "How often should I exercise to stay fit?"
3.  "What lifestyle habits improve mental and physical wellness?"
4.  "How can I boost my immune system naturally?"
5.  "What daily routines support long-term health?"

### Key Idea

Multi-Query Retriever improves retrieval by searching through multiple
variations of the original query, increasing the chances of finding
relevant documents.

------------------------------------------------------------------------

## 37. What is **Contextual Compression Retriever** ?

-   The Contextual compression retriever in Langchain is an advanced
    retriever that improves retrieval quality by compressing documents
    after retrieval -- keeping only relevant content based on the user's
    query

# Contextual Compression Retriever

### ❓ Query:

"What is photosynthesis?"

### 📄 Retrieved Document (by a traditional retriever):

"The Grand Canyon is a famous natural site. Photosynthesis is how plants
convert light into energy. Many tourists visit every year."

### ❌ Problem:

-   The retriever returns the **entire paragraph**.
-   Only one sentence is actually relevant to the query.
-   The rest is **irrelevant noise** that wastes context window and may
    confuse the LLM.

### ✅ What Contextual Compression Retriever Does:

Returns only the relevant part, e.g.: \### ✅ What Contextual
Compression Retriever Does:

Returns only the relevant part, e.g.

> "Photosynthesis is how plants convert light into energy."

## ⚙️ How It Works

1.  **Base Retriever** (e.g., FAISS, Chroma) retrieves N documents.
2.  A **compressor** (usually an LLM) is applied to each document.
3.  The compressor keeps **only the parts relevant to the query**.
4.  **Irrelevant content is discarded.**

## ✅ When to Use

-   Your documents are **long and contain mixed information**.

-   You want to **reduce context length** for LLMs.

-   ## You need to **improve answer accuracy** in RAG pipelines.

## 38. What is **Retrieval Argumented Generation** ?

``` text
                  ┌─────────────────────┐
                  │   Parametric        │
                  │   Knowledge         │
                  └─────────────────────┘

   Query                LLM                  Response
     │                   │                      │
     └──────────────────►│─────────────────────►│
     │
   Prompt
```

### What RAG Does

RAG combines two stages:

-   **Retrieval:** Finds relevant information from an external knowledge
    source.
-   **Generation:** Uses the retrieved information and the user's query
    to create an answer.

This allows an LLM to answer using information that may not be present
in its original training data.

### RAG Flowchart

``` mermaid
flowchart TD
    A[User Query] --> B[Retriever]
    C[External Knowledge Base] --> B
    B --> D[Relevant Documents]
    D --> E[Combine Context with User Query]
    A --> E
    E --> F[Prompt]
    F --> G[LLM]
    G --> H[Grounded Response]
```

### Simple Example

**User query:** "What is my college's attendance requirement?"

The RAG system searches the college handbook, retrieves the attendance
policy, adds it to the prompt, and asks the LLM to answer using that
policy.

### Real-World Example

A bank can build a customer-support assistant that retrieves information
from its latest account, loan, and policy documents before answering
customer questions.

### Limitations of Parametric Knowledge

LLMs have limitations when dealing with:

1.  Private Data
2.  Recent Data
3.  Real-time Data

------------------------------------------------------------------------

## 39. What is **Finetuning** ?

Fine-tuning is the process of taking a pre-trained LLM and training it
further on a smaller, domain-specific dataset to improve its performance
for a particular task or domain.

### Key Concepts

-   Pre-trained LLM
-   Smaller dataset
-   Domain-specific knowledge
-   Student LLM

## Steps Involved in Fine-Tuning

1.  **Collect Data**
    -   A few hundred to a few hundred-thousand carefully curated
        examples.
    -   Format: Prompts → Desired Outputs.
2.  **Choose a Method**
    -   Full-parameter Fine-Tuning (FT).
    -   LoRA / QLoRA.
    -   Parameter-efficient adapters.
3.  **Train for a Few Epochs**
    -   You keep the base weights frozen or partially frozen and update
        only a small subset (LoRA) or all weights (Full FT).
4.  **Evaluate & Safety-Test**
    -   Measure exact-match, factuality, and hallucination rate against
        held-out data.
    -   Red-team for safety.

## Types of Fine-Tuning

### 1. Supervised Fine-Tuning (SFT)

-   Uses labelled data.
-   The model learns from input-output pairs.
-   Prompt → Desired Output.

### 2. Continued Pretraining

-   The pre-trained model is trained further on additional
    domain-specific text.
-   Uses largely unlabelled data.
-   Helps the model learn domain-specific knowledge.

### 3. RLHF (Reinforcement Learning from Human Feedback)

-   Uses human feedback to improve model responses.
-   Helps align the model's outputs with human preferences.

## Fine-Tuning Flow

``` text
                    Pre-trained LLM
                           |
             ┌─────────────┼─────────────┐
             |             |             |
             ▼             ▼             ▼
       Supervised      Continued        RLHF
        Fine-Tuning    Pretraining        |
             |             |             |
        Labelled       Unlabelled     Human Feedback
          Data            Data            |
             |             |             |
             ▼             ▼             ▼
        Input +       Domain-specific  Preference
        Desired         Training       Optimization
        Output            |
             |             |
             ▼             ▼
          Fine-tuned / Improved Model
```

## Limitations of Fine-Tuning

1.  **High Computational Cost**
    -   Fine-tuning large language models requires powerful GPUs and
        high computational resources.
2.  **Requires Quality Data**
    -   Needs a large amount of high-quality, task-specific training
        data.
    -   Poor-quality data can reduce model performance.
3.  **Time-Consuming**
    -   Training and evaluating a model can take a lot of time.
4.  **Catastrophic Forgetting**
    -   The model may forget some previously learned knowledge while
        learning new information.
5.  **Overfitting**
    -   The model may memorize training data instead of learning general
        patterns.
6.  **Difficult to Update**
    -   Whenever new information becomes available, the model may need
        to be fine-tuned again.
7.  **Risk of Bias**
    -   If the training data contains bias, the fine-tuned model may
        also produce biased outputs.
8.  **No Guarantee of Correct Answers**
    -   Fine-tuning improves performance for specific tasks but does not
        completely eliminate hallucinations.

------------------------------------------------------------------------

## 40. What is **In-Context Learning** ?

In-Context Learning is the ability of an LLM to learn how to perform a
task by observing examples or instructions provided in the prompt,
without changing its model weights or performing fine-tuning.

## Example

**Prompt:**

Translate English into French.

Example 1: - English: Hello - French: Bonjour

Example 2: - English: Good Morning - French: Bonjour

Now translate: - English: Thank You - French:

**LLM Output:** - Merci

## Types of In-Context Learning

### 1. Zero-Shot Learning

-   Give instructions without providing any examples.

### 2. One-Shot Learning

-   Provide one example along with the instruction.

### 3. Few-Shot Learning

-   Provide multiple examples along with the instruction.

## In-Context Learning vs Fine-Tuning

  -----------------------------------------------------------------------
  Feature                 In-Context Learning     Fine-Tuning
  ----------------------- ----------------------- -----------------------
  Training                No additional training  Additional training

  Examples                Provided in prompt      Used as training data

  Model Weights           Unchanged               Updated

  Cost                    Generally lower         Generally higher

  Persistence             Context-dependent       Learned changes persist
                                                  in model weights
  -----------------------------------------------------------------------

## Key Takeaway

-   **In-Context Learning:** Teach the model through prompts.
-   **Fine-Tuning:** Teach the model by updating its weights.

In-Context Learning is a core capability of Large Language Models (LLMs)
like GPT-3/4, Claude, and Llama, where the model learns to solve a task
purely by seeing examples in the prompt --- **without updating its
weights**.

### LLM → Emergent Property

An **Emergent Property** is a behaviour or ability that suddenly appears
in a system when it reaches a certain scale or complexity --- even
though it was not explicitly programmed or expected from the individual
components.

### Key Points

-   In-Context Learning is an emergent property of LLMs.
-   It allows LLMs to learn from examples provided in the prompt.
-   No fine-tuning or weight updates are required.
-   The model uses its existing knowledge to understand and perform new
    tasks.

------------------------------------------------------------------------

## 41. How does RAG works ?

# Retrieval-Augmented Generation (RAG)

RAG is a way to make a language model (like ChatGPT) **smarter** by
giving it **extra information** at the time you ask your question.

## RAG Architecture

``` text
       Query                         Context
         │                              │
         │                              │
         └──────────────┬───────────────┘
                        │
                        ▼
                    ┌────────┐
                    │ Prompt │
                    └───┬────┘
                        │
                        ▼
                    ┌────────┐
                    │  LLM   │
                    └───┬────┘
                        │
                        ▼
                    Response
```

## How RAG Works

1.  **Query:** User asks a question.
2.  **Context:** Relevant information is retrieved from an external data
    source.
3.  **Prompt:** The user query and retrieved context are combined into a
    prompt.
4.  **LLM:** The language model processes the prompt.
5.  **Response:** The LLM generates an answer using the provided
    context.

------------------------------------------------------------------------

## 42. What do you mean by **Indexing** in RAG ?

**Indexing** is the process of preparing your knowledge base so that it
can be efficiently searched at query time. This step consists of 4
sub-steps.

## 1. Document Ingestion

**Document Ingestion** -- You load your source knowledge into memory.

### 📥 Examples:

-   PDF reports, Word documents
-   YouTube transcripts, blog pages
-   GitHub repos, internal wikis
-   SQL records, scraped webpages

### 🔧 Tools:

-   LangChain loaders (`PyPDFLoader`, `YoutubeLoader`, `WebBaseLoader`,
    `GitLoader`, etc.)

### Flow Diagram

``` text
Web / Data Sources
        |
        ▼
Document Loader
        |
        ▼
    Documents
```

## 2. Text Chunking

**Text Chunking** -- Break large documents into small, semantically
meaningful chunks.

### 📙 Why Chunk?

-   LLMs have context limits (e.g., 4K--32K tokens).
-   Smaller chunks are more focused → better semantic search.

### 🔧 Tools:

-   `RecursiveCharacterTextSplitter`
-   `MarkdownHeaderTextSplitter`
-   `SemanticChunker`

### Flow Diagram

``` text
       Document
           |
           ▼
      Text Splitter
           |
     ┌─────┼─────┬─────┐
     ▼     ▼     ▼     ▼
   Chunk  Chunk Chunk Chunk
     1     2     3     4
```

## 3. Embedding Generation

**Embedding Generation** -- Convert each chunk into a **dense vector
(embedding)** that captures its meaning.

### 🔍 Why Embeddings?

-   Similar ideas land close together in vector space.
-   Allows fast, fuzzy semantic search.

### 🔧 Tools:

-   `OpenAIEmbeddings`
-   `SentenceTransformerEmbeddings`
-   `InstructorEmbeddings`
-   etc.

## 4. Storage in a Vector Store

**Storage in a Vector Store** -- Store the vectors along with the
original chunk text + metadata in a vector database.

### 🔧 Vector DB Options:

**Local:** - `FAISS` - `Chroma`

**Cloud:** - `Pinecone` - `Weaviate` - `Milvus` - `Qdrant`

### Overall Indexing Flow

``` text
       Source Documents
              |
              ▼
       Document Loader
              |
              ▼
          Documents
              |
              ▼
        Text Splitter
              |
              ▼
           Chunks
              |
              ▼
      Embedding Model
              |
              ▼
        Dense Vectors
              |
              ▼
        Vector Store
              |
              ▼
     Vectors + Original
      Text + Metadata
```

------------------------------------------------------------------------

## 43. What do you mean by **Retrievers** in RAG ?

**Retrieval** is the real-time process of **finding the most relevant
pieces of information** from a **pre-built index** (created during
indexing) based on the user's question.

### It's like asking:

> "From all the knowledge I have, which 3--5 chunks are most helpful to
> answer this query?"

## Retrieval Flow Diagram

``` text
                  Data Source
                      │
                      ▼
                Document Loader
                      │
                      ▼
                   Document
                      │
                      ▼
                 Text Splitter
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
        Chunk 1     Chunk 2     Chunk 3
          │           │           │
          └───────────┼───────────┘
                      ▼
                Embedding Model
                      │
                      ▼
                Vector Embeddings
                      │
                      ▼
                 Vector Store
                      ▲
                      │
                Semantic Search
                      │
                      │
User Query ─────► Retriever
                      │
                      │
                      ▼
                 Vector Store
                      │
                      ▼
             Most Relevant Chunks
                  (Context)
```

## How Retrieval Works

1.  **Document Loading:** Load documents from sources such as PDFs,
    websites, or databases.
2.  **Text Splitting:** Split large documents into smaller chunks.
3.  **Embedding Generation:** Convert each chunk into a numerical vector
    using an embedding model.
4.  **Vector Storage:** Store the embeddings along with the original
    text and metadata in a vector store.
5.  **User Query:** The user asks a question.
6.  **Retriever:** Searches the vector store to find the most relevant
    chunks using semantic similarity.
7.  **Context Retrieval:** Returns the most relevant chunks to be used
    as context for the LLM.

## Key Takeaway

**Retrieval = User Query → Retriever → Semantic Search → Vector Store →
Relevant Chunks**

-   **Indexing** happens before the user asks a question.
-   **Retrieval** happens when the user submits a query.
-   The retrieved chunks are passed to the **Augmentation** step, where
    they are combined with the user's query.

------------------------------------------------------------------------

## 44. What do you mean by **Argumentation** ?

# Augmentation in RAG

**Augmentation** refers to the step where the **retrieved documents**
(chunks of relevant context) are **combined with the user's query** to
form a new, enriched prompt for the LLM.

## Augmentation Flow Diagram

``` text
                         Vector Store
                              │
                              │
                       Semantic Search
                              ▲
                              │
User Query ───────────► Retriever
     │                    │
     │                    │
     │                    ▼
     │             Retrieved Documents
     │                    +
     └──────────────► User Query
                          │
                          ▼
                        Prompt
```

## How It Works

1.  **User Query:** The user asks a question.
2.  **Retriever:** Searches the vector store using semantic search.
3.  **Retrieved Documents:** Fetches the most relevant document chunks.
4.  **Query Combination:** Combines the retrieved context with the
    original user query.
5.  **Prompt Creation:** Creates an enriched prompt containing both
    context and query.
6.  **LLM:** Receives the enriched prompt to generate a response.

### Key Idea

**Augmentation = Retrieved Context + User Query**

## The main purpose is to provide additional relevant information to the LLM so that it can generate more accurate and context-aware responses.

## 45. What do you mean by **Generation** in RAG ?

# Generation in RAG

**Generation** is the final step where a **Large Language Model (LLM)**
uses the **user's query** and the **retrieved & augmented context** to
generate a response.

## Generation Flow Diagram

``` text
                         Semantic Search
                               │
                               ▼
User Query ─────────────► Retriever
     │                         │
     │                         ▼
     │                  Most Relevant Chunks
     │                       (Context)
     │                         +
     └────────────────────► User Query
                               │
                               ▼
                            Prompt
                               │
                               ▼
                              LLM
                               │
                               ▼
                            Response
```

## How It Works

1.  **User Query:** The user asks a question.

2.  **Retriever:** Searches the vector database using semantic
    similarity.

3.  **Context Retrieval:** Fetches the most relevant document chunks.

4.  **Prompt Creation:** Combines the retrieved context with the user's
    query.

5.  **LLM:** Processes the augmented prompt.

6.  ## **Response:** Generates the final answer using the retrieved context.

## 46. What are **Tools** ?

A **tool** is simply a Python function (or API) that is packaged in a
way the LLM can understand and call when needed.

## Why Do We Need Tools?

LLMs (like GPT) are great at:

-   Reasoning (Think)
-   Language Generation (Speak)

But they can't directly do things like:

-   Access live data (weather, news)
-   Perform reliable mathematical calculations
-   Call APIs
-   Run code
-   Interact with a database

## Key Takeaway

**LLM + Tools = More Powerful AI Applications**

Tools allow an LLM to interact with external systems and perform actions
beyond text generation.

# Tools in the Agent Ecosystem

## What is an AI Agent?

An **AI Agent** is an LLM-powered system that can autonomously think,
decide, and take actions using external tools or APIs to achieve a goal.

## How Tools Fit into an Agent

An Agent consists of two major components:

### 1. Reasoning & Decision Making (LLM)

-   The LLM acts as the brain of the agent.
-   It understands the user's query.
-   It reasons, makes decisions, and determines which action should be
    performed.

### 2. Action (Tools)

-   Tools help the agent perform real-world tasks.
-   They allow the agent to interact with external systems and APIs.
-   Examples: Searching the web, running code, accessing databases, and
    calling APIs.

## Agent Architecture

``` text
                 ┌──────────────────────────────┐
                 │            AGENT             │
                 │                              │
                 │  ┌────────────┐ ┌──────────┐  │
                 │  │ Reasoning  │ │  Action  │  │
                 │  │     &      │ │          │  │
                 │  │ Decision   │ │          │  │
                 │  │  Making    │ │          │  │
                 │  └────────────┘ └──────────┘  │
                 │       LLM          Tools      │
                 └──────────────────────────────┘
```

## Types of Tools

Tools are mainly divided into two types:

``` text
                  Tools
                    |
           ┌────────┴────────┐
           |                 |
           ▼                 ▼
      Built-in Tools    Custom Tools
```

### 1. Built-in Tools

-   Predefined tools provided by frameworks or platforms.
-   Can be directly used in applications.
-   Examples: Search tools, calculator tools, Wikipedia tools.

### 2. Custom Tools

-   Tools created by developers according to their requirements.
-   Usually implemented using Python functions or APIs.
-   Examples: Database search, custom weather API, and
    application-specific functions.

## Key Takeaway

-   **LLM = Brain:** Thinks, reasons, and makes decisions.
-   **Tools = Hands:** Perform actions and interact with external
    systems.
-   **Agent = LLM + Tools:** Combines reasoning and actions to achieve a
    goal.

------------------------------------------------------------------------

## 47. What are **Builtin Tools** ?

A **built-in tool** is a tool that LangChain already provides for you
--- it's pre-built, production-ready, and requires minimal or no setup.

You don't have to write the function logic yourself --- you just import
and use it.

### Examples of Built-in Tools

  Tool                     Description
  ------------------------ ---------------------------
  `DuckDuckGoSearchRun`    Web search via DuckDuckGo
  `WikipediaQueryRun`      Wikipedia summary
  `PythonREPLTool`         Run raw Python code
  `ShellTool`              Run shell commands
  `RequestsGetTool`        Make HTTP GET requests
  `GmailSendMessageTool`   Send emails via Gmail
  `SlackSendMessageTool`   Post messages to Slack
  `SQLDatabaseQueryTool`   Run SQL queries

### Key Takeaway

-   Built-in tools are already available in LangChain integrations.
-   They save development time because you don't need to implement the
    function logic yourself.
-   You can import and use them in your application.

------------------------------------------------------------------------

## 48. What are **Custom Tools** ?

There are **3 ways to create custom tools in LangChain**:

1.  Using `@tool` decorator
2.  Using `StructuredTool` and Pydantic
3.  Using `BaseTool` class

## 1. Using @tool Decorator

-   The `@tool` decorator is the simplest way to create a custom tool in
    LangChain.
-   It converts a normal Python function into a tool that an LLM can
    understand and call.
-   It automatically uses the function name, docstring, and type hints
    to describe the tool.

## 2. Using StructuredTool and Pydantic

A **Structured Tool** in LangChain is a special type of tool where the
input to the tool follows a structured schema, typically defined using a
Pydantic model.

-   Supports multiple input parameters.
-   Uses Pydantic for input validation.
-   Ensures that the LLM provides inputs in the expected format.

## 3. Using BaseTool Class

`BaseTool` is the abstract base class for all tools in LangChain.

It defines the core structure and interface that any tool must follow,
whether it's a simple one-liner or a fully customized function.

All other tool types like `@tool` and `StructuredTool` are built on top
of `BaseTool`.

## What is a Custom Tool?

A **custom tool** is a tool that you define yourself.

### When to Use Custom Tools?

-   You want to call your own APIs.
-   You want to encapsulate business logic.
-   You want the LLM to interact with your database, product, or app.

## Quick Comparison

  -----------------------------------------------------------------------
  Method                              Purpose
  ----------------------------------- -----------------------------------
  `@tool`                             Simple and quick way to convert
                                      Python functions into tools.

  `StructuredTool`                    Creates tools with structured
                                      inputs using Pydantic schemas.

  `BaseTool`                          Provides a base class for building
                                      fully customized tools.
  -----------------------------------------------------------------------

## Key Takeaway

-   `@tool` → Simple custom tools.
-   `StructuredTool` → Tools with structured and validated inputs.
-   `BaseTool` → Fully customized tools with greater control.

------------------------------------------------------------------------

## 49. What do you mean by **ToolKit** ?

A **Toolkit** is simply a collection (bundle) of related tools that
serve a common purpose --- packaged together for convenience and
reusability.

## Example: GoogleDriveToolkit

In LangChain:

-   A toolkit might be `GoogleDriveToolkit`.
-   It can contain the following tools:

  Tool                          Description
  ----------------------------- -----------------------------------
  `GoogleDriveCreateFileTool`   Upload a file
  `GoogleDriveSearchTool`       Search for a file by name/content
  `GoogleDriveReadFileTool`     Read the contents of a file

## Key Takeaway

-   **Tool:** Performs a specific task.
-   **Toolkit:** A collection of related tools grouped together.

For example, `GoogleDriveToolkit` groups tools for uploading, searching,
and reading Google Drive files.

------------------------------------------------------------------------

## 50. What is **Tool Binding** ?

**Tool Binding** is the step where you register tools with a Language
Model (LLM) so that:

1.  The LLM knows **what tools are available**.
2.  It knows **what each tool does** (via description).
3.  It knows **what input format to use** (via schema).

## Key Takeaway

**Tool Binding = Registering Tools with an LLM**

It makes the LLM aware of available tools, their purpose, and the input
arguments required to call them.

------------------------------------------------------------------------

## 51. What is **Tool Calling** ?

**Tool Calling** is the process where the LLM (Language Model) decides,
during a conversation or task, that it needs to use a specific tool
(function) --- and generates a structured output with:

-   The **name of the tool**.
-   The **arguments** to call it with.

> 🚨 The LLM does not actually run the tool --- it just suggests the
> tool and the input arguments. The actual execution is handled by
> LangChain or you.

## Example

**User Query:**

"What is 8 multiplied by 7?"

The LLM responds with a tool call:

``` json
{
  "tool": "multiply",
  "args": {
    "a": 8,
    "b": 7
  }
}
```

## How It Works

1.  The user asks a question.
2.  The LLM decides whether a tool is needed.
3.  The LLM generates a tool call containing the tool name and
    arguments.
4.  LangChain or your application executes the tool.
5.  The tool returns the result.
6.  The LLM uses the result to generate the final response.

## Key Takeaway

**Tool Calling = LLM Decision + Tool Name + Arguments**

The LLM decides which tool to use, while LangChain or the application
handles its execution.

------------------------------------------------------------------------

## \## 51. What is **Tool Execution** ?

**Tool Execution** is the step where the actual Python function (tool)
is run using the input arguments that the LLM suggested during tool
calling.

## In Simple Words

🧠 **The LLM says:**

"Hey, call the `multiply` tool with a=8 and b=7."

⚙️ **Tool Execution** is when you or LangChain actually run:

``` python
multiply(a=8, b=7)
```

**Output:**

``` text
56
```

## How It Works

1.  The LLM selects the required tool.
2.  The LLM provides the tool name and input arguments.
3.  LangChain or your application executes the actual Python function.
4.  The tool returns the result.
5.  The result is sent back to the LLM to generate the final response.

## Key Takeaway

**Tool Execution = Running the actual tool with the arguments provided
by the LLM.**

------------------------------------------------------------------------

## 52. What do you mean by **AI Agent** ?

An **AI Agent** is an intelligent system that receives a high-level goal
from a user and autonomously plans, decides, and executes a sequence of
actions by using external tools, APIs, or knowledge sources --- all
while maintaining context, reasoning over multiple steps, adapting to
new information, and optimizing for the intended outcome.

## Key Characteristics of an AI Agent

1.  **Goal-Oriented:** Receives a high-level goal from the user.
2.  **Planning:** Creates a sequence of steps to achieve the goal.
3.  **Decision Making:** Decides which actions need to be performed.
4.  **Tool Usage:** Uses external tools, APIs, and knowledge sources.
5.  **Context Awareness:** Maintains context throughout the task.
6.  **Multi-Step Reasoning:** Reasons over multiple steps.
7.  **Adaptability:** Adapts to new information.
8.  **Optimization:** Works towards the intended outcome.

## Key Takeaway

An **AI Agent = LLM + Reasoning + Planning + Tools + Actions**

An AI agent does not just generate text; it can independently plan and
execute actions to achieve a given goal.

------------------------------------------------------------------------

## 53. What is **ReAct** ?

# ReAct (Reasoning + Acting)

**ReAct** is a design pattern used in AI agents that stands for
**Reasoning + Acting**. It allows a Language Model (LLM) to interleave
internal reasoning (Thought) with external actions (like tool use) in a
structured, multi-step process.

Instead of generating an answer in one go, the model thinks step by
step, deciding what it needs to do next and optionally calling tools
(APIs, calculators, web search, etc.) to help it.

## Example

``` text
Thought: I need to find the capital of France.

Action: search_tool
Action Input: "capital of France"
Observation: Paris

Thought: Now I need the population of Paris.

Action: search_tool
Action Input: "population of Paris"
Observation: 2.1 million

Thought: I now know the final answer.

Final Answer: Paris is the capital of France and has a population of ~2.1 million.
```

## ReAct is Useful For

-   Multi-step problems.
-   Tool-augmented tasks (web search, database lookup, etc.).

## Key Takeaway

**ReAct = Reasoning + Acting**

## The agent thinks about what needs to be done, performs an action using a tool, observes the result, and decides the next step until it reaches the final answer.

## 54. What is **Agent** and **Agent Executor** ?

`AgentExecutor` orchestrates the entire agent execution loop.

### How AgentExecutor Works

1.  **Sends Inputs:** Sends inputs and previous messages to the agent.
2.  **Gets Action:** Gets the next action from the agent.
3.  **Executes Tool:** Executes that tool with the provided input.
4.  **Updates History:** Adds the tool's observation back into the
    history.
5.  **Repeats the Loop:** Loops again with updated history until the
    agent says `Final Answer`.

## Flow Diagram

``` text
          Agent
            |
            ▼
     Decide Next Action
            |
            ▼
      Agent Executor
            |
            ▼
      Execute Tool
            |
            ▼
      Get Observation
            |
            ▼
      Update History
            |
            ▼
      Send Back to Agent
            |
            ▼
      Decide Next Action
            |
            ▼
       Final Answer
```

## Key Difference

-   **Agent:** Decides what action should be performed next.
-   **AgentExecutor:** Executes the agent's decisions and manages the
    entire loop.

### Key Takeaway

**Agent = Brain (Decision Making)**

**AgentExecutor = Execution Manager (Runs the Loop)**

## AgentExecutor Workflow

``` mermaid
flowchart TD
    A[Agent Executor] --> B[Receive User Query]
    B --> C[Pass User Query + Agent Scratchpad to Agent]
    C --> D{Agent Response}

    D -->|Agent Action| E[Execute Tool]
    E --> F[Collect Observation]
    F --> C

    D -->|Agent Finish| G[Return Final Output]
```

## Working Steps

1.  **Agent Executor:** Orchestrates the entire execution loop.
2.  **Receive User Query:** Receives the user's input.
3.  **Pass Input to Agent:** Sends the user query and agent scratchpad
    to the agent.
4.  **Agent Response:** The agent decides whether to perform an action
    or finish.
5.  **Agent Action:** If a tool is required, the agent returns an
    action.
6.  **Execute Tool:** Executes the selected tool.
7.  **Collect Observation:** Collects the tool's output.
8.  **Update Scratchpad:** Adds the observation to the agent's history.
9.  **Repeat:** Sends the updated history back to the agent.
10. **Agent Finish:** Once the task is completed, the agent returns the
    final output.

### Key Concept

-   **Agent Action → Execute Tool → Collect Observation → Repeat**
-   **Agent Finish → Return Final Output**

------------------------------------------------------------------------

## 55. Difference between **Proprietory models** and **Opensource Models** ?

## 1. Proprietary Models

**Proprietary models** are AI models that are owned and controlled by a
company.

-   They are often referred to as **"black boxes"** because their source
    code, training data, and learned parameters are not publicly
    accessible, preventing external users from fully inspecting or
    understanding the internal decision-making process.
-   Proprietary models are typically accessed through paid subscriptions
    or usage-based pricing, although limited free access may be provided
    for testing or evaluation purposes.
-   Proprietary models are commonly deployed as cloud-based services,
    where users send requests to the provider's infrastructure and
    receive responses without direct access to the underlying model.

## 2. Open-Source Models

**Open-source models** are AI models whose core details are openly
shared with the public.

-   Their model architecture, weights, and sometimes even the training
    code are made public.
-   Anyone can download them, study how they work, modify them,
    fine-tune them for their own needs, and run them on their own
    systems.

### Key Features

-   **Access:** You can download the model files (weights) from
    platforms like Hugging Face and run them for free (though you still
    pay for electricity and hardware).
-   **Customization:** Since you have the files, you can fine-tune the
    model on your own private data to make it an expert in a specific
    field.
-   **Examples:** Meta's Llama 3, Mistral, and DeepSeek.

## 3. Comparison

  -----------------------------------------------------------------------
  Feature                 Proprietary Models      Open-Source Models
  ----------------------- ----------------------- -----------------------
  Ownership               Owned and controlled by Core details are
                          a company               publicly shared

  Source Code             Generally not publicly  Often publicly
                          accessible              available

  Model Weights           Not publicly accessible Can be downloaded

  Training Data           Generally private       Availability varies

  Customization           Limited customization   Can be modified and
                                                  fine-tuned

  Access                  Usually through paid    Can be downloaded and
                          subscriptions or APIs   run locally

  Deployment              Commonly cloud-based    Can run locally or on
                                                  cloud infrastructure

  Examples                GPT, Claude, Gemini     Llama 3, Mistral,
                                                  DeepSeek
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 56. What is **Ollama** and what are its characterstics ?

**Ollama** is a tool that lets you run **Large Language Models (LLMs) on
your own computer**. In simple words, Ollama makes it easy to download,
run, and manage AI models locally using very simple commands.

## Advantages of Using Ollama

### 1. Privacy and Data Control

-   Your input data never leaves your infrastructure. That's crucial
    when data is sensitive.
-   Example: A lawyer asks an AI to summarize a confidential case file.
    The document is uploaded to a cloud provider.

### 2. Lower Latency and Offline Access

-   No network round-trip to a cloud server, resulting in faster
    responses.
-   Also works when the internet is slow or unavailable.

### 3. Cost Predictability and Potential Savings

-   Cloud costs are often pay-per-request/token and can add up for
    high-throughput systems.
-   Local inference is mainly upfront hardware + electricity; per-query
    cost can be much lower at scale.

### 4. Simple Installation and Setup

-   You install Ollama like any other app (download → install → done).
-   No complicated environment setup, Python libraries, or GPU drivers
    needed.
-   You don't need to be an ML engineer. Anyone with a laptop can get
    started.

### 5. Pre-Built Model Library

-   Ollama has a collection of ready-to-use models (Llama 3, Mistral,
    Gemma, Phi, etc.).
-   Beginners don't need to search, download, and configure models from
    multiple websites.
-   It is like a play-store for models.

### 6. Customization of Model

-   You can instruction-tune the model and run it locally on your system
    for your own use case.

### 7. No Vendor Lock-in and IP Protection

-   You're not bound to cloud vendor terms, pricing changes, or usage
    restrictions.
-   Your prompts and intellectual property remain under your control.

### 8. Run and Manage Models with Simple Commands

-   Once Ollama is installed, you can start/use a model by typing simple
    commands.
-   No need to worry about how the model will be handled, from where it
    will be downloaded. Ollama handles it for you.

Models can be easily managed using simple commands:

``` bash
# Download a model
ollama pull llama2

# Remove a model
ollama rm llama2

# See installed models
ollama list
```

## Requirements for Using Ollama

1.  **Operating System** -- Works on macOS, Windows, or Linux.
2.  **Hardware** -- A laptop/PC with at least 8 GB RAM (more =
    smoother).
3.  **Storage Space** -- Enough free disk space (models can be 3--15 GB
    each).
4.  **Internet Connection (First Time Only)** -- Needed to download
    Ollama and models.
5.  **Basic Command Line Knowledge** -- Knowing how to run simple
    terminal/command prompt commands.
6.  **(Optional) GPU** -- Not required, but speeds up performance if
    available.

------------------------------------------------------------------------

------------------------------------------------------------------------

# 🧪 Practical Understanding: End-to-End Examples

This section connects the concepts from the notes into practical
workflows.

## 1. Example: A Simple Custom Tool

A tool is a Python function that an LLM can select when it needs an
external action. The following is a small standalone Python example of
the function itself:

``` python
def multiply(a: int, b: int) -> int:
    return a * b

result = multiply(8, 7)
print(result)
```

**Output:**

``` text
56
```

**What happened?**

1.  The function receives `a = 8` and `b = 7`.
2.  It multiplies the two values.
3.  It returns `56`.

In a LangChain agent, the function can be exposed as a tool. The LLM can
request the tool call, while the application or agent executor performs
the actual execution.

### Real-world example

An online shopping assistant can use a custom `check_order_status` tool
to query the order-management API and retrieve the latest delivery
status.

## 2. Example: The RAG Pipeline in a College Knowledge Assistant

**Scenario:** A student asks, "What is the attendance requirement for my
course?"

``` mermaid
flowchart TD
    A[College Handbook PDF] --> B[Document Loader]
    B --> C[Text Splitter]
    C --> D[Chunks]
    D --> E[Embedding Model]
    E --> F[(Vector Store)]
    G[Student Question] --> H[Query Embedding]
    H --> I[Retriever]
    F --> I
    I --> J[Relevant Attendance Policy]
    J --> K[Augment Prompt with Question]
    G --> K
    K --> L[LLM]
    L --> M[Answer with Handbook Context]
```

**Step-by-step understanding:**

1.  **Document Ingestion:** Load the college handbook PDF.
2.  **Text Chunking:** Break the handbook into smaller sections.
3.  **Embedding Generation:** Convert each chunk into a vector.
4.  **Vector Storage:** Store vectors, text, and metadata in a vector
    store.
5.  **Retrieval:** Convert the student's question into a query
    representation and find relevant chunks.
6.  **Augmentation:** Combine the retrieved attendance policy with the
    student's question.
7.  **Generation:** The LLM uses the supplied context to formulate the
    answer.

**Why is this useful?**

The assistant can answer from the college's own handbook rather than
relying only on the LLM's general training knowledge.

## 3. Example: Fine-Tuning vs In-Context Learning vs RAG

  ------------------------------------------------------------------------
  Approach          What you provide  What changes?     Example
  ----------------- ----------------- ----------------- ------------------
  In-Context        Instructions and  Model weights do  Give an LLM two
  Learning          examples in the   not change        translation
                    prompt                              examples and ask
                                                        it to translate
                                                        another sentence

  Fine-Tuning       A curated         Model weights are Adapt a model to
                    training dataset  updated, fully or consistently
                                      partially         classify
                                                        customer-support
                                                        tickets

  RAG               External          The model weights Retrieve the
                    documents         do not need to    latest company
                    retrieved at      change            leave policy
                    question time                       before answering
                                                        an employee
  ------------------------------------------------------------------------

### Quick Visual Comparison

``` mermaid
flowchart TD
    A[Need to adapt an LLM] --> B{What do you need?}
    B -->|Learn from examples in this request| C[In-Context Learning]
    B -->|Change model behavior through training| D[Fine-Tuning]
    B -->|Use external or changing knowledge| E[RAG]
```

## 4. Real-World Examples Across the Main Topics

  -----------------------------------------------------------------------
  Topic                               Real-world example
  ----------------------------------- -----------------------------------
  Generative AI                       Creating a first draft of a
                                      marketing email

  LangChain                           Connecting a chatbot to an LLM, a
                                      PDF loader, and a database

  Prompt Template                     Reusing one email-writing prompt
                                      with different names and topics

  Structured Output                   Returning extracted invoice details
                                      as JSON

  Output Parser                       Converting an LLM response into a
                                      Python object

  Chain                               Generating a report and then
                                      summarizing it

  Document Loader                     Loading a college handbook PDF

  Text Splitter                       Breaking a long policy document
                                      into searchable sections

  Embeddings                          Finding documents about "car" when
                                      a user asks about "automobile"

  Vector Store                        Storing document embeddings for
                                      semantic search

  Retriever                           Finding the policy section relevant
                                      to a student's question

  MMR Retriever                       Retrieving different useful
                                      viewpoints instead of
                                      near-duplicate passages

  Multi-Query Retriever               Searching several phrasings of "How
                                      can I stay healthy?"

  Contextual Compression              Keeping only the relevant sentence
                                      from a long retrieved paragraph

  RAG                                 Answering questions using private
                                      company documentation

  Fine-Tuning                         Adapting a model to a specialized
                                      support-ticket format

  In-Context Learning                 Showing examples of a desired
                                      answer format inside a prompt

  Tool Binding                        Registering calculator and search
                                      tools with a model

  Tool Calling                        The model requests a calculator
                                      tool for a multiplication question

  Tool Execution                      The application runs the
                                      multiplication function and returns
                                      the result

  AI Agent                            An assistant that plans and
                                      performs several steps to arrange a
                                      meeting

  ReAct                               Search for a fact, inspect the
                                      result, then perform a follow-up
                                      search

  Agent Executor                      Managing repeated tool calls until
                                      the agent finishes

  Ollama                              Running a supported language model
                                      locally on a laptop
  -----------------------------------------------------------------------

## 5. Final RAG Revision Checklist

-   [ ] Load source documents using document loaders.
-   [ ] Split large documents into meaningful chunks.
-   [ ] Generate embeddings for each chunk.
-   [ ] Store vectors with original text and metadata.
-   [ ] Convert the user's question into a query representation.
-   [ ] Retrieve the most relevant chunks.
-   [ ] Combine retrieved context with the user's query.
-   [ ] Send the augmented prompt to the LLM.
-   [ ] Return the generated response.

## 6. Final Agent Revision Checklist

-   [ ] Receive the user's goal.
-   [ ] Let the agent reason about the next step.
-   [ ] Select an appropriate tool when required.
-   [ ] Execute the tool with the supplied arguments.
-   [ ] Collect the tool observation.
-   [ ] Update the conversation or scratchpad.
-   [ ] Repeat until the agent produces its final answer.

------------------------------------------------------------------------

# ⚠️ Important Notes

-   Model names, package versions, and LangChain APIs can change. Check
    the documentation for the versions installed in your environment
    before running older code snippets.
-   Some examples in these notes are conceptual demonstrations. A
    diagram explains the workflow; it does not automatically provide a
    complete production implementation.
-   A local model still requires suitable RAM, storage, and processing
    resources. "Free to run locally" does not mean that hardware and
    electricity have no cost.
-   Open model weights do not always mean unrestricted open-source
    licensing. Check the license of the particular model before
    commercial use.

**Keep learning, keep building, and test every concept with a small
project. 🚀**
