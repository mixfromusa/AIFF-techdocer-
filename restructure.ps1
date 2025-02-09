# Restructure script for KnowledgeBase project

# Function to create directory with README
function Create-DirectoryWithReadme {
    param (
        [string]$path,
        [string]$description,
        [string]$details
    )
    
    # Create directory if it doesn't exist
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path -Force
        Write-Host "Created directory: $path"
    }
    
    # Create README.md
    $readmeContent = @"
# $(Split-Path $path -Leaf)

## Description
$description

## Contents
$details

## Usage Guidelines
- Place relevant files in appropriate subdirectories
- Follow naming conventions defined in /docs/standards
- Update this README when adding new components

## Structure
"@
    
    Set-Content -Path (Join-Path $path "README.md") -Value $readmeContent
    Write-Host "Created README for: $path"
}

# Define new structure with descriptions
$structure = @{
    "core" = @{
        "path" = "core"
        "description" = "Core components of the knowledge base system"
        "subdirs" = @{
            "types" = "Type definitions and formats"
            "schemas" = "Data schemas and structures"
            "interfaces" = "Interface definitions"
        }
    }
    "prompts" = @{
        "path" = "prompts"
        "description" = "Prompt templates and management"
        "subdirs" = @{
            "templates" = "Base prompt templates"
            "directives" = "AI directives"
            "modes" = "Operation modes"
            "scripts" = "Prompt processing scripts"
        }
    }
    "ai" = @{
        "path" = "ai"
        "description" = "AI-specific components and integrations"
        "subdirs" = @{
            "models" = "AI model information"
            "integrations" = "AI integration components"
            "competitions" = "Bot competition materials"
        }
    }
    "tools" = @{
        "path" = "tools"
        "description" = "Utility tools and helpers"
        "subdirs" = @{
            "translators" = "Translation tools"
            "analyzers" = "Analysis tools"
            "converters" = "Format converters"
        }
    }
    "docs" = @{
        "path" = "docs"
        "description" = "Project documentation"
        "subdirs" = @{
            "standards" = "Standards and guidelines"
            "api" = "API documentation"
            "guides" = "User guides"
        }
    }
    "config" = @{
        "path" = "config"
        "description" = "Configuration files"
        "subdirs" = @{
            "personal" = "Personal settings"
            "system" = "System settings"
        }
    }
}

# Create migration log
$migrationLog = @"
# Migration Log

## Started: $(Get-Date)

## Actions:
"@

# Create new structure
foreach ($dir in $structure.Keys) {
    $mainDir = $structure[$dir]
    Create-DirectoryWithReadme -path $mainDir.path -description $mainDir.description -details "Subdirectories:"
    
    # Create subdirectories
    foreach ($subdir in $mainDir.subdirs.Keys) {
        $subdirPath = Join-Path $mainDir.path $subdir
        Create-DirectoryWithReadme -path $subdirPath -description $mainDir.subdirs[$subdir] -details "Place relevant files here"
    }
    
    $migrationLog += "`nCreated directory structure for: $dir"
}

# Move existing files to new structure
$fileMapping = @{
    "MyPrompts/*" = "prompts/templates/"
    "API/*" = "docs/api/"
    "Standarts/*" = "docs/standards/"
    "types/*" = "core/types/"
    "Configs/*" = "config/system/"
}

foreach ($source in $fileMapping.Keys) {
    $destination = $fileMapping[$source]
    
    if (Test-Path $source) {
        Get-ChildItem -Path $source -Recurse | ForEach-Object {
            $destPath = Join-Path $destination $_.Name
            if (-not (Test-Path $destPath)) {
                Copy-Item $_.FullName -Destination $destPath -Force
                $migrationLog += "`nMoved: $($_.Name) to $destination"
            }
        }
    }
}

# Save migration log
$migrationLog += "`n`n## Completed: $(Get-Date)"
Set-Content -Path "migration_log.md" -Value $migrationLog

Write-Host "Structure reorganization completed. Check migration_log.md for details."
