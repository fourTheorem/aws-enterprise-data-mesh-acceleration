# What is a Data Mesh

**A data mesh is an architectural framework that solves advanced data security challenges through distributed, decentralised ownership.**  

Organisations have multiple data sources from different lines of business that must be integrated for analytics. A data mesh architecture effectively unites disparate data sources and links them together through centrally managed data sharing and governance guidelines. Business functions can control how shared data is accessed, who accesses it, and in what formats it’s accessed. A data mesh adds complexities to architecture but also brings efficiency by improving data access, security, and scalability.


## What challenges does a data mesh solve?
Historically, organisations have often utilised a central team of data engineers for managing data. This model has worked well in the past when there was a limited number of data sources and destinations, e.g. extracting data nightly from an operational system into a data warehouse. However as data volumes and the number of data sources have increased, organisations have struggled to scale their data pipelines because of the following reasons:
1. **Siloed data team:** The central data team consists of specialised data scientists and engineers with limited business and domain knowledge. Despite this, they are responsible for providing data for a wide range of operational and analytical needs, often without fully understanding the rationale behind these needs.
2. **Slow responsiveness to change:** Data engineers typically implement pipelines that ingest the data and transform it over several steps before storing it in a central data lake. Any requested changes require modifications to the entire pipeline. The central team has to make these changes while managing conflicting priorities and with limited business domain knowledge.
3. **Reduced accuracy:** Business units are disconnected from the data consumers and the central data teams. As a result, they lack the incentive to provide meaningful, correct, and useful data.

