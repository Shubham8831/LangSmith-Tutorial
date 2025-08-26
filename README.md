# **LangSmith: Why Do We Need It? 🤔**

## The Problem with LLM Applications

Large Language Models (LLMs) are powerful but come with unique challenges that traditional debugging tools can't handle.

## WHY LangSmith? 

### The Core Issues:
1. **Non-Deterministic Behavior** - Same input → Different outputs
2. **Black Box Nature** - No clear explanation of what's happening inside
3. **No Traditional Errors** - Problems occur silently without crashes

---

## Real-World Problems

### 🔍 Example 1: AI Job Assistant
**What it does:** Finds relevant jobs and crafts cover letters with your resume

**The Problem:**
- Normal execution time: **1 minute**
- Suddenly shoots up to: **10 minutes**
- **Why?** Complex workflow with multiple components - impossible to identify the slow component

### 💰 Example 2: Research Assistant Agent
**What it does:** Provides detailed research answers

**The Problem:**
- Normal cost per query: **₹1**
- Suddenly increases to: **₹20**
- **Why?** No clear way to track which part of the pipeline is consuming more tokens

### 🤖 Example 3: RAG Company Chatbot
**What it does:** Answers questions about company policies and leave

**The Problem:**
- Chatbot starts **hallucinating** - giving false information
- **Two possible causes:**
  1. Retriever not finding relevant documents
  2. LLM generating poor answers from good documents
- **Why?** Can't determine which component is failing

---

## The Challenge

Traditional debugging doesn't work because:

- ❌ **No stack traces** when things go wrong
- ❌ **No clear error messages** for quality issues
- ❌ **Can't see inside** the LLM decision process
- ❌ **Hard to track** performance across complex workflows

## The Solution: LangSmith

LangSmith provides **visibility and debugging tools** specifically designed for LLM applications, helping you:

- 🔍 **Monitor** each step of your LLM workflow
- 📊 **Track** performance, costs, and quality metrics
- 🐛 **Debug** issues in complex AI pipelines
- 📈 **Optimize** your applications based on real data

---

## What is Observability? 👀

**Observability** = The ability to see what's happening inside your system

Think of it like having X-ray vision for your AI application:
- **Trace every step** from start to finish
- **Understand internal state** by looking at external outputs (logs, metrics, traces)
- **Diagnose issues** and improve performance by analyzing system data

### Why Traditional Monitoring Fails for AI?
- Regular apps: Clear error messages, predictable flows
- AI apps: Silent failures, complex multi-step workflows, unpredictable outputs

---

## LangSmith: Your AI Observability Solution 🔬

**LangSmith** is a unified platform for debugging, testing, and monitoring AI applications.

### What Does LangSmith Trace?
Every execution captures:
- 📥 **Input & Output** - What goes in, what comes out
- 🔄 **All Intermediate Steps** - Every component in your workflow
- ⏱️ **Latency** - How long each step takes
- 🪙 **Token Usage** - Exact tokens consumed
- 💰 **Cost** - Real money spent per execution
- ❌ **Errors** - When and where things break
- 🏷️ **Tags & Metadata** - Custom labels for organization
- 💬 **Feedback** - User ratings and comments

---

## Core LangSmith Concepts 🧱

### 📁 **Project**
The complete AI workflow/application
- Example: User → Prompt → LLM → Parser

### 🔗 **Trace** 
One single execution of your entire project
- When a user asks one question = 1 trace

### ⚙️ **Run**
Execution of individual components within a trace
- **Prompt Run**: Processing the user input
- **LLM Run**: Getting response from the language model  
- **Parser Run**: Formatting the final output

### Example Breakdown:
```
Project: AI Job Assistant
├── Trace 1: "Find me Python jobs"
│   ├── Run 1: Process user query (Prompt)
│   ├── Run 2: Search jobs database (LLM)
│   └── Run 3: Format results (Parser)
└── Trace 2: "Write cover letter"
    ├── Run 1: Analyze job requirements (Prompt)
    ├── Run 2: Generate letter (LLM)
    └── Run 3: Format output (Parser)
```

**Result:** Complete visibility into every step of your AI application! 🎯

---

## 🚀 Getting Started with LangSmith

### Step 1: Clone the Tutorial Repository
```bash
git clone https://github.com/Shubham8831/LangSmith-Tutorial
cd LangSmith-Tutorial
```

### Step 2: Environment Setup (.env file)
Create a `.env` file in your project root with these keys:

```env
# Groq API Key (for LLM calls)
GROQ_API_KEY=your_groq_api_key_here
LANGCHAIN_API_KEY=langsmith_api_key_here

# LangSmith Configuration
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_PROJECT=your_project_name
```

### Step 3: Run Your First Example
```bash
python 1_simple_llm_call.py
```

### Step 4: View Results
1. Open [LangSmith Website](https://smith.langchain.com/)
2. Go to your project dashboard
3. See detailed traces, costs, and performance metrics!

---

## 🎛️ Advanced Configuration

### Setting Project Name in Code
```python
import os
os.environ['LANGCHAIN_PROJECT'] = "My AI Assistant"
```

### Adding Tags, Metadata & Custom Names
Use the `config` parameter when invoking your chain:

```python
# Example configuration
config = {
    "run_name": "Custom Run Name",
    "tags": ["production", "user-query", "v1.2"],
    "metadata": {
        "user_id": "user_123",
        "session_id": "session_456",
        "version": "1.2.0",
        "environment": "production"
    }
}

# Use config when invoking
response = chain.invoke(
    {"question": "What is LangSmith?"},
    config=config
)
```

### Trace-Level Configuration
```python
# For entire trace
config = {
    "tags": ["important-query"],
    "metadata": {"priority": "high"}
}
```

### Run-Level Configuration
```python
# For individual component runs
llm_config = {
    "run_name": "GPT-4 Generation",
    "tags": ["llm-call"],
    "metadata": {"model": "gpt-4", "temperature": 0.7}
}
```

**Result:** Organized, searchable, and well-labeled traces for easy debugging! 🏷️

---

### 📚 RAG Implementation & Tracing Evolution

---

### 🔍 **3_rag_v1.py** - Initial RAG Implementation
**Problem:** Only chains/runnables were being traced
- ❌ Document loading not traced
- ❌ Text chunking not traced  
- ❌ Vector database creation not traced
- ❌ Vector store recreated on every run (inefficient)

**What we saw:** Incomplete visibility into the RAG pipeline

---

### 🛠️ **3_rag_v2.py** - Adding @traceable Decorator
**Solution:** Use `@traceable` decorator for non-runnable functions

```python
from langsmith import traceable

@traceable(name="Document Loader", tags=["preprocessing"])
def load_documents():
    # Document loading logic
    pass

@traceable(name="Text Splitter", tags=["preprocessing"])  
def split_documents():
    # Text chunking logic
    pass

@traceable(name="Vector Store Creation", tags=["preprocessing"])
def create_vector_store():
    # Vector database creation
    pass
```

**New Problem:** Individual functions traced separately, not as unified pipeline

---

### 🔗 **3_rag_v3.py** - Pipeline Integration
**Solution:** Combine all components into a cohesive pipeline
- ✅ All functions traced with proper hierarchy
- ✅ Unified pipeline view in LangSmith
- ✅ Better organization with tags and metadata
- ❌ Still recreating vector store every run

**Result:** Complete pipeline visibility but performance issues remain

---

### ⚡ **3_rag_v4.py** - Optimized Final Version
**Solution:** Persistent vector store + complete tracing
- ✅ Vector store created once, reused across runs
- ✅ All components properly traced
- ✅ Efficient pipeline execution
- ✅ Production-ready implementation

### Key Decorator Features:
```python
@traceable(
    name="Custom Function Name",
    tags=["preprocessing", "rag"],
    metadata={"version": "1.0", "type": "loader"}
)
def my_function():
    pass
```

### Evolution Summary:
| Version | Chains Traced | Functions Traced | Pipeline Unity | Efficiency |
|---------|---------------|------------------|----------------|------------|
| v1      | ✅            | ❌               | ❌             | ❌         |
| v2      | ✅            | ✅               | ❌             | ❌         |
| v3      | ✅            | ✅               | ✅             | ❌         |
| v4      | ✅            | ✅               | ✅             | ✅         |

**Final Result:** Production-ready RAG with complete observability! 🎯

---
