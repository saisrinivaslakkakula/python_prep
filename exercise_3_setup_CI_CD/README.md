# Exercise 3 – CI/CD with Jenkins & Docker

## 🎯 Goal
Practice setting up a **full CI/CD pipeline** for a simple Python application (Calculator), using **Jenkins** and **Docker**.  
This mimics how production pipelines validate and deploy native apps or firmware.  

---

## 🛠️ What This Exercise Covers
1. **CI (Continuous Integration)**  
   - Run Python unit tests with `pytest`.  
   - Ensure code changes don’t break functionality.  

2. **CD (Continuous Delivery/Deployment)**  
   - Package the Calculator app as a **Docker image** (simulating deployable artifact).  
   - Run **system tests** against the built container (like firmware validation).  
   - Archive logs & results for traceability.  

3. **Automation & Triggers**  
   - Use Jenkins declarative pipeline (`Jenkinsfile`).  
   - Trigger builds automatically via **GitHub Webhooks**.  
   - View pipeline visually using **Blue Ocean plugin**.  

---

## 📂 Repo Structure
```
exercise_2/ # Source: Calculator app
exercise_2b/ # Test runner mini-framework
system_tests.sh # CLI-based system tests
Dockerfile # Containerizes the Calculator app
Jenkinsfile # CI/CD pipeline definition
```


---

## ⚙️ Pipeline Flow
Stages defined in `Jenkinsfile`:

1. **Checkout** – Pull code from GitHub.  
2. **Setup Python & Run Unit Tests** – Run `pytest` on Calculator module.  
3. **Build Docker Image** – Build artifact image: `calc-app:<build_number>`.  
4. **System Tests** – Run `system_tests.sh` against the Dockerized app.  
5. **Archive Results** – Save logs and test results as Jenkins artifacts.  

---

## 🖥️ System Tests
System tests validate Calculator as a **CLI binary** (not a server). Example:

```bash
docker run --rm calc-app:10 + 1 2   # → 3
docker run --rm calc-app:10 - 1 2   # → -1
```

---

## 🔗 GitHub Webhook

- Configured a **webhook** (/github-webhook/) so push events auto-trigger builds.

- Validated via ngrok for local Jenkins.
