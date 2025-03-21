# 👟 **Local Async Data Engineer Chatbot with Mistral**

This is a **local, asynchronous chatbot** designed to act as a data engineering assistant. It's built using **Panel** for the user interface and powered by the **Mistral** language model via **Ollama**, ensuring all processing occurs locally. This tool allows you to interact with a data engineering expert through natural language prompts, receiving code suggestions, explanations, and assistance directly within the chat interface.

🔑 **Key Benefits:**

-   **Local Execution:** All LLM processing happens locally using Ollama, ensuring data privacy and no reliance on external APIs.
-   **Asynchronous Processing:** Utilizes `asyncio` for non-blocking operations, providing a responsive and smooth user experience.
-   **Mistral Power:** Leverages the Mistral language model for high-quality and contextually relevant responses.
-   **Data Engineering Focus:** Pre-configured with a system context to act as a dedicated data engineering assistant.
-   **Interactive Chat Interface:** Built with Panel's `ChatInterface` for a user-friendly and intuitive experience.

📎 This tool is particularly useful for **rapid prototyping, learning, and developing data engineering workflows** in a secure and offline environment.

**Screenshots:**

![Chat Interface](images/[mistral_bot.png])

---

## 🎛 **Setup Instructions**

### 1. **Install Ollama**
Download and install **Ollama** to run local LLMs:  
[Ollama Installation](https://ollama.com/download)
Make sure you have installed minstral library
(see ollama documentation)

### 2. **Clone the Repository**
```bash
git clone https://github.com/Ethanlchandler/local_panel_mistral_SQL_chatbot
```

### 3. **Create and Activate a Virtual Environment**
On Linux/macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 5. **Run the Application**
```bash
panel serve main.py
```

## 🍴 **Possible Uses**

This tool can be extended or forked to suit various **data engineering assistance** needs:

-   **Code Generation:**
    Generate data engineering code snippets (e.g., SQL, Python data pipelines, Spark scripts).
-   **Debugging Assistance:**
    Get help debugging data-related code and pipelines, including error analysis and troubleshooting.
-   **Concept Explanation:**
    Understand complex data engineering concepts (e.g., data warehousing, ETL, data modeling) through natural language interaction.
-   **Workflow Planning:**
    Plan and design data engineering workflows and architectures, including data flow diagrams and system design.
-   **Learning Resource:**
    Use it as a personal learning tool for data engineering topics, providing explanations and examples.
-   **Data Transformation Guidance:**
    Obtain assistance with data transformation tasks, like data cleaning, aggregation and feature engineering.
-   **Infrastructure as Code (IaC) Support:**
    Generate and understand IaC code related to data platforms (Terraform, CloudFormation, etc.)
-   **Data Governance Consultation:**
    Receive assistance with data governance best practices, data quality checks, and metadata management.
-   **Interview Preparation:**
    Practice for data engineering interviews by asking technical questions and receiving detailed answers.
-   **Quick Script Prototyping:**
    Rapidly generate simple data manipulation scripts for quick data exploration and analysis.

---

## 🗿 **Tech Stack**
- **Language Model:** Mistral via Ollama  
- **Framework:** Panel 
- **Languages:** Python    

---

## 🤷🏻‍♂️ **Author**
**Ethan Chandler**  
- [GitHub](https://github.com/Ethanlchandler)  
- [LinkedIn](https://www.linkedin.com/in/ethan-chandler)  

---

Let me know if you want further modifications, additional sections, or more details!
