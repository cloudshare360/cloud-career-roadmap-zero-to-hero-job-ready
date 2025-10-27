# 🔗 Markdown Link Checker Setup
*Automated validation of all markdown links*

## 🎯 Why Use Link Checker?
- **Automated scanning**: Checks all markdown files automatically
- **Comprehensive validation**: Tests internal and external links
- **CI/CD integration**: Can be integrated into GitHub Actions
- **Detailed reporting**: Shows exactly which links are broken
- **Fast execution**: Quickly scans entire documentation tree

---

## 🚀 Quick Setup & Usage

### **Method 1: NPM-based Link Checker**

#### **Install markdown-link-check**
```bash
# Install globally
npm install -g markdown-link-check

# Or install locally in project
cd /home/sri/Downloads/cloud-career-roadmap-zero-to-hero-job-ready
npm init -y
npm install --save-dev markdown-link-check
```

#### **Basic Usage**
```bash
# Check single file
markdown-link-check README.md

# Check all markdown files
find . -name "*.md" -exec markdown-link-check {} \;

# Check with custom config
markdown-link-check -c .markdown-link-check.json README.md
```

### **Method 2: GitHub CLI Link Checker**

#### **Install GitHub CLI**
```bash
# Install gh CLI (if not already installed)
sudo apt update
sudo apt install gh

# Or download from https://cli.github.com/
```

#### **Use Repository Link Checker**
```bash
# Clone and use markdown-link-check-action locally
git clone https://github.com/gaurav-nelson/github-action-markdown-link-check.git
cd github-action-markdown-link-check
```

---

## 🔧 Configuration

### **Create Configuration File**
Create `.markdown-link-check.json` in project root:

```json
{
  "ignorePatterns": [
    {
      "pattern": "^http://localhost"
    },
    {
      "pattern": "^https://localhost"
    },
    {
      "pattern": "^#"
    }
  ],
  "replacementPatterns": [
    {
      "pattern": "^/",
      "replacement": "file://{{BASEURL}}/"
    }
  ],
  "httpHeaders": [
    {
      "urls": ["https://github.com"],
      "headers": {
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "markdown-link-check"
      }
    }
  ],
  "timeout": "20s",
  "retryOn429": true,
  "retryCount": 3,
  "fallbackHTTPStatus": [400, 401, 403, 404, 500, 502, 503, 504]
}
```

### **Advanced Configuration Options**
```json
{
  "ignorePatterns": [
    {
      "pattern": "^http://localhost",
      "comment": "Ignore localhost links during testing"
    },
    {
      "pattern": "^mailto:",
      "comment": "Ignore email links"
    },
    {
      "pattern": "^tel:",
      "comment": "Ignore telephone links"
    }
  ],
  "replacementPatterns": [
    {
      "pattern": "^docs/",
      "replacement": "{{BASEURL}}/docs/",
      "comment": "Convert relative paths to absolute"
    }
  ],
  "aliveStatusCodes": [200, 206, 999],
  "timeout": "30s",
  "retryOn429": true,
  "retryCount": 5
}
```

---

## 🧪 Testing Scripts

### **Create Testing Scripts**

#### **basic-link-check.sh**
```bash
#!/bin/bash
# Basic link checking script

echo "🔍 Starting markdown link check..."
echo "Project: Cloud Career Roadmap"
echo "Date: $(date)"
echo "================================"

# Change to project directory
cd /home/sri/Downloads/cloud-career-roadmap-zero-to-hero-job-ready

# Initialize counters
total_files=0
files_with_errors=0
total_links=0
broken_links=0

# Find all markdown files and check them
for file in $(find . -name "*.md" -not -path "./node_modules/*" -not -path "./.git/*"); do
    echo "Checking: $file"
    total_files=$((total_files + 1))
    
    # Run link check and capture output
    output=$(markdown-link-check "$file" 2>&1)
    exit_code=$?
    
    if [ $exit_code -ne 0 ]; then
        files_with_errors=$((files_with_errors + 1))
        echo "❌ ERRORS FOUND in $file"
        echo "$output"
        echo "---"
    else
        echo "✅ All links OK in $file"
    fi
done

echo "================================"
echo "📊 SUMMARY"
echo "Total files checked: $total_files"
echo "Files with errors: $files_with_errors"
echo "Success rate: $(( (total_files - files_with_errors) * 100 / total_files ))%"

if [ $files_with_errors -eq 0 ]; then
    echo "🎉 All links are working correctly!"
    exit 0
else
    echo "⚠️  Found broken links in $files_with_errors files"
    exit 1
fi
```

