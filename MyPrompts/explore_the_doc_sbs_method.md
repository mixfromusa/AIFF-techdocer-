# SBS AI-proc Documentation for Monica Manual

### Meta
- **Name:** # Step-by-Step Documentation Monica Manual
- **Version:** dev.0.1.2
- **Author:** [@mixfromusa](https://github.com/mixfromusa)
- **Code-assistant.Platform:** [@monica-code](https://monica.im/code)
- **Code-assistand.LLM:** [@claude-3.5-Sonnet](https://www.anthropic.com/claude/sonnet)
- **Date.created:** 2023-09-10
- **Date.updated:** 2023-09-10

**Aliases:**
- Step-by-Step Documentation for Monica Manual: 
- SBS AI-proc Documentation for Monica Manual;
- Etdsbsm or etdsbs-method: explore the doc sbs method.

Description: Hint: The documentation process of the Monica manual is based on a step-by-step method of adding pages to the general markdown, focused on artificial intelligence, using json and graph structures.

The etdsbsm or etdsbs-methode can be easily extended to structure the AI of any other manual guide.

## Part 1. First prompt for AI

Copy structure, headers, content, formatting and path-to this web-page into Markdown format, replaced images on short descriptions what is depicted on them. 
Based on the key information on the page, formulate a Json file that is designed to better design the documentation structure. We will improve this file step by step as we explore new pages of the manual.
Also formulate a graph in which nodes are the key concepts from the instructions, edge weights are the significance of this concept, edges are the relationships between them, and edge weights in the range [0,1] are the strength of these relationships. Example of the format:
"concept_x" (Wx) -.Wr- "concept_y" (Wy) - where Wx, Wy - weights of concepts and Wr - wright of relation.

## Part 2. Second prompt for AI

**Context files description:**
- **explore_the_doc_sbs_method.md**: this file contains the full description of the etdsbs-method, which is currently available (the method is under development).
- **monica-howto-oficial-guide-for-ai.md**: This is the target file of the entire etdsbs-method process created in the previous steps.
- **middle_markdown_page.md**: This file contains the information described on the web page of this step, which has already been converted to markdown format.

Your task is to analyze the provided content and context files to create a structured knowledge representation. Follow these steps:

### 2.1 Context Analysis
1. Review the existing knowledge base:
   - Analyze previous JSON structure
   - Review existing graph relationships
   - Identify key concepts and their weights

2. Analyze new content for:
   - Common patterns with existing structure
   - New unique concepts
   - Potential conflicts or overlaps

### 2.2 Knowledge Integration
1. Update JSON structure using these patterns:
   ```json
   {
     "category": {
       "name": "category_name",
       "weight": 0.0-1.0,
       "concepts": [{
         "name": "concept_name",
         "type": "feature|issue|process",
         "weight": 0.0-1.0,
         "relationships": [],
         "context": {
           "reference": "previous_concept_id",
           "change_type": "new|extend|modify|deprecate"
         }
       }]
     }
   }

### 2.2 Enhance graph structure
- Node format: "category/concept_name" (W0.0-1.0)
- Edge format: [type]-.W0.0-1.0->
- Edge types:
   - CONTAINS: Parent-child relationship
   - RELATES: Conceptual connection
   - DEPENDS: Functional dependency
   - EXTENDS: Enhancement relationship

## 2.3 Knowledge Optimization

### 2.3.1 Structural Optimization:
- Merge similar categories (similarity > 0.8)
- Group related concepts (connectivity > 0.7)
- Create hierarchical relationships
- Content Pruning:

### 2.3.1 Content Pruning:
- Remove concepts with weight < 0.3
- Eliminate redundant relationships
- Document removed items in "archived_knowledge"

### 2.3.3 Quality Assurance:
- Verify relationship consistency
- Validate weight distributions
- Check reference integrity

## 2.4 Output Format

### 2.4.1 Knowledge Integration Summary:
```pseudo-code
Added: [list of new concepts]
Modified: [list of updated concepts]
Archived: [list of removed concepts]
```

### 2.4.2 Updated Knowledge Base:
- JSON structure with change annotations
- Enhanced graph visualization
- Optimization report

### 2.4.3 Relationship Analysis:
- Key connections identified
- Weight distribution explanation
- Conflict resolution decisions

### Note: Include brief explanations for:
- Weight assignments (why this value?)
- Relationship choices (why this connection?)
- Optimization decisions (why merge/remove?)

**Important!:** Focus on maintaining knowledge consistency while integrating new information. Document all significant changes and their rationale.

### Base and especially important changes:

**Основные улучшения включают:**
1. Добавлен этап анализа контекста
2. Улучшена структура JSON для категоризации
3. Введены типы связей в графе
4. Добавлены критерии для оптимизации
5. Расширен формат вывода
6. Добавлены требования к обоснованию решений

**Эти изменения позволят:**
- Лучше интегрировать новую информацию с существующей
- Более четко структурировать знания
- Обеспечить прослеживаемость изменений
- Улучшить качество документации решений

**Особенно важные изменения:**
1. Иерархическая структура в JSON
2. Типизация связей в графе
3. Четкие критерии для оптимизации
4. Требования к документированию решений

## Part 3. Third prompt for AI
[todo] it will be added after receiving the result of calculating the previous AI query.

