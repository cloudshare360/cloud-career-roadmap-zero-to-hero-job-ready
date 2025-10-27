#!/bin/bash
# Comprehensive link checking script for Cloud Career Roadmap

echo "🔍 Cloud Career Roadmap - Link Validation"
echo "========================================"
echo "Date: $(date)"
echo "Project: Zero to Hero Job Ready"
echo ""

# Change to project directory
PROJECT_DIR="/home/sri/Downloads/cloud-career-roadmap-zero-to-hero-job-ready"
cd "$PROJECT_DIR"

# Initialize counters and arrays
total_files=0
files_with_errors=0
declare -a error_files=()
declare -a all_files=()

echo "📁 Scanning for markdown files..."

# Find all markdown files (excluding node_modules and git)
while IFS= read -r -d '' file; do
    all_files+=("$file")
    total_files=$((total_files + 1))
done < <(find . -name "*.md" -not -path "./node_modules/*" -not -path "./.git/*" -not -path "./testing/*" -print0)

echo "Found $total_files markdown files to check"
echo ""

# Check if markdown-link-check is installed
if ! command -v markdown-link-check &> /dev/null; then
    echo "❌ markdown-link-check is not installed"
    echo "Installing now..."
    npm install -g markdown-link-check
    echo ""
fi

echo "🔗 Starting link validation..."
echo "---"

# Check each file
for file in "${all_files[@]}"; do
    echo "Checking: $file"
    
    # Run link check and capture output
    if output=$(markdown-link-check "$file" 2>&1); then
        echo "✅ All links OK"
    else
        files_with_errors=$((files_with_errors + 1))
        error_files+=("$file")
        echo "❌ ERRORS FOUND"
        echo "$output"
    fi
    echo "---"
done

# Generate summary
echo ""
echo "📊 VALIDATION SUMMARY"
echo "===================="
echo "Total files checked: $total_files"
echo "Files with errors: $files_with_errors"
echo "Files with valid links: $((total_files - files_with_errors))"

if [ $total_files -gt 0 ]; then
    success_rate=$(( (total_files - files_with_errors) * 100 / total_files ))
    echo "Success rate: $success_rate%"
else
    echo "Success rate: N/A (no files found)"
fi

echo ""

if [ $files_with_errors -eq 0 ]; then
    echo "🎉 EXCELLENT! All links are working correctly!"
    echo ""
    echo "✅ Your documentation is ready for:"
    echo "   - GitHub deployment"
    echo "   - User navigation"
    echo "   - Professional presentation"
    echo ""
    exit 0
else
    echo "⚠️  ATTENTION NEEDED"
    echo ""
    echo "Files with broken links:"
    for error_file in "${error_files[@]}"; do
        echo "   - $error_file"
    done
    echo ""
    echo "🔧 NEXT STEPS:"
    echo "1. Review the errors shown above"
    echo "2. Fix the broken links"
    echo "3. Re-run this script to verify fixes"
    echo "4. Consider using 'docsify serve' for live testing"
    echo ""
    exit 1
fi