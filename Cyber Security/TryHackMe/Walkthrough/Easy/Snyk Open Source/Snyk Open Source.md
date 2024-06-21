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

