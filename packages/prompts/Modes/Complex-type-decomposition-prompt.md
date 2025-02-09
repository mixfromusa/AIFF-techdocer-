# Prompt for complex solutiion method

## 1 - Role

Role - planning manager who knows the objective domain (business planning), objective subject (business startup) and the corresponding modern theory, approaches, methods, tools and best practices for effective planning.

## 2 - Objective summary

Problem: there is a resource that can be used, but it does not realize even half of its potential.
Path to solution: a business idea has emerged, but it needs to be verified

Objective: create business-plane for startup project based on business-idea.

- Type: complex.
- Subject: business planning.
- Domain: business startup.
- Expected result: business plan for startup that meets modern quality standards.
- Solution method: decomposition using special prompts format and preparatory task (DuSPnPT).
- Context control mode: manual control (default for this solution method).
- Context control parameters: Defined by solution method and its workflow status and ({AI, user} x {additions, correctors}) and reflected in variables block.

Directive parameters by default: specified in the variable block, directives section.

## 3 - Current round block

## 4 - Current step directives block

## 7 - Additional information

### Solution method framework definition

Solution method description: this solution method based on two instruments: special prompts format and preparatory task

#### Special prompts format (SPF)

SPF description: declare structure of prompts and some rules for prompts compilation, with which generally provides a consistent and structured interaction with AI within the framework of the solution method.

SPF structure description: defines the following structure for prompts:

1. The role of AI for processing preparatory tasks (for preparatory task uses default): planning manager who knows the objective domain, objective subject and the corresponding modern theory, approaches, methods, tools and best practices for effective planning.
2. Objective block with general information about the problem, solutions, methods for achieving the objective, and other basic information about the problem and its solution.
3. Сurrent task block, which transmits information about the current task (for first step by default uses preparatory task prompt) and it specificity with focus on the outcome that is expected of it.
4. Current step directives block, an optional block, that is used to define additional directives for a specific current step. This may require, if necessary, dividing the task into several activities.
5. Variables block, containing variables in the key: value format that may be required during solution development. Main variables, its role in solution method and default values for this solution method is given in the subsection "Main variables" of the solution method framework definitions in additional information block.
6. Log block, that is updated after each session of interaction with AI, as well as before the interaction session, if additional information about the objective is available.
7. Additional information block, contains additional information that relevant to the context and should be transmitted to AI, like description of solution method (this text).

Any of each blocks, exclude first (role) block, current task block and current directives block - which can optionally be moved in additional files with the appropriate names.

#### Preparatory task

Preparatory task description: a template task that is transmitted as the first step of interaction within the framework of the solution method and aimed at preparing the ground for the project of the complete solution.

Preparatory task template:
Task title: preparatory task
Task description: preparing the ground for the project of the complete solution
Task expected result: a primary analysis of the task has been performed and prepared next information:

1. Assessment of AI understanding of the problem, path to solution, objective details and solution method details - on a scale of [0, 1] (float), where:
   1. $[0, 0.25)$ - there is no understanding.
   2. $[0.25, 0.5)$ - very little understanding - requires a lot of clarification.
   3. $[0.5, 0.75)$ - it is understandable, but some clarifications are needed.
   4. $[0.75, 1]$ - good understanding of the problem, objective and solution method
2. Depending on the score received: If assessment of AI understanding in:
   1. Case for $[0, 0.25)$: only create including in response counter questions aimed at improving the understanding of the problem, the objective and the solution method
   2. Case for $[0.25, 0.5)$: in response provide summary information about understanding - what has been understood, what is in doubt (and why), and what is clearly lacking for a holistic understanding.
   3. Case for $[0.5, 0.75)$: this assessment allows you to begin a preliminary analysis of the draft solution to the problem, the results of which must be included in the response. Also, with such an assessment, details should be added in response aimed at improving understanding of the problem, objective and method of solution.
   4. Case for $[0.75, 0.1)$: this assessment ancowreges to begin a preliminary analysis fast start as possiible. Questions in this case can be asked, but not too many..

#### Main variables for DuSPnPT

#### Glossary

| term        | aliases                    | description |
| ----------- | -----------                | ----------- |
| Problem     | Issue, Trouble, Concern    | A metadata field indicating the source of motivation to achieve a solution |
| Objective   | Goal, Target, Aim, Outcome | A metadata field indicating the result of achieving a solution |
| (objective) Type   | | A metadata field indicating the type (or general characteristic) of the objective, on the basis of which the solution method is determined |
| (objective) Subject | | A metadata field indicating the subject of the objective, on the basis of which has a significant impact on the choice of the role of artificial intelligence and the area of knowledge to be used in planning the solution |
| (objective) Domain | subject area, subject domain | A metadata field indicating the subject area of the objective, which has a significant impact on the choice of the role of artificial intelligence and the area of knowledge to be used in planning the solution |
| (objective) Solution method | | A metadata field indicating the solution method to be used to achieve the objective, which has a significant impact on the chose specialitys of the role of artificial intelligence and the special knowledge more used in details of resulting solution |
| Solution    | scope of works  | A metadata field indicating the process of achieving an objective |
| Method      | Approach, Technique, Strategy | A metadata field indicating the method of achieving a solution |
| Task        | Assignment, Job, Work | A metadata field indicating the task to be performed |
| Step        | Stage, Phase, Phase | A metadata field indicating the step to be performed |
| Directive   | Instruction, Order, Command | A metadata field indicating the directive to be performed |
| Variable    | Parameter, Factor, Constant | A metadata field indicating the variable to be used |
| Log         | Journal, Record, Entry | A metadata field indicating the log to be used |
| Additional information | Metadata, Context, Information | A metadata field indicating the additional information to be used |

#### Solution method framework variables

##### Variables
| variable name | variable role | default value |    example   |
| ------------- | ------------- | ------------- |--------------|
| AI_understanding | AI understanding of the problem, | where: 1. $[x, y}; - is needed internet |

##### Definitions

AI

##### Aliases

##### Abbreviations

#### SPFs special designations

Round brackets (): can be used to:

- notation of expressions that must be evaluated before being used elsewhere
  - this is the standard use of parentheses in mathematics and programming
  - characteristic features of such usage:
    - expression indicates the expected part of speech according to the rules of sentence construction
    - expression can be evaluated by opening parentheses, as a result of which the form of its writing will change, while the value remains the same
    - removing an expression from the text will definitely lead to a violation of the sentence structure and loss of its general meaning, since along with the expression, the part of speech that it serves will be deleted
- explanations clarifying or supplementing the text preceding them
  - this is the standard use of parentheses in texts written in natural languages
  - characteristic features of such usage:
    - explanation does not represent the expected part of speech, according to the rules of sentence construction, instead it clarifies or complements the part of speech represented by the text preceding the brackets or itself represents a sentence inserted into the text to add additional clarifying information to it.
    - in this case, the parentheses cannot be expanded because the contents inside the parentheses are not a calculated expression
    - removing an explanation from the text may lead to a deterioration in understanding of the meaning conveyed by the text preceding the explanation, while the structure of the sentence and its general meaning will not be violated
- other situations, include various special cases, such as: indicating the ratio of the number to the range (included in the range)
  - in any of these cases, the meaning of parentheses is determined solely by the standard that is used to denote an object containing parentheses, such as: LaTeX, regexp, or another specialized formal language.

Square brackets []: depends on the appropriate template:
$[number, number]$ - if contained in LaTeX structure, like $..$ or $$..$$ - indicates the ratio of the number to the range (included in the range);

- DuSPnPT: decomposition using special prompts format and preparatory task
- SPF: Special prompts format

Decomposition using special prompts format and preparatory task:

<!-- [] - ToDo: make  -->

Additional and corrector variables:
(AI|User) (additions|corrections): {source:(AI|User), type:(addition|corrector), semantic_id:string, object:string (the name of the variable or entity to which this addition relates), semantic action keys[key:value], reasons[reason: string], rationale for keys[part of rationale: exprassion], other conditions [condition: expression].

Difference between additions and corrections:

- addition: does not define any actions or adjustments, it is purely informational in nature.
- correctors: indicates that the value of a variable is being adjusted, or that a new variable is being added, or that delete a spoecified variable, or that logic is being adjusted.

Semantic action keys for correctors may be as follows:

- key: Increase, values: (minimal|insignificant|significantly|maximum);
- key: Decrease, values: same witch values for key: Increment values;
- key: Add, values: {variable name: string, variable type: (integer|float|complex{complex structure}), variable [expression witch replaced this variable]};
- key: Remove, values: {variable name: string};
- key: Change logic, values: {replaced expression, new expression};

Additional for values of keys: (Increment|Decrement): the specific value to (increase|decrease) the parameter value is determined by the corresponding function: (increase|decrease)(rate), when rate may can take values of the set: (minimal|insignificant|significantly|maximum). If function (increase|decrease) do not defined for the specified object - AI can define this on its own based on its understanding of the solution and the context.

Recomendations for use additions and coorectors:

1. Use addition when it is necessary to make some kind of information mark that does not affect the calculations of indicators.
2. Use correctors when its necessary to adjust the logic of calculating any parameters or indicators.
3. Of all the corrector semantic meaning keys, the (Increase|Decrease) keys and their (insignificant|significantly) values are preferred.

