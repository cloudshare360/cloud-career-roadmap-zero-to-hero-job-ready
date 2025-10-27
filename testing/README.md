# 🔍 Documentation Testing Suite
*Local testing environment for markdown navigation and link validation*

## 🎯 Testing Overview
This folder contains tools and scripts to test all markdown links locally before deploying to GitHub, ensuring perfect navigation and user experience.

## 🛠️ Available Testing Methods

### **Method 1: Docsify Server (Recommended)**
Lightweight documentation server that mimics GitHub's markdown rendering.

### **Method 2: Markdown Link Checker**
Automated tool to scan and validate all markdown links.

### **Method 3: Local HTTP Server**
Simple HTTP server to test markdown files in browser.

### **Method 4: VSCode Live Preview**
Use VSCode's built-in markdown preview with live server.

---

## 🚀 Quick Start Guide

### **Option A: Docsify Server Setup**
```bash
# Install docsify globally
npm install -g docsify-cli

# Initialize docsify in the project root
cd /home/sri/Downloads/cloud-career-roadmap-zero-to-hero-job-ready
docsify init .

# Start the server
docsify serve . --port 3000

# Access at: http://localhost:3000
```

### **Option B: Markdown Link Checker**
```bash
# Install markdown link checker
npm install -g markdown-link-check

# Run link validation
cd /home/sri/Downloads/cloud-career-roadmap-zero-to-hero-job-ready
find . -name "*.md" -exec markdown-link-check {} \;
```

### **Option C: Python HTTP Server**
```bash
# Start simple HTTP server
cd /home/sri/Downloads/cloud-career-roadmap-zero-to-hero-job-ready
python3 -m http.server 8000

# Access at: http://localhost:8000
```

---

## 📋 Testing Checklist

### **Navigation Testing**
- [ ] All README.md links work correctly
- [ ] Cross-references between documents function
- [ ] Directory navigation is intuitive
- [ ] File paths are accurate and accessible

### **Content Validation**
- [ ] All referenced files exist
- [ ] Images and diagrams display correctly
- [ ] Code blocks render properly
- [ ] Tables format correctly

### **User Experience Testing**
- [ ] Documentation flows logically
- [ ] Links open in appropriate context
- [ ] Back navigation works smoothly
- [ ] Search functionality (if enabled)

---

## 🔧 Setup Instructions

See individual setup files:
- [docsify-setup.md](./docsify-setup.md) - Comprehensive documentation server
- [link-checker-setup.md](./link-checker-setup.md) - Automated link validation
- [http-server-setup.md](./http-server-setup.md) - Simple local testing
- [vscode-preview-setup.md](./vscode-preview-setup.md) - IDE-based testing

---

*Choose the method that best fits your workflow and testing needs.*