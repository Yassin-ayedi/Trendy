# Trendy Jobs & Tools – Azure Data Warehouse

## 📌 Project Overview
This project implements a **modern data warehouse on Azure Cloud** to analyze **trending jobs and tools** based on both **real-time popularity** and **historical market demand**.

The goal is to understand:
- What jobs and tools are **popular right now**
- How their **demand evolved over past years**
- How popularity aligns (or not) with market demand

---

## 🧠 Data Sources
The warehouse ingests data from multiple sources:

### Real-time / Near real-time popularity
- **Reddit**
- **Stack Overflow**
- (Other social / community platforms can be added later)

These sources are used to measure **popularity** based on activity and mentions.

### Historical demand
- CSV databases containing **past years market data**
- Used to measure **job and tool demand over time**

---

## 📊 Data Model
The warehouse is built around **two main fact tables**:
- **Popularity fact** → real-time / near real-time metrics
- **Demand fact** → historical market demand

This allows comparison between:
- *What is trendy now*
- *What is actually demanded in the market*

---

## ☁️ Cloud Architecture
The solution is built using a **modern Azure data architecture** with **minimal infrastructure requirements**:

- **Azure Data Lake Storage Gen2**
- **Azure Synapse Analytics**
  - PySpark notebooks
  - SQL scripts
  - Pipelines

### Data Lake Zones
The Data Lake is organized into three containers following best practices:

- **Bronze** → raw, unprocessed data
- **Silver** → cleaned and transformed data
- **Gold** → analytics-ready data (facts & dimensions)

---

## 📁 Repository Structure
.
├── extract/
│ └── Local extraction scripts (VS Code)
│ - Fetch data from external sources
│ - Upload raw data directly into the Bronze layer
│ - Uses Azure extensions & credentials
│
├── transform/
│ └── Azure Synapse PySpark notebooks
│ - Data cleaning
│ - Data transformation
│ - Bronze → Silver → Gold
│
├── load(sql)/
│ └── SQL scripts & notebooks (Azure Synapse)
│ - Fact table loading
│ - Aggregations
│ - Warehouse modeling
│
├── synapse_publish/
│ └── Auto-generated Azure Synapse artifacts
│ - Published notebooks
│ - Pipelines
│ - Queries
│ - Workspace configuration
│
└── README.md

---

## ⚙️ Configuration (to be added)
Configuration files (connections, secrets, parameters) will be added later.

Planned:
- Environment-specific configuration
- Secure credentials (Key Vault)
- Parameterized paths and resources

> 📌 **Placeholder**: Configuration documentation will be added here.

---

## 🚀 How the Pipeline Works (High Level)
1. **Extract**
   - Run locally using VS Code
   - Fetch data from Reddit, Stack Overflow, and historical CSVs
   - Store raw data in **Bronze**

2. **Transform**
   - PySpark notebooks in Azure Synapse
   - Clean and enrich data
   - Move data to **Silver** and **Gold**

3. **Load**
   - SQL scripts build facts and analytics tables
   - Support reporting and trend analysis

---

## 🛠 Technologies Used
- Azure Data Lake Storage Gen2
- Azure Synapse Analytics
- PySpark
- SQL
- Python
- GitHub

---

## 📌 Notes
- Raw data is **not versioned** in GitHub
- GitHub contains **code only**
- Data lives exclusively in the Data Lake

---






The GitHub repository is organized as follows:

