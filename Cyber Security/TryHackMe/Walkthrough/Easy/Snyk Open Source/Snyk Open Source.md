![](images/Pasted%20image%2020240622003938.png)
Introduction

**Learning Objectives**

- Recognize open-source security risks and comprehend their implications on contemporary software projects
- Operate Snyk effectively to detect vulnerabilities
- Evaluate and classify identified vulnerabilities
- Apply appropriate remediation measures

**Understanding Open Source Security Risks**

Open-source software components have revolutionized the world of software development, enabling developers to build complex systems faster than ever before. 

What are some open source security risks

**Large attack surface**

Modern applications often rely on hundreds, if not thousands, of open-source libraries and frameworks. Managing the security of so many disparate components requires significant effort and expertise. 

**Rapid release cycles**

The rapid pace of innovation in open-source communities frequently leads to updates, bug fixes, and feature enhancements. 

**Transitive dependencies**

Many open-source libraries depend on other libraries, forming intricate interdependencies. When left unmanaged, transitive dependencies can harbor unknown vulnerabilities propagating silently throughout an entire system. 

**Limited visibility**

Tracking open-source usage and associated risks become more manageable with proper instrumentation and visibility. 

1. Which JSON-formatted manifest file serves as the central hub for Node.js projects, listing metadata, scripts, and dependency declarations?

- package.json

2. How many dependencies do we have for this new feature?

- 5

3. Which term describes indirect package dependencies formed through shared prerequisites, possibly concealing vulnerabilities and demanding cautious assessment?

- transitive dependencies

---


**Getting Started with Snyk Open Source**

1. What single authentication mechanism allows users to transition smoothly amongst various linked platforms and services?

- single sign-on

---

**Diving Deeper Into Vulnerabilities**

After analyzing the scan Jessica find severity level(high,medium,low) which allows her to prioritise critical issues first.

1. What is prototype Pollution?

- When creating a new object, JavaScript uses the prototype chain to look for properties and methods. The prototype chain starts with the **Object.prototype** and continues upward until it finds the property or method requested.

Example where prototype pollution might occur:

**Unpredictable behaviour:** Modified prototypes may cause functions to behave differently than intended, leading to bugs and crashes.

**Data manipulation:** Malicious actors can use prototype pollution to modify data stored in arrays or other structures, resulting in incorrect outputs or even data loss.

**Information disclosure:** Attackers can exploit prototype pollution to gain access to sensitive information stored in affected variables or objects.

1. What is the version of the vulnerable lodash package?

- 2.4.2

2. Which vulnerability allows an attacker to modify an Object?

- prototype pollution

**Remediating Vulnerabilities**

What is Vulnerability Triage?

Triage evaluates and categorizes vulnerabilities according to their severity, impact, and likelihood of exploitation. 

**Explains a few best practices for vulnerability triage:**

- Prioritise based on CVSS scores: The Common Vulnerability Scoring System (CVSS) provides standardised scoring metrics for assessing the severity of vulnerabilities. Teams should use CVSS scores to determine the relative importance of different vulnerabilities. 

- Consider the business context: Not every vulnerability poses an equal risk to the organisation. Factors such as the sensitivity of the data involved, regulatory compliance obligations, and the potential financial impact of a breach should inform triage decisions.

- Evaluate exploitability: Some vulnerabilities are more easily exploited than others. Teams should evaluate the ease with which an attacker could leverage a given vulnerability to mount an effective attack.

1. What does CVSS stand for?

- common vulnerability scoring system

2. Should the development team bulk fix all the vulnerabilities found in this new feature? (y/n)

- n

**Automating the Process Through CI/CD Pipelines**

1. How does CircleCI help streamline pipeline configuration and standardisation?
- orb

2. What file defines the GitHub Actions workflow configuration that enables automation and customised sequences for building, testing, and deploying?
- yaml

**Implementing Continuous Monitoring**

1. Which collaborative DevOps practice combines real-time communication channels, automation, and operational agility?

- chatops

