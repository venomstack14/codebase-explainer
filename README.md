#  Codebase Explainer

A lightweight web tool to analyze, explore, and query any Python codebase.  
Built to help developers and recruiters quickly understand the structure of a project.

---

##  Features

- Parse any Python project to extract:
  - Functions
  - Classes
  - Imports
- Provide a **project overview** with summary statistics
- Show **file-level insights**
- Build a **dependency graph** (file → imports)
- Ask natural questions about your codebase (e.g., “Which files define Flask routes?”)
- Clean dark-themed UI for easy navigation

---

##  Tech Stack

- **Frontend:** HTML, CSS, JavaScript (vanilla)  
- **Backend:** Python, Flask  
- **Code Parsing:** `ast` module  
- **Graph Analysis:** `networkx`  

---

## 🚀 Installation & Usage

1. **Clone the repository**

```bash
git clone https://github.com/venomstack14/codebase-explainer.git
cd codebase-explainer
