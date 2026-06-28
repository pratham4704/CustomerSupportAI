# AI-Powered Customer Support Automation System using LangGraph

## Project Overview

This project implements an AI-powered Customer Support Automation System for **ABC Technologies**, a SaaS company providing cloud-based business management software.

The system automates customer support by classifying customer queries, routing them to specialized support agents, retrieving relevant information using Retrieval-Augmented Generation (RAG), maintaining conversation history using SQLite, and escalating sensitive requests to a human supervisor before generating the final response.

The project is built using **LangGraph**, **Google Gemini API**, **LangChain**, **FAISS**, **SQLite**, and **Streamlit**.

---

# Features

* AI-powered customer support automation
* Intent classification
* Department-based routing
* Retrieval-Augmented Generation (RAG)
* FAISS vector database
* PDF knowledge base
* SQLite conversation memory
* Human-in-the-loop approval
* Supervisor response validation
* Streamlit user interface

---

# Support Departments

| Department        | Handles                                            |
| ----------------- | -------------------------------------------------- |
| Sales             | Product information, pricing, subscription plans   |
| Technical Support | Installation, login, crashes, configuration        |
| Billing           | Refunds, invoices, payments                        |
| Account           | Password reset, profile update, account activation |

---

# Technology Stack

* Python 3.12+
* LangGraph
* LangChain
* Google Gemini API (`google-genai`)
* FAISS
* HuggingFace Embeddings
* SQLite
* Streamlit
* PyPDF

---

# Project Structure

```
CustomerSupportAI/

│
├── app.py
├── graph.py
├── nodes.py
├── router.py
├── approval.py
├── supervisor.py
├── rag.py
├── memory.py
├── config.py
├── state.py
├── requirements.txt
├── README.md
├── .env
│
├── knowledge_base/
│      company_policy.pdf
│      pricing_guide.pdf
│      technical_manual.pdf
│      faq.pdf
│
├── vectorstore/
│
└── database/
       memory.db
```

---

# Installation

## Clone the repository

```
git clone <repository-url>

cd CustomerSupportAI
```

---

## Create Virtual Environment (Optional)

Windows

```
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```
pip install -r requirements.txt
```

---

# Configure Gemini API

Create a `.env` file inside the project folder.

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

# Build the Vector Database

Run:

```
python build_vector.py
```

This creates the FAISS vector database from the PDF documents inside the `knowledge_base` folder.

---

# Run the Application

```
streamlit run app.py
```

The application will open automatically in your browser.

Default URL:

```
http://localhost:8501
```

---

# Workflow

1. Customer enters name and query.
2. LangGraph classifies the intent.
3. Query is routed to the correct department.
4. Relevant company documents are retrieved using RAG.
5. High-risk requests are checked for approval.
6. Supervisor reviews the generated response.
7. Conversation is stored in SQLite.
8. Final response is displayed to the customer.

---

# Human-in-the-Loop Requests

The following requests require manual approval:

* Refund Request
* Subscription Cancellation
* Account Closure
* Compensation Request
* Escalation to Management

---

# Knowledge Base

The system retrieves information from the following documents:

* Company Policy
* Pricing Guide
* Technical Manual
* FAQ Document

---

# Memory

SQLite stores previous customer conversations.

Example:

Customer:

"My name is David. I have a billing issue."

Later:

"What was my previous support issue?"

The system retrieves the previous interaction from SQLite memory.

---

# Sample Queries

### Sales

What are the pricing plans available?

---

### Technical

My application crashes whenever I upload a file.

---

### Billing

I need a refund for my annual subscription.

---

### Account

I forgot my password.

---

### Memory

What was my previous support issue?

---

# Future Improvements

* Multi-language support
* Voice-based customer interaction
* Email integration
* CRM integration
* Sentiment analysis
* Automatic ticket generation
* Live human approval dashboard

---

# Developed Using

* LangGraph
* Google Gemini
* LangChain
* Streamlit
* SQLite
* FAISS
* Python

---

# Author

AI-Powered Customer Support Automation System

Academic Project

![query1](../screenshots/query1.png)
![query2](../screenshots/query2.png)
![query3](../screenshots/query3.png)
![query4](../screenshots/query4.png)
![query5](../screenshots/query5.png)


##Workflow diagram
                         +----------------------+
                         |   Customer Query     |
                         +----------+-----------+
                                    |
                                    v
                     +-----------------------------+
                     |   Intent Classification     |
                     +--------------+--------------+
                                    |
      +-----------------------------+-----------------------------+
      |               |               |               |           |
      v               v               v               v           v
+-------------+ +-------------+ +-------------+ +-------------+ +-------------+
| Sales Agent | | Technical   | | Billing     | | Account     | | Memory      |
|             | | Support     | | Support     | | Support     | | Recall      |
+------+------+ +------+------+ +------+------+ +------+------+ +------+------+
       |               |               |               |               |
       +---------------+---------------+---------------+               |
                       |                                               |
                       v                                               |
              +-------------------------+                             |
              |   RAG Document Search   |                             |
              | (FAISS + Knowledge Base)|                             |
              +------------+------------+                             |
                           |                                          |
                           v                                          |
              +-------------------------+                             |
              | Human Approval Required?|<----------------------------+
              +------------+------------+
                           |
               +-----------+-----------+
               |                       |
              Yes                     No
               |                       |
               v                       v
     +-------------------+    +-------------------+
     | Human Supervisor  |    | Supervisor Agent  |
     +---------+---------+    +---------+---------+
               |                        |
               +-----------+------------+
                           |
                           v
                 +-----------------------+
                 | Save to SQLite Memory |
                 +-----------+-----------+
                             |
                             v
                  +----------------------+
                  | Final Customer Reply |
                  +----------------------+