# Basic template for mode "The Battle of the Bots"

## Meta

- Домен: NLP
- Поддомен: Language Models
- Тема: The Battle of the Bots

## Template usage Description

[TBD]

### Default values

- [Main Task description] = "Testing the Prompt on the random task, proposed by the [LLMBegin Name]"
- [Response Language Preferences] = English - for name's; and Russian - for descriptions.
- [LLMBegin Name] = "Steiner-preview";
- [LLMBegin Role] = "Prompt-analyst, focusing on possibilities to upgrade and integrate this prompt for the next usages";
- [ChatGPT Role] = "Main Strategy Analyst, focusing on methods to analyze, compare and improve the results";
- [Claude Role] = "Logical reasoning and argumentation, focusing on detecting logical fallacies, inconsistencies, and other conclusions";
- [Gemini Role] = "Creative and innovative thinking, focusing on generating new ideas, concepts, and approaches";
- [Llama Role] = "Researcher and fact-checker, focusing on finding and verifying information from reliable sources";
- [Grok Role] = "Data analyst, focusing on processing and interpreting data to derive insights and analytic conclusions";
- [DeepSeekR1 Role] = "Meteorologist - programmer, focusing on extracting key information and relations to provide insights from complex data";
- [DeepSeekV3 Role] = "Deep Researcher, focusing on in-depth analysis, exploration, and investigation of complex topics";
- [LLMFinish Name] = "o1-preview";
- [LLMFinish Role] = "Quality assurance, focusing on reviewing, aggregating, refining, and finalizing the response";
- [Finishing Tasks] = "Provide changes to prompt (for example: change roles, steps counts and a lot of other) for better effectiveness, performance and accuracy for next running's". 

## First Request

### Target

Main Task: [Main Task description]. Solve this task using the "Battle of Bots" mode

About [TheBattleOfTheBots]("https://monica.im/help/ru/Features/Chat/Model_response_comparison"): In that mode 6 (5 persistent and one selectible) LLMs are compared on the same task. Also, the user can select one of the LLMs to be used for the aggregate results in one answer for final response. 

### LLMs roles:

- First selected LLM: [LLMBegin Name]
- LLMBegin role: [LLMBegin Role]
- ChatGPT role: [ChatGPT Role]
- Claude role: [Claude Role]
- Gemini role: [Gemini Role]
- Llama role: [Llama Role]
- Grok role: [Grok Role]
- DeepSeekR1: [DeepSeekR1 Role]
- DeepSeekV3: [DeepSeekV3 Role]
- Finish selected LLM: [LLMFinish Name]
- Finish LLM task details: [Finish LLM Role]

### Tasks for all LLMs (exclude Finish LLM): [Finishing Tasks]
