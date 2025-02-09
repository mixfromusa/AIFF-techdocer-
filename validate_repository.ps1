# Repository validation script

# Configuration
$CONFIG = @{
    RequiredMetadataFields = @('type', 'status', 'version', 'tags', 'created', 'updated')
    AllowedFileTypes = @('.md', '.json', '.yaml', '.ps1', '.sh')
    MaxFileSize = 1MB
    MaxLineLength = 120
    MinReadmeLength = 50
}

function Test-FileMetadata {
    param (
        [string]$filePath
    )
    
    $results = @{
        file = $filePath
        issues = @()
    }
    
    $content = Get-Content $filePath -Raw
    
    # Check for metadata section
    if ($content -match '^---\s*\n(.*?)\n---\s*\n') {
        $metadata = $matches[1]
        
        # Verify required fields
        foreach ($field in $CONFIG.RequiredMetadataFields) {
            if ($metadata -notmatch "$field:\s*.+") {
                $results.issues += "Missing required metadata field: $field"
            }
        }
        
        # Validate version format
        if ($metadata -match 'version:\s*(.+)') {
            if ($matches[1] -notmatch '^\d+\.\d+\.\d+$') {
                $results.issues += "Invalid version format. Should be x.y.z"
            }
        }
        
        # Validate dates
        foreach ($dateField in @('created', 'updated')) {
            if ($metadata -match "$dateField:\s*(.+)") {
                try {
                    [datetime]::ParseExact($matches[1], 'yyyy-MM-dd', $null)
                }
                catch {
                    $results.issues += "Invalid date format in $dateField. Use YYYY-MM-DD"
                }
            }
        }
    }
    else {
        $results.issues += "Missing metadata section"
    }
    
    return $results
}

function Test-ContentStructure {
    param (
        [string]$filePath
    )
    
    $results = @{
        file = $filePath
        issues = @()
    }
    
    $content = Get-Content $filePath
    
    # Check line length
    $longLines = $content | Where-Object { $_.Length -gt $CONFIG.MaxLineLength }
    if ($longLines) {
        $results.issues += "Lines exceeding maximum length ($($CONFIG.MaxLineLength) chars)"
    }
    
    # Check markdown structure (for .md files)
    if ($filePath -match '\.md$') {
        # Verify heading hierarchy
        $headings = $content | Where-Object { $_ -match '^#+\s' }
        $previousLevel = 0
        foreach ($heading in $headings) {
            $level = ($heading -match '^(#+)')[0].length
            if ($level - $previousLevel -gt 1) {
                $results.issues += "Invalid heading hierarchy: $heading"
            }
            $previousLevel = $level
        }
        
        # Check for empty sections
        $sections = 0..($headings.Count-2) | ForEach-Object {
            @{
                heading = $headings[$_]
                content = $content[($content.IndexOf($headings[$_]))..($content.IndexOf($headings[$_+1]))]
            }
        }
        foreach ($section in $sections) {
            if ($section.content.Count -le 1) {
                $results.issues += "Empty section: $($section.heading)"
            }
        }
    }
    
    return $results
}

function Test-RepositoryStructure {
    $results = @{
        structure = @()
        files = @()
    }
    
    # Check required directories
    $requiredDirs = @('core', 'prompts', 'ai', 'tools', 'docs', 'config')
    foreach ($dir in $requiredDirs) {
        if (-not (Test-Path $dir)) {
            $results.structure += "Missing required directory: $dir"
        }
        else {
            # Check for README
            if (-not (Test-Path (Join-Path $dir "README.md"))) {
                $results.structure += "Missing README.md in $dir"
            }
        }
    }
    
    # Validate file locations
    Get-ChildItem -Recurse -File | ForEach-Object {
        # Check file type
        if ($_.Extension -notin $CONFIG.AllowedFileTypes) {
            $results.files += "Unsupported file type: $($_.FullName)"
        }
        
        # Check file size
        if ($_.Length -gt $CONFIG.MaxFileSize) {
            $results.files += "File too large: $($_.FullName)"
        }
        
        # Check file location
        switch -Regex ($_.FullName) {
            '/prompts/.*\.md$' {
                $metadata = Test-FileMetadata $_.FullName
                if ($metadata.issues) {
                    $results.files += $metadata.issues
                }
            }
            '/core/types/.*' {
                if ($_.Extension -notin @('.json', '.yaml')) {
                    $results.files += "Invalid file type for types directory: $($_.FullName)"
                }
            }
            '/docs/.*\.md$' {
                $structure = Test-ContentStructure $_.FullName
                if ($structure.issues) {
                    $results.files += $structure.issues
                }
            }
        }
    }
    
    return $results
}

function Test-NamingConventions {
    $results = @()
    
    Get-ChildItem -Recurse -File | ForEach-Object {
        # Check file naming
        switch -Regex ($_.FullName) {
            '/prompts/templates/.*' {
                if ($_.Name -notmatch '^[a-z0-9-]+\.md$') {
                    $results += "Invalid template name format: $($_.FullName)"
                }
            }
            '/core/types/.*' {
                if ($_.Name -notmatch '^[A-Z][a-zA-Z0-9]+\.(json|yaml)$') {
                    $results += "Invalid type name format: $($_.FullName)"
                }
            }
        }
    }
    
    return $results
}

# Run all checks
$validationResults = @{
    repository = Test-RepositoryStructure
    naming = Test-NamingConventions
}

# Generate report
$report = @"
# Repository Validation Report
Generated: $(Get-Date)

## Structure Issues
$($validationResults.repository.structure | ForEach-Object { "- $_`n" })

## File Issues
$($validationResults.repository.files | ForEach-Object { "- $_`n" })

## Naming Convention Issues
$($validationResults.naming | ForEach-Object { "- $_`n" })

## Recommendations
1. Fix all metadata issues in prompt files
2. Ensure proper file organization
3. Follow naming conventions
4. Add missing README files
"@

Set-Content -Path "validation_report.md" -Value $report

Write-Host "Validation completed. Check validation_report.md for results."