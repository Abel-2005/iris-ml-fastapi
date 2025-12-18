Machine Learning Model Deployment Using FastAPI with Git Version Control

1\. Introduction



This project demonstrates the complete lifecycle of a machine learning application, starting from model training to deployment as a web service. The objective of the project is to integrate concepts from Machine Learning, DevOps, and Version Control Systems. A classification model is trained using the Iris dataset and deployed as a RESTful API using FastAPI. The entire development process is managed using Git and GitHub, following proper branching, merging, and conflict resolution practices.



2\. Project Objectives



The main objectives of this project are:



To train a machine learning model using a standard dataset.



To deploy the trained model as a REST API using FastAPI.



To demonstrate Git version control concepts such as branching and merging.



To create and resolve merge conflicts.



To host the project on a remote GitHub repository.



3\. Technologies Used



Python



Scikit-learn



FastAPI



Uvicorn



Git



GitHub



4\. Dataset Description



The project uses the Iris dataset, which is a well-known dataset in machine learning. It contains measurements of iris flowers, including:



Sepal length



Sepal width



Petal length



Petal width



The target variable represents the species of the flower. The dataset is used to train a Logistic Regression classification model.



5\. Project Structure

iris-ml-fastapi/

├── predict.py

├── train\_model.py

├── model.pkl

├── README.md

├── requirements.txt

├── data/

├── experiments/





train\_model.py: Trains the machine learning model and saves it.



predict.py: FastAPI application that loads the model and serves predictions.



model.pkl: Serialized trained machine learning model.



requirements.txt: List of required Python dependencies.



README.md: Project documentation.



6\. Model Training



The model is trained using Logistic Regression from the Scikit-learn library. The Iris dataset is split into training and testing sets. After training, the model is serialized using Python’s pickle module and saved as model.pkl. This file is later loaded by the FastAPI application to generate predictions.



7\. FastAPI Deployment



FastAPI is used to deploy the trained machine learning model as a REST API. The application provides:



A root endpoint (/) to verify that the API is running.



A prediction endpoint (/predict) that accepts feature values as JSON input and returns the predicted class.



FastAPI automatically generates interactive API documentation using Swagger UI, which can be accessed through the /docs endpoint.



8\. Git Version Control Workflow



This project follows a structured Git workflow to demonstrate version control concepts.



8.1 Branches Used



master/main: Main stable branch.



feature-model: Used for feature-related development.



bugfix-api: Used to fix issues related to the API.



experiment-model: Used to experiment with model configuration changes.



8.2 Merging and Conflict Resolution



Each branch was merged into the main branch after committing changes. During the merge of the feature branch, a merge conflict occurred involving both source code and a binary file (model.pkl). The conflict was manually resolved by selecting the correct version of files and committing the resolution. This demonstrates practical handling of merge conflicts in real-world scenarios.



9\. Remote GitHub Repository



A remote GitHub repository was created to host the project. The local repository was connected using the git remote add origin command, and all commits and branches were pushed to GitHub. This enables centralized version control and serves as a backup and collaboration platform.



10\. How to Run the Project



Install dependencies:



pip install -r requirements.txt





Train the model:



python train\_model.py





Run the FastAPI application:



python -m uvicorn predict:app





Open the browser and visit:



http://127.0.0.1:8000



http://127.0.0.1:8000/docs



11\. Results



The trained model successfully predicts the class of iris flowers based on input features. The FastAPI service responds with predictions in real time, demonstrating the successful deployment of a machine learning model as a web API.

12\. Conclusion



This project successfully integrates machine learning with DevOps practices using Git and GitHub. It provides hands-on experience with model training, API deployment, version control workflows, branching strategies, and merge conflict resolution. The project reflects a real-world development scenario and strengthens practical understanding of end-to-end machine learning system development.



\## 📁 Project Structure



\### Project Directory Structure

!\[Project Directory Structure](screenshots/project-directory-structure.png)



---



\## 🔧 Git Setup



\### Git Initial Setup

!\[Git Initial Setup](screenshots/git-initial-setup.png)



\### Branches Created

!\[Branches Created](screenshots/branches-created.png)



\### Git Status

!\[Git Status](screenshots/git-status.png)



---



\## ⚠️ Merge Conflict



\### Merge Conflict

!\[Merge Conflict](screenshots/merge-conflict.png)



\### Merge Conflict Resolved

!\[Merge Conflict Resolved](screenshots/merge-conflict-resolved.png)



---



\## 🚀 API \& FastAPI



\### API Running

!\[API Running](screenshots/api-running.png)



\### FastAPI Swagger UI

!\[FastAPI Swagger UI](screenshots/fastapi-swagger-ui.png)



\### Uvicorn Server Running

!\[Uvicorn Server](screenshots/uvicorn-server-running.png)



---



\## 🐙 GitHub Repository



\### GitHub Repository

!\[GitHub Repository](screenshots/github-repository.png)



\### Remote Origin

!\[Git Remote Origin](screenshots/git-remote-origin.png)


## Challenges Faced

- Understanding Git branching and managing multiple branches simultaneously.
- Resolving merge conflicts while modifying the same file in different branches.
- Debugging errors while integrating the machine learning model with the FastAPI application.
- Handling large dataset uploads and managing repository structure efficiently.
- Ensuring correct input format for API predictions.




13\. Future Scope



Deployment using Docker and cloud platforms.



Addition of authentication to the API.



Integration of CI/CD pipelines.



Support for multiple machine learning models.



14\. References



Scikit-learn Documentation – https://scikit-learn.org



FastAPI Documentation – https://fastapi.tiangolo.com



Git Documentation – https://git-scm.com



GitHub Documentation – https://docs.github.com