#### **detailed-link-check.sh**
```bash
#!/bin/bash
# Detailed link checking with reporting

REPORT_FILE="testing/link-check-report-$(date +%Y%m%d-%H%M%S).md"
PROJECT_DIR="/home/sri/Downloads/cloud-career-roadmap-zero-to-hero-job-ready"

cd "$PROJECT_DIR"

echo "# Link Check Report" > "$REPORT_FILE"
echo "Generated: $(date)" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "## Summary" >> "$REPORT_FILE"
echo "| Metric | Value |" >> "$REPORT_FILE"
echo "|--------|-------|" >> "$REPORT_FILE"

total_files=0
error_files=0
all_errors=""

for file in $(find . -name "*.md" -not -path "./node_modules/*" -not -path "./.git/*"); do
    total_files=$((total_files + 1))
    echo "Checking: $file"
    
    output=$(markdown-link-check "$file" 2>&1)
    if [ $? -ne 0 ]; then
        error_files=$((error_files + 1))
        all_errors="$all_errors\n### $file\n\`\`\`\n$output\n\`\`\`\n"
    fi
done

success_rate=$(( (total_files - error_files) * 100 / total_files ))

echo "| Total Files | $total_files |" >> "$REPORT_FILE"
echo "| Files with Errors | $error_files |" >> "$REPORT_FILE"
echo "| Success Rate | $success_rate% |" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

if [ $error_files -gt 0 ]; then
    echo "## Detailed Errors" >> "$REPORT_FILE"
    echo -e "$all_errors" >> "$REPORT_FILE"
else
    echo "## Result" >> "$REPORT_FILE"
    echo "🎉 All links are working correctly!" >> "$REPORT_FILE"
fi

echo "Report saved to: $REPORT_FILE"
```

### **Make Scripts Executable**
```bash
chmod +x testing/basic-link-check.sh
chmod +x testing/detailed-link-check.sh
```

---

## 🎯 Running Link Checks

### **Quick Check (Single Command)**
```bash
cd /home/sri/Downloads/cloud-career-roadmap-zero-to-hero-job-ready

# Quick check all files
find . -name "*.md" -not -path "./node_modules/*" -exec markdown-link-check {} \;

# Check with config file
find . -name "*.md" -not -path "./node_modules/*" -exec markdown-link-check -c .markdown-link-check.json {} \;
```

### **Comprehensive Testing**
```bash
# Run basic check
./testing/basic-link-check.sh

# Run detailed check with report
./testing/detailed-link-check.sh

# View the latest report
ls -la testing/link-check-report-*.md | tail -1 | xargs cat
```

### **Specific Section Testing**
```bash
# Check only job acquisition files
find docs/01-immediate/job-acquisition -name "*.md" -exec markdown-link-check {} \;

# Check only skill enhancement files
find docs/01-immediate/skill-enhancement -name "*.md" -exec markdown-link-check {} \;

# Check main README files
markdown-link-check README.md
markdown-link-check docs/01-immediate/README.md
```

---

## 📊 Interpreting Results

### **Successful Check Output**
```
FILE: docs/01-immediate/job-acquisition/immediate-job-acquisition-plan.md
  ✓ https://github.com/cloudshare360/cloud-career-roadmap-zero-to-hero-job-ready
  ✓ ./daily-job-search-system.md
  ✓ ./salary-negotiation-tactics.md
  
  3 links checked.
```

### **Failed Check Output**
```
FILE: docs/01-immediate/portfolio-strategies/advanced-serverless-projects.md
  ✗ ./missing-file.md → Status: 404 (Not Found)
  ✓ ./job-winning-portfolio-guide.md
  
  2 links checked.
  
ERROR: 1 dead links found!
```

### **Common Error Types**
- **404 Not Found**: File doesn't exist at specified path
- **File not found**: Relative path is incorrect
- **Connection timeout**: External link is slow or unavailable
- **SSL certificate**: HTTPS certificate issues

---

## 🔧 Integration with Development Workflow

### **Pre-commit Hook**
Create `.git/hooks/pre-commit`:
```bash
#!/bin/bash
echo "Running markdown link check..."
if ! ./testing/basic-link-check.sh; then
    echo "❌ Link check failed. Please fix broken links before committing."
    exit 1
fi
echo "✅ All links are working correctly."
```

### **GitHub Actions Integration**
Create `.github/workflows/link-check.yml`:
```yaml
name: Check Markdown Links

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  markdown-link-check:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: gaurav-nelson/github-action-markdown-link-check@v1
      with:
        config-file: '.markdown-link-check.json'
        folder-path: 'docs/'
        max-depth: -1
```

---

## 🎯 Testing Workflow

### **Daily Testing Routine**
1. **Before making changes**: Run quick link check
2. **After adding new files**: Run comprehensive check
3. **Before committing**: Run full validation
4. **Before pushing**: Final verification

### **Testing Checklist**
```markdown
PRE-DEVELOPMENT:
□ Run baseline link check
□ Document current status

DURING DEVELOPMENT:
□ Check links as you create them
□ Test internal references immediately
□ Validate file paths are correct

POST-DEVELOPMENT:
□ Run comprehensive link check
□ Generate detailed report
□ Fix any broken links found
□ Re-run verification

PRE-COMMIT:
□ Final link validation
□ Ensure all new files are included
□ Verify no regressions introduced
```

---

**Quick Start Commands:**
```bash
# Install and run immediately
npm install -g markdown-link-check
cd /home/sri/Downloads/cloud-career-roadmap-zero-to-hero-job-ready
find . -name "*.md" -exec markdown-link-check {} \;
```

*This automated approach ensures all your documentation links work perfectly before users encounter them.*