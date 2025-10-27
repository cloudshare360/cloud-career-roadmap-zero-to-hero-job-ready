# 💻 VSCode Markdown Preview Setup
*IDE-integrated testing for markdown navigation*

## 🎯 Why Use VSCode Preview?
- **Integrated workflow**: Test without leaving your editor
- **Live preview**: Real-time updates as you edit
- **Side-by-side**: Code and preview simultaneously
- **Git integration**: See changes alongside documentation
- **Extension ecosystem**: Enhanced markdown features

---

## 🚀 Setup & Configuration

### **Required VSCode Extensions**

#### **Essential Extensions**
```
1. Markdown All in One
   - ID: yzhang.markdown-all-in-one
   - Features: TOC, preview, shortcuts

2. Markdown Preview Enhanced
   - ID: shd101wyy.markdown-preview-enhanced
   - Features: Advanced preview, math, diagrams

3. Live Server
   - ID: ritwickdey.liveserver
   - Features: Local server with live reload

4. Markdown Links
   - ID: tchayen.markdown-links
   - Features: Link validation and navigation
```

#### **Installation Commands**
```bash
# Install via command line
code --install-extension yzhang.markdown-all-in-one
code --install-extension shd101wyy.markdown-preview-enhanced
code --install-extension ritwickdey.liveserver
code --install-extension tchayen.markdown-links
```

### **VSCode Settings Configuration**
Create/update `.vscode/settings.json`:

```json
{
  "markdown.preview.breaks": true,
  "markdown.preview.linkify": true,
  "markdown.preview.typographer": true,
  "markdown.extension.toc.updateOnSave": true,
  "markdown.extension.preview.autoShowPreviewToSide": true,
  "markdown.extension.orderedList.marker": "one",
  "markdown.extension.italic.indicator": "*",
  "markdown.extension.bold.indicator": "**",
  "markdown.extension.tableFormatter.enabled": true,
  "markdown.extension.completion.respectVscodeSearchExclude": true,
  "markdownlint.config": {
    "MD013": false,
    "MD033": false,
    "MD041": false
  },
  "liveServer.settings.root": "/",
  "liveServer.settings.CustomBrowser": "chrome",
  "liveServer.settings.port": 5500,
  "liveServer.settings.donotShowInfoMsg": true,
  "files.associations": {
    "*.md": "markdown"
  }
}
```

### **Workspace Configuration**
Create `.vscode/launch.json` for debugging:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Preview Markdown",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}",
      "console": "integratedTerminal"
    }
  ]
}
```

---

## 🧪 Testing Workflow

### **Method 1: Built-in Preview**

#### **Basic Preview**
```
1. Open any .md file in VSCode
2. Press Ctrl+Shift+V (or Cmd+Shift+V on Mac)
3. Preview opens in new tab
4. Click links to test navigation
```

#### **Side-by-Side Preview**
```
1. Open .md file
2. Press Ctrl+K V (or Cmd+K V on Mac)
3. Preview opens beside editor
4. Edit and see live updates
5. Test links in preview pane
```

### **Method 2: Live Server Integration**

#### **Setup Live Server**
```
1. Right-click on project folder
2. Select "Open with Live Server"
3. Browser opens automatically
4. Navigate to any .md file
5. Test all links and navigation
```

#### **Advanced Live Server**
```
1. Install "Live Server" extension
2. Configure settings in .vscode/settings.json
3. Right-click index.html or any file
4. Select "Open with Live Server"
5. Browser auto-refreshes on file changes
```

### **Method 3: Enhanced Preview**

#### **Markdown Preview Enhanced**
```
1. Open .md file
2. Press Ctrl+Shift+M (or Cmd+Shift+M)
3. Enhanced preview with:
   - Math equations
   - Diagrams (mermaid)
   - Custom CSS
   - Export options
```

---

## 🔧 Advanced Configuration

### **Custom CSS for Preview**
Create `.vscode/markdown.css`:

```css
/* GitHub-like styling for VSCode preview */
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
  line-height: 1.6;
  color: #24292e;
  background-color: #ffffff;
  max-width: 1012px;
  margin: 0 auto;
  padding: 45px;
}

h1, h2, h3, h4, h5, h6 {
  margin-top: 24px;
  margin-bottom: 16px;
  font-weight: 600;
  line-height: 1.25;
}

h1 {
  font-size: 2em;
  border-bottom: 1px solid #eaecef;
  padding-bottom: 0.3em;
}

h2 {
  font-size: 1.5em;
  border-bottom: 1px solid #eaecef;
  padding-bottom: 0.3em;
}

code {
  background-color: rgba(27,31,35,0.05);
  border-radius: 3px;
  font-size: 85%;
  margin: 0;
  padding: 0.2em 0.4em;
}

pre {
  background-color: #f6f8fa;
  border-radius: 3px;
  font-size: 85%;
  line-height: 1.45;
  overflow: auto;
  padding: 16px;
}

blockquote {
  border-left: 0.25em solid #dfe2e5;
  color: #6a737d;
  padding: 0 1em;
}

table {
  border-collapse: collapse;
  border-spacing: 0;
}

table th,
table td {
  border: 1px solid #dfe2e5;
  padding: 6px 13px;
}

table th {
  background-color: #f6f8fa;
  font-weight: 600;
}

a {
  color: #0366d6;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
```

### **Update VSCode Settings for Custom CSS**
Add to `.vscode/settings.json`:

```json
{
  "markdown.styles": [
    ".vscode/markdown.css"
  ],
  "markdown.preview.fontFamily": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
}
```

---

## 📋 Testing Checklists

### **VSCode Preview Testing Checklist**
```markdown
SETUP VERIFICATION:
□ VSCode extensions installed
□ Settings configured correctly
□ Custom CSS applied (optional)
□ Live server extension working

BASIC PREVIEW TESTING:
□ Ctrl+Shift+V opens preview
□ Ctrl+K V opens side-by-side
□ Links clickable in preview
□ Images display correctly
□ Tables format properly
□ Code blocks render correctly

NAVIGATION TESTING:
□ Internal links work in preview
□ Cross-document references function
□ Anchor links (# headers) work
□ Relative paths resolve correctly
□ File extensions recognized

LIVE SERVER TESTING:
□ Live server starts correctly
□ Browser opens automatically
□ File changes trigger refresh
□ All markdown files accessible
□ Navigation works in browser
```

### **Systematic Link Testing Process**
```markdown
TESTING WORKFLOW:
1. Open README.md in VSCode
2. Start side-by-side preview (Ctrl+K V)
3. Click each link in preview pane
4. Verify target document opens
5. Test back navigation
6. Document any broken links

FILES TO TEST:
□ /README.md
□ /docs/01-immediate/README.md
□ /docs/01-immediate/job-acquisition/immediate-job-acquisition-plan.md
□ /docs/01-immediate/job-acquisition/daily-job-search-system.md
□ /docs/01-immediate/job-acquisition/salary-negotiation-tactics.md
□ /docs/01-immediate/job-acquisition/interview-excellence-guide.md
□ /docs/01-immediate/skill-enhancement/skills-gap-analysis.md
□ /docs/01-immediate/skill-enhancement/4-week-intensive-learning.md
□ /docs/01-immediate/skill-enhancement/aws-certification-fast-track.md
□ /docs/01-immediate/skill-enhancement/serverless-mastery-accelerated.md
□ /docs/01-immediate/portfolio-strategies/job-winning-portfolio-guide.md
```

---

## 🔍 Link Validation in VSCode

### **Using Markdown Links Extension**

#### **Features**
- Automatic link detection
- Broken link highlighting
- Quick navigation between files
- Link completion suggestions

#### **Usage**
```
1. Install "Markdown Links" extension
2. Open any .md file
3. Broken links highlighted in red
4. Hover for error details
5. Ctrl+Click to navigate links
```

### **Manual Link Testing**

#### **Testing Internal Links**
```markdown
PROCESS:
1. Open document with internal links
2. Hold Ctrl and click link (or Cmd+click on Mac)
3. Verify correct file opens
4. Check if target section/header exists
5. Test return navigation

COMMON ISSUES:
- Incorrect relative paths
- Missing file extensions (.md)
- Case sensitivity problems
- Spaces in filenames
```

#### **Testing External Links**
```markdown
PROCESS:
1. Click external links in preview
2. Verify they open in browser
3. Check if destinations are valid
4. Test https vs http protocols

VALIDATION:
- GitHub repository links
- Documentation references
- External tool links
- Resource downloads
```

---

## 📊 Testing Documentation

### **Create VSCode Testing Log**
Create `testing/vscode-test-log.md`:

```markdown
# VSCode Preview Testing Log

## Test Environment
- **Date**: [Current Date]
- **VSCode Version**: [Check Help → About]
- **Extensions Installed**: 
  - Markdown All in One: [Version]
  - Markdown Preview Enhanced: [Version]
  - Live Server: [Version]
  - Markdown Links: [Version]

## Preview Testing Results

### Basic Functionality
- [x] Side-by-side preview works
- [x] Live preview updates correctly
- [x] Links clickable in preview
- [x] Custom CSS applied

### Navigation Testing
- [x] Internal links function
- [x] Cross-document references work
- [x] Anchor links to headers work
- [ ] All file paths accessible

### Issues Found
1. **[Issue description]**
   - File: [filename]
   - Link: [broken link]
   - Error: [error description]
   - Fix: [how to resolve]

## Recommendations
- [List of improvements needed]
- [Suggested workflow changes]

## Next Steps
- [ ] Fix identified issues
- [ ] Re-test in VSCode
- [ ] Validate with other methods
```

---

## 🎯 Workflow Integration

### **Daily Development Workflow**
```markdown
RECOMMENDED PROCESS:
1. Open VSCode in project root
2. Enable side-by-side preview (Ctrl+K V)
3. Edit markdown files
4. Test links immediately in preview
5. Use Live Server for browser testing
6. Commit only after link validation
```

### **Pre-commit Testing**
```markdown
CHECKLIST BEFORE COMMIT:
□ All new files previewed in VSCode
□ Links tested in preview pane
□ Live server validation completed
□ No broken link warnings
□ Cross-references verified
```

---

## 🚀 Quick Start Commands

### **Essential VSCode Commands**
```
Ctrl+Shift+V      - Open preview in new tab
Ctrl+K V          - Open preview to the side
Ctrl+Shift+M      - Enhanced preview (if extension installed)
Ctrl+Shift+P      - Command palette
F1                - Help and commands
Ctrl+`            - Toggle terminal
```

### **File Navigation**
```
Ctrl+P            - Quick file open
Ctrl+Shift+E      - Explorer sidebar
Ctrl+G            - Go to line
Ctrl+T            - Go to symbol
Ctrl+Shift+O      - Go to symbol in file
```

---

**Immediate Setup:**
1. Install recommended extensions
2. Configure settings.json
3. Open README.md and start side-by-side preview
4. Test all navigation links systematically
5. Document any issues found

*VSCode provides the most integrated experience for testing and developing your documentation workflow.*