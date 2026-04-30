# 🚀 Microsoft Fabric — End-to-End Data Pipeline Project

A complete data pipeline built entirely within the **Microsoft Fabric** ecosystem — from raw source ingestion to business-ready Power BI visuals.

---

## 📐 Architecture Overview

```
┌─────────────────────────────────────────────────┐
│              DATA SOURCES                        │
│   Web API (HTTP)  │  GitHub  │  CSV Files        │
└──────────────────┬──────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────┐
│         🔵 BRONZE LAYER — Ingestion              │
│   Fabric Notebooks (PySpark)                     │
│   Lakehouse → Parquet Files                      │
│   ⏰ Scheduler: Daily 8 AM                       │
└──────────────────┬──────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────┐
│         🟡 SILVER LAYER — Transformation         │
│   Dataflow Gen2                                  │
│   Warehouse + Shortcut → SQL Database            │
└──────────────────┬──────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────┐
│         🟢 GOLD LAYER — Serving                  │
│   SQL Database                                   │
│   Semantic Model (BI Connectivity)               │
│   SQL — Insights & Analysis                      │
└──────────────────┬──────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────┐
│         📊 DISTRIBUTION — Power BI               │
│   Report → Published to Workspace → App          │
│   Stakeholder delivery via Power BI App          │
└─────────────────────────────────────────────────┘
```

---

## 🔵 Bronze Layer — Ingestion

| Item | Detail |
|---|---|
| Sources | Web API (HTTP), GitHub, CSV Files |
| Tool | Fabric Notebooks (PySpark) |
| Storage | Lakehouse |
| Format | Parquet files |
| Schedule | Daily trigger at 8 AM |

---

## 🟡 Silver Layer — Transformation

| Item | Detail |
|---|---|
| Tool | Dataflow Gen2 |
| Input | Lakehouse (Bronze) |
| Output | Warehouse |
| Shortcut | SQL Database |
| Operations | Business transformations & data cleaning |

---

## 🟢 Gold Layer — Serving

| Item | Detail |
|---|---|
| Storage | SQL Database |
| Analysis | SQL queries for insights & outcomes |
| Model | Semantic Model for BI connectivity |

---

## 📊 Distribution — Power BI

| Item | Detail |
|---|---|
| Mode 1 | Direct Query → Semantic Model |
| Mode 2 | Import Mode → Warehouse |
| Development | Power BI Desktop (DAX measures & visuals) |
| Publishing | Report → Workspace → App |
| Audience | Stakeholders via Power BI App |
| Refresh | Semantic Model scheduled daily at 8 AM |
| Subscriptions | Email delivery of reports & filtered logs |

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Ingestion | Fabric Notebooks (PySpark), Web API, GitHub, CSV |
| Storage | Lakehouse (Parquet), Warehouse, SQL Database |
| Transformation | Dataflow Gen2 |
| Modelling | Semantic Model, Shortcuts |
| Visualisation | Power BI Desktop, DAX |
| Distribution | Power BI Report, Power BI App |
| Automation | Fabric Scheduler, PBI Subscriptions |

---

## 🔧 What's Next

- [ ] Advanced pipelines with dynamic parameter entries
- [ ] Parameterized Dataflows
- [ ] Data Factory Pipelines
- [ ] Deeper exploration of Fabric toolset (Eventstream, Real-time Intelligence, Mirroring)

> This is a **medium-complexity** project. Planning to build more advanced and dynamic pipelines as Fabric has a lot more to offer! 🚀

---

## 🎯 Certification

**DP-600** — Microsoft Fabric Analytics Engineer *(In Progress ⏳)*

---

## 📬 Connect

If you're exploring Microsoft Fabric for your data platform, feel free to connect and share learnings!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](www.linkedin.com/in/harsha-venkata-sai-katta-a4478316b)

---

*Built with ❤️ using Microsoft Fabric*
