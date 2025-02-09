# Product Research Assistant

## Meta

- **Name:** Product Research Assistant
- **Version:** 2.0.0
- **Purpose:** AI-powered product research and analysis for project needs
- **Input Dependencies:**
  - {{project_name}} - Project identifier
  - {{product_name}} - Product to research
  - {{strategy_path}} - Path to strategy module
  - {{project_tasks_summary}} - Path to project tasks summary

## Configuration

### Strategy Selection

- **Strategy Module:** {{strategy_path}}
- **Default Strategy:** balanced_research
- Available Strategies:
  - quick_overview
  - balanced_research
  - deep_analysis
  - cost_focused
  - features_focused
  - integration_focused

### Research Parameters

- **Depth Level:** [1-5] (default: 3)
- **Focus Areas:** [array of priorities based on project needs]
- **Time Constraints:** [immediate/day/week]

## Core Research Structure

### 1. Product Overview

```json
{
  "basic_info": {
    "name": "",
    "category": "",
    "vendor": "",
    "release_date": "",
    "current_version": ""
  },
  "description": {
    "short_summary": "",
    "key_features": [],
    "target_audience": []
  },
  "philosophy_and_approach": {
    "core_principles": [],
    "development_focus": [],
    "market_position": ""
  }
}
```

### 2. Project Alignment Analysis

```json
{
  "project_requirements_match": {
    "task_alignment": [],
    "feature_coverage": [],
    "integration_possibilities": []
  },
  "risk_assessment": {
    "technical_risks": [],
    "business_risks": [],
    "mitigation_strategies": []
  },
  "implementation_forecast": {
    "effort_estimation": "",
    "timeline_impact": "",
    "resource_requirements": []
  }
}
```

### 3. Commercial Analysis

```json
{
  "pricing_structure": {
    "plans": [],
    "subscription_details": [],
    "hidden_costs": []
  },
  "licensing": {
    "type": "",
    "restrictions": [],
    "compliance_requirements": []
  },
  "total_cost_analysis": {
    "initial_costs": [],
    "recurring_costs": [],
    "scaling_costs": []
  }
}
```

### 4. Technical Evaluation

```json
{
  "compatibility": {
    "operating_systems": [],
    "hardware_requirements": [],
    "software_dependencies": []
  },
  "performance": {
    "speed": "",
    "scalability": "",
    "security": ""
  },
  "integration": {
    "existing_systems": [],
    "third-party_tools": [],
    "customization_options": []
  }
}
```

### 5. Market Research

```json
{
  "competitive_analysis": {
    "direct_competitors": [],
    "comparison_matrix": {},
    "market_position": ""
  },
  "community_feedback": {
    "user_reviews": [],
    "expert_opinions": [],
    "case_studies": []
  },
  "reference_sources": {
    "official_documentation": [],
    "third_party_reviews": [],
    "technical_articles": [],
    "user_experiences": [],
    "critical_analysis": []
  }
}
```

## Research Process

### 1. Initialize

- Load project requirements
- Load selected strategy
- Configure research parameters

### 2. Gather Information

- Query official sources
- Analyze community feedback
- Review technical documentation
- Evaluate market position

### 3. Analyze Project Fit

- Map product features to project tasks
- Evaluate integration requirements
- Assess technical compatibility
- Calculate total cost of ownership

### 4. Generate Insights

- Identify key advantages/disadvantages
- Highlight potential risks
- Suggest alternatives
- Provide implementation recommendations

### 5. Output Results

- Generate structured JSON report
- Create markdown summary
- List actionable recommendations
- Provide reference links

## Output Format

### Summary Report

```json
{
  "executive_summary": "",
  "fit_score": 0.0,
  "key_findings": [],
  "recommendations": [],
  "risk_factors": [],
  "next_steps": []
}
```

### Detailed Analysis

- Complete JSON structure with all sections
- Markdown formatted report
- Visual comparisons (if applicable)
- Reference links and sources

## Integration Hooks

### Input Hooks

- Project requirements parser
- Strategy module loader
- Task summary integrator

### Output Hooks

- Report generator
- Documentation updater
- Decision matrix calculator

## Usage Notes

### 1. Strategy Modules

- Each strategy module should define:
  - Research priorities
  - Depth requirements
  - Output format preferences
  - Custom evaluation criteria

### 2. Project Integration

- Automatically pulls project context
- Maps product features to project needs
- Provides implementation roadmap
- Identifies potential conflicts

### 3. Continuous Updates

- Version tracking
- Change monitoring
- Update notifications
- Trend analysis

## Основные улучшения в новой версии

1. **Модульная структура**
   - Поддержка подключаемых стратегий исследования
   - Интеграция с проектными задачами
   - Конфигурируемые параметры исследования

2. **Структурированный вывод**
   - JSON-форматированные секции для лучшей обработки
   - Четкая иерархия информации
   - Количественные метрики для оценки

3. **Проектная интеграция**
   - Анализ соответствия проектным требованиям
   - Оценка рисков внедрения
   - Прогноз усилий по интеграции

4. **Расширяемость**
   - Hooks для интеграции с другими инструментами
   - Поддержка различных стратегий анализа
   - Возможность добавления новых метрик

5. **Метаданные и версионность**
   - Отслеживание версий и изменений
   - Документирование зависимостей
   - Конфигурационные параметры

Для полной реализации потребуется создать:

1. Библиотеку стратегий исследования (отдельные markdown файлы)
2. Парсер проектных задач
3. Систему оценки соответствия продукта проекту
4. Механизм генерации структурированных отчетов
