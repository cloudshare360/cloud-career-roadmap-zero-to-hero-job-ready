# 📚 Docsify Documentation Server Setup
*Professional documentation server for local testing*

## 🎯 Why Docsify?
- **GitHub-like rendering**: Matches GitHub's markdown styling
- **Live reload**: Automatically refreshes when files change
- **Navigation sidebar**: Auto-generates navigation from folder structure
- **Search functionality**: Built-in search across all documents
- **Zero configuration**: Works out of the box with existing markdown files

---

## 🚀 Quick Setup

### **Step 1: Install Node.js (if not already installed)**
```bash
# Check if Node.js is installed
node --version
npm --version

# If not installed, install Node.js from https://nodejs.org/
# Or using your package manager:
sudo apt update
sudo apt install nodejs npm
```

### **Step 2: Install Docsify CLI**
```bash
# Install docsify globally
npm install -g docsify-cli

# Verify installation
docsify --version
```

### **Step 3: Initialize Docsify**
```bash
# Navigate to project root
cd /home/sri/Downloads/cloud-career-roadmap-zero-to-hero-job-ready

# Initialize docsify (this creates index.html and .nojekyll)
docsify init .
```

### **Step 4: Start the Server**
```bash
# Start docsify server
docsify serve . --port 3000

# Server will start at: http://localhost:3000
# Press Ctrl+C to stop the server
```

---

## 🔧 Configuration Options

### **Basic Configuration (index.html)**
The docsify init command creates an `index.html` file. You can customize it:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Cloud Career Roadmap - Zero to Hero Job Ready</title>
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <meta name="description" content="Complete cloud career acceleration system">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
</head>
<body>
  <div id="app"></div>
  <script>
    window.$docsify = {
      name: 'Cloud Career Roadmap',
      repo: 'https://github.com/cloudshare360/cloud-career-roadmap-zero-to-hero-job-ready',
      loadSidebar: true,
      autoHeader: true,
      subMaxLevel: 3,
      search: 'auto',
      pagination: {
        previousText: '← Previous',
        nextText: 'Next →',
        crossChapter: true,
        crossChapterText: true,
      },
    }
  </script>
  <!-- Docsify v4 -->
  <script src="//cdn.jsdelivr.net/npm/docsify@4"></script>
  <!-- Search plugin -->
  <script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
  <!-- Pagination plugin -->
  <script src="//cdn.jsdelivr.net/npm/docsify-pagination/dist/docsify-pagination.min.js"></script>
</body>
</html>
```

### **Sidebar Configuration (_sidebar.md)**
Create a `_sidebar.md` file for custom navigation:

```markdown
* [Home](/)
* [Getting Started](README.md)

* **Immediate Action (Weeks 1-8)**
  * **Job Acquisition**
    * [Immediate Job Acquisition Plan](docs/01-immediate/job-acquisition/immediate-job-acquisition-plan.md)
    * [Daily Job Search System](docs/01-immediate/job-acquisition/daily-job-search-system.md)
    * [Salary Negotiation Tactics](docs/01-immediate/job-acquisition/salary-negotiation-tactics.md)
    * [Interview Excellence Guide](docs/01-immediate/job-acquisition/interview-excellence-guide.md)
  
  * **Skill Enhancement**
    * [Skills Gap Analysis](docs/01-immediate/skill-enhancement/skills-gap-analysis.md)
    * [4-Week Intensive Learning](docs/01-immediate/skill-enhancement/4-week-intensive-learning.md)
    * [AWS Certification Fast Track](docs/01-immediate/skill-enhancement/aws-certification-fast-track.md)
    * [Serverless Mastery Accelerated](docs/01-immediate/skill-enhancement/serverless-mastery-accelerated.md)
  
  * **Portfolio Strategies**
    * [Job-Winning Portfolio Guide](docs/01-immediate/portfolio-strategies/job-winning-portfolio-guide.md)
    * [Advanced Serverless Projects](docs/01-immediate/portfolio-strategies/advanced-serverless-projects.md)
    * [GitHub Optimization Guide](docs/01-immediate/portfolio-strategies/github-optimization-guide.md)
    * [Technical Presentation Skills](docs/01-immediate/portfolio-strategies/technical-presentation-skills.md)

* **Testing**
  * [Documentation Testing](testing/README.md)
```

---

## 🧪 Testing Workflow

### **1. Start Testing Session**
```bash
# Open terminal and start docsify
cd /home/sri/Downloads/cloud-career-roadmap-zero-to-hero-job-ready
docsify serve . --port 3000

# Open browser to http://localhost:3000
```

### **2. Systematic Link Testing**
1. **Navigate through all main sections**
2. **Click every link in README.md**
3. **Test cross-references between documents**
4. **Verify all file paths are correct**
5. **Check that images and diagrams load**

### **3. Document Testing Checklist**
```markdown
MAIN NAVIGATION:
□ README.md loads correctly
□ All main section links work
□ Directory structure is accessible

JOB ACQUISITION SECTION:
□ immediate-job-acquisition-plan.md
□ daily-job-search-system.md
□ salary-negotiation-tactics.md
□ interview-excellence-guide.md

SKILL ENHANCEMENT SECTION:
□ skills-gap-analysis.md
□ 4-week-intensive-learning.md
□ aws-certification-fast-track.md
□ serverless-mastery-accelerated.md

PORTFOLIO STRATEGIES SECTION:
□ job-winning-portfolio-guide.md
□ advanced-serverless-projects.md (to be created)
□ github-optimization-guide.md (to be created)
□ technical-presentation-skills.md (to be created)

CROSS-REFERENCES:
□ Internal document links work
□ Section references are accurate
□ File paths are correct
□ No broken links exist
```

### **4. Advanced Testing Features**

#### **Live Reload Testing**
- Edit any markdown file
- Save the changes
- Browser automatically refreshes
- Verify changes appear correctly

#### **Search Testing**
- Use the search box (if enabled)
- Search for key terms
- Verify search results link correctly

#### **Mobile Responsive Testing**
- Resize browser window
- Test on mobile device
- Verify navigation works on smaller screens

---

## 🔍 Troubleshooting

### **Common Issues & Solutions**

#### **Docsify not found**
```bash
# Reinstall docsify globally
npm uninstall -g docsify-cli
npm install -g docsify-cli
```

#### **Port already in use**
```bash
# Use different port
docsify serve . --port 3001

# Or kill existing process
lsof -ti:3000 | xargs kill -9
```

#### **Links not working**
- Check file paths are relative to project root
- Ensure file extensions are included (.md)
- Verify files actually exist at specified paths

#### **Styling issues**
- Clear browser cache
- Try different docsify theme
- Check for conflicting CSS

---

## 🎯 Testing Results Documentation

### **Create Testing Report**
Document your testing results:

```markdown
# Link Testing Report
Date: [Current Date]
Tester: [Your Name]

## Summary
- Total links tested: ___
- Working links: ___
- Broken links: ___
- Success rate: ___%

## Broken Links Found
1. [Link description] - [File path] - [Error description]
2. [Link description] - [File path] - [Error description]

## Recommendations
- [List of fixes needed]
- [Suggested improvements]

## Next Steps
- [Action items to resolve issues]
```

---

## 🚀 Advanced Usage

### **Custom Plugins**
Add additional functionality:

```html
<!-- Add to index.html -->
<!-- Zoom image plugin -->
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/zoom-image.min.js"></script>

<!-- Copy code plugin -->
<script src="//cdn.jsdelivr.net/npm/docsify-copy-code/dist/docsify-copy-code.min.js"></script>

<!-- Tabs plugin -->
<script src="//cdn.jsdelivr.net/npm/docsify-tabs@1"></script>
```

### **Performance Optimization**
```javascript
window.$docsify = {
  // ... other config
  relativePath: true,
  notFoundPage: true,
  executeScript: true,
  maxLevel: 4,
  subMaxLevel: 3
}
```

---

**Next Steps:**
1. Run the setup commands above
2. Test all navigation links systematically
3. Document any broken links found
4. Fix issues and retest
5. Proceed with confidence that all links work correctly

*This testing setup ensures your documentation works perfectly before users access it on GitHub.*