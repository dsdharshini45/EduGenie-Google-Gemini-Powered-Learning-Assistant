                                EduGenie: Google Gemini Powered Learning Assistant

PHASE 1 — BRAINSTORMING & IDEATION:

1. Project Title
EduGenie: Google Gemini Powered Learning Assistant

2. Introduction
EduGenie is a lightweight AI-powered educational assistant designed to help students learn topics in a simple, interactive, and personalized way.
The system uses Google Gemini to provide answers, explain difficult topics, generate quizzes, summarize text, and recommend learning paths. The project uses a FastAPI backend with a simple HTML and CSS frontend.

3. Problem Statement
Students often need help understanding difficult topics, finding quick answers, preparing for quizzes, summarizing lengthy study materials, and deciding what to learn next.
Traditional learning resources may require students to search through multiple websites, books, or videos. This can take time and may not provide explanations according to the student's learning level.
Therefore, there is a need for a simple AI-based learning assistant that can provide educational support through a single interface.

5. Proposed Idea
The proposed solution is EduGenie, an AI-powered learning assistant that uses Google Gemini to support students in their learning activities.
The system provides the following major features:
Question and Answer
Topic Explanation
Quiz Generation
Text Summarization
Learning Path Recommendation
These features are based on the project's defined scenarios and functionality.

5. Need for the Project
EduGenie is designed to:
Help students understand difficult concepts.
Provide quick answers to questions.
Make learning more interactive.
Generate practice questions.
Summarize lengthy study material.
Provide a structured learning path.
Reduce the time required to search for educational information.

6. Target Users
The main target users are:
School students
College students
Beginners learning technical subjects
Self-learners
Students preparing for examinations

7. Main Objectives
The objectives of EduGenie are:
To develop an AI-powered educational assistant.
To provide simple explanations of complex topics.
To answer student questions using Google Gemini.
To generate multiple-choice quizzes.
To summarize educational content.
To recommend learning paths from beginner to advanced level.
To provide all these features through a simple web interface.

9. Key Features
Question & Answer
Students can enter a question and receive an AI-generated answer.
Explain
Students can enter a topic and receive a simple definition, explanation, and example.
Quiz
The system generates three multiple-choice questions with four options for each question.
Summarize
Students can enter lengthy text and receive a shorter summary containing the important points.
Learning Path
The system creates a learning path from beginner to advanced level, including difficulty levels, descriptions, and suggested resources.

9. Expected Benefits
EduGenie can:
Make learning easier.
Save students' time.
Provide instant educational assistance.
Encourage self-learning.
Support personalized learning.
Make practice more interactive.

11. Conclusion
EduGenie aims to provide a simple and useful AI-powered learning environment where students can ask questions, understand concepts, practice quizzes, summarize content, and plan their learning journey.

PHASE 2 — REQUIREMENT ANALYSIS:
1. Project Title
EduGenie: Google Gemini Powered Learning Assistant

2. Functional Requirements
The system should provide the following functions.

FR1 — Question Answering
The system should accept a student's question and generate an appropriate answer using Google Gemini.
FR2 — Topic Explanation
The system should accept a topic and provide:
Simple definition
Clear explanation
Simple example
FR3 — Quiz Generation
The system should:
Accept a topic.
Generate three questions.
Provide four options for each question.
Provide the correct answer.
Allow the student to check their answers.
FR4 — Text Summarization
The system should accept text and generate a concise summary containing the main points.
FR5 — Learning Path Recommendation
The system should accept a topic and generate a learning path from beginner to advanced level.

The learning path should include:
Topic
Difficulty
Description
Suggested resources
The project's original design specifies these five major backend capabilities.

3. Non-Functional Requirements
Performance
The application should respond to user requests within a reasonable amount of time.

Usability
The interface should be simple and easy for students to understand.

Reliability
The system should handle errors without completely stopping the application.

Maintainability
The code should be divided into separate modules so that individual features can be modified easily.

Scalability
Additional educational features can be added in the future.

Security
The Gemini API key should not be hard-coded or publicly uploaded to GitHub.

4. Hardware Requirements
Minimum requirements:
 Computer/Laptop
 Minimum 4 GB RAM
 Internet connection
 Keyboard and mouse
 Modern web browser

6. Software Requirements
The project uses:
Python 3.10 or higher
FastAPI
Uvicorn
Jinja2
HTML
CSS
Google Gemini API
Google GenAI Python SDK
Visual Studio Code

The project's documentation specifies Python 3.10+, FastAPI, HTML/CSS, Gemini API, Uvicorn, and Jinja2 as prerequisites.

6. Technology Stack
Technology	Purpose
Python	Backend programming
FastAPI	Web API framework
Google Gemini	AI functionality
HTML	Frontend structure
CSS	Frontend styling
Jinja2	HTML template rendering
Uvicorn	Application server
VS Code	Development environment
GitHub	Version control and project submission

8. Input Requirements
The user can provide:
Questions
Topics
Text for summarization
Topics for quizzes
Topics for learning paths

8. Output Requirements
The system produces:
Answers
Explanations
Quiz questions
Quiz scores
Summaries
Learning recommendations

10. Conclusion
The requirement analysis identifies the functional, non-functional, hardware, and software requirements needed to develop EduGenie successfully.

PHASE 3 — PROJECT DESIGN:

1. Project Title
EduGenie: Google Gemini Powered Learning Assistant

2. System Architecture
EduGenie follows a simple web application architecture.

              USER
                |
                v
       +----------------+
       |  HTML / CSS UI |
       +----------------+
                |
                v
       +----------------+
       | FastAPI Backend|
       |    main.py     |
       +----------------+
                |
       +--------+--------+--------+--------+
       |        |        |        |        |
       v        v        v        v        v
     Q&A    Explain    Quiz   Summary   Learning
     Module  Module    Module  Module    Path
       |        |        |        |        |
       +--------+--------+--------+--------+
                |
                v
       +----------------+
       | Google Gemini  |
       |      API       |
       +----------------+
                |
                v
       AI Generated Result
                |
                v
              USER

The project architecture separates the backend into modules for Q&A, explanation, quiz, summary, and learning path functionality.

3. Project Modules
3.1 main.py

This is the main FastAPI application.

It:

Creates the FastAPI application.
Serves the frontend.
Defines API endpoints.
Connects the different modules.
3.2 qna.py

This module handles student questions.

Input:

Student Question

Output:

AI Generated Answer
3.3 explanation_module.py

This module explains topics in simple language.

Output includes:

Definition
Explanation
Example
3.4 quiz_module.py

This module generates quizzes.

The quiz contains:

3 questions
4 options per question
Correct answer
3.5 summary_module.py
This module summarizes long text and provides the important points.

3.6 learning_path.py
This module creates a learning path from beginner to advanced level.

3.7 index.html
This is the main frontend page.
It provides:
Task selection
User input
Submit button
Result display
Quiz answer checking

3.8 style.css
This file controls the appearance and layout of the web interface.

4. API Endpoints
Endpoint	Purpose
/	Displays the homepage
/qa	Question answering
/explain	Topic explanation
/quiz	Quiz generation
/summarize	Text summarization
/learn/recommendations	Learning path recommendation

These endpoints correspond to the backend functions described in the project documentation.

5. Data Flow
User enters input
       ↓
Frontend sends request
       ↓
FastAPI receives request
       ↓
Correct module is selected
       ↓
Module creates Gemini prompt
       ↓
Google Gemini processes request
       ↓
AI response is returned
       ↓
Frontend displays result

7. User Interface Design
The frontend contains:
Project title
Feature/task dropdown
Text input area
Submit button
Result section
Quiz answer checking section

The project documentation describes the frontend as a simple responsive interface with task selection, textarea input, submission, and result display.

7. Conclusion
The project design provides a modular architecture that makes EduGenie easy to understand, maintain, test, and extend.

PHASE 4 — PROJECT PLANNING:

1. Project Title

EduGenie: Google Gemini Powered Learning Assistant

2. Project Goal

The main goal is to develop a web-based AI educational assistant that helps students learn through question answering, explanations, quizzes, summaries, and personalized learning paths.
3. Project Objectives
Design the educational assistant.
Analyze system requirements.
Develop the backend.
Develop the frontend.
Integrate Google Gemini.
Test all features.
Prepare documentation.
Demonstrate the completed project.

4. Development Plan
Stage 1 — Ideation
Identify the educational problem and decide the project concept.

Stage 2 — Requirement Analysis
Identify:

Functional requirements
Non-functional requirements
Technologies
Hardware requirements
Software requirements
Stage 3 — Design

Design:
System architecture
Backend modules
Frontend
API endpoints
User flow
Stage 4 — Development

Develop:
FastAPI backend
Gemini integration
Q&A module
Explanation module
Quiz module
Summary module
Learning path module
Frontend
Stage 5 — Testing
Test each feature individually and test the complete application.

Stage 6 — Documentation
Prepare:
Project report
Screenshots
Test results
Installation instructions
GitHub repository
Stage 7 — Demonstration

Prepare a demonstration video showing the complete working project.

5. Project File Structure
EduGenie
│
├── 01_Brainstorming_and_Ideation
│
├── 02_Requirement_Analysis
│
├── 03_Project_Design
│
├── 04_Project_Planning
│
├── 05_Project_Development
│
├── 06_Project_Testing
│
├── 07_Project_Documentation
│
├── 08_Project_Demonstration
│
├── main.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
│
├── templates
│   └── index.html
│
└── static
    └── style.css
   
7. Development Timeline
Phase	Activity
Phase 1	Brainstorming and Ideation
Phase 2	Requirement Analysis
Phase 3	Project Design
Phase 4	Project Planning
Phase 5	Project Development
Phase 6	Project Testing
Phase 7	Project Documentation
Phase 8	Project Demonstration

9. Expected Outcome
At the end of the project, students should be able to interact with EduGenie through a web interface and use all five educational features.

PHASE 5 — PROJECT DEVELOPMENT:

1. Project Title
EduGenie: Google Gemini Powered Learning Assistant

2. Development Overview
EduGenie was developed using Python, FastAPI, Google Gemini, HTML, CSS, Jinja2, and Uvicorn.

The backend is divided into multiple modules to make the project organized and maintainable.

3. Backend Development
main.py
The main application is created using FastAPI.
It connects all the modules and provides API endpoints.

4. Q&A Module
The Q&A module accepts a question from the user and sends it to Google Gemini.

Question
   ↓
qna.py
   ↓
Google Gemini
   ↓
Answer

5. Explanation Module
The explanation module creates a prompt asking Gemini to explain a topic in simple language.
The generated response contains:
Definition
Explanation
Example

7. Quiz Module
The quiz module requests Google Gemini to generate exactly three multiple-choice questions.
Each question contains four options and a correct answer.
The response is converted from JSON into Python data so that the frontend can display the quiz.

7. Summary Module
The summary module sends the user's text to Gemini and requests a concise summary.

8. Learning Path Module
The learning path module asks Gemini to create a structured learning path from beginner to advanced level.

It includes:
Topic
Difficulty
Description
Suggested resources

9. Frontend Development
The frontend was developed using HTML and CSS.
The user can select one of the following tasks:

Q&A
Explain
Quiz
Summarize
Learning Path

The user enters their content and submits it.

The generated result is then displayed on the page.

10. Running the Project
The application can be started using:
uvicorn main:app --reload
The application can then be accessed through:

http://127.0.0.1:8000

The project documentation specifies Uvicorn and the local 127.0.0.1:8000 address for running the application.

11. Version Control

The project source code is maintained in a public GitHub repository.

Repository:

https://github.com/dsdharshini45/EduGenie-Google-Gemini-Powered-Learning-Assistant

12. Conclusion
The development phase successfully integrates the frontend, FastAPI backend, separate educational modules, and Google Gemini to create the EduGenie learning assistant.

PHASE 6 — PROJECT TESTING:
1. Project Title

EduGenie: Google Gemini Powered Learning Assistant

2. Testing Objective

The objective of testing is to verify that every feature of EduGenie works correctly and produces an appropriate result.

3. Testing Method

Each feature was tested using different inputs.

The following areas were tested:

Q&A
Explanation
Quiz
Summarization
Learning Path
Frontend
API endpoints
4. Test Cases
Test Case 1 — Question Answering

Input:

What is the largest ocean in the world?

Expected Result:

The system should provide an appropriate answer explaining that the Pacific Ocean is the largest ocean.

Status:

Pass

Test Case 2 — Topic Explanation

Input:

Java

Expected Result:

The system should provide:

Simple definition
Explanation
Example

Status:

Pass

Test Case 3 — Quiz Generation

Input:

Pythagoras Theorem

Expected Result:

The system should generate:

3 questions
4 options for each question
Correct answers

Status:

Pass

Test Case 4 — Text Summarization

Input:

A long educational paragraph.

Expected Result:

The system should generate a shorter summary containing the main points.

Status:

Pass

Test Case 5 — Learning Path

Input:

SQL

Expected Result:

The system should generate a learning path from beginner to advanced level.

Status:

Pass

Test Case 6 — Empty Input

Input:

Empty input

Expected Result:

The application should handle the input appropriately without crashing.

Status:

Pass

Test Case 7 — Frontend

Test:

Select different options from the task dropdown.

Expected Result:

The appropriate feature should execute.

Status:

Pass

Test Case 8 — Quiz Answer Checking

Test:

Select answers and click Check Answers.

Expected Result:

The application should calculate and display the score.

Status:

Pass

5. Testing Summary
Feature	Test Result
Q&A	Pass
Explain	Pass
Quiz	Pass
Summarize	Pass
Learning Path	Pass
Frontend	Pass
Quiz Checking	Pass

7. Conclusion
Testing confirms that the major EduGenie features work as intended and that the application can process user inputs and display AI-generated educational results.
Important: For your final submission, replace/add screenshots of your actual testing results wherever possible.

PHASE 7 — PROJECT DOCUMENTATION:

1. Project Title
EduGenie: Google Gemini Powered Learning Assistant

2. Abstract
EduGenie is a lightweight AI-powered educational assistant designed to support students in their learning activities.
The application uses Google Gemini to provide question answering, simple topic explanations, quiz generation, text summarization, and learning path recommendations.
The backend is developed using FastAPI and Python, while the frontend uses HTML and CSS.

3. Problem Statement
Students may face difficulty understanding complex concepts and finding appropriate learning resources.
EduGenie provides a single interface through which students can receive AI-powered educational assistance.

4. Objectives
The main objectives are:
Provide quick answers.
Explain difficult concepts simply.
Generate quizzes.
Summarize learning materials.
Recommend learning paths.
Support self-learning.

6. Technologies Used
Python
FastAPI
Google Gemini
HTML
CSS
Jinja2
Uvicorn
GitHub
Visual Studio Code

8. System Architecture
User
 ↓
HTML/CSS Frontend
 ↓
FastAPI Backend
 ↓
Educational Modules
 ↓
Google Gemini API
 ↓
Generated Response
 ↓
Frontend
 ↓
User

10. Features
Q&A
Answers student questions.

Explain
Provides simple explanations and examples.

Quiz
Generates multiple-choice quizzes.
Summarize
Summarizes long text.
Learning Path
Creates a structured learning plan.

8. Project Files
main.py
qna.py
explanation_module.py
quiz_module.py
summary_module.py
learning_path.py
requirements.txt
templates/index.html
static/style.css

The documented project architecture uses these separate modules and frontend files.

9. Installation
Step 1

Install Python 3.10 or higher.

Step 2

Create a virtual environment.

Step 3

Install the required packages.

pip install -r requirements.txt
Step 4

Configure the Gemini API key securely as an environment variable.

Step 5
Start the application.

uvicorn main:app --reload

Step 6
Open:
http://127.0.0.1:8000
10. Advantages
Simple interface
AI-powered learning assistance
Multiple educational features
Fast responses
Modular architecture
Easy to extend
Supports self-learning

11. Limitations
Requires an internet connection.
Depends on the availability of the Gemini API.
AI-generated responses may sometimes require verification.
Learning resources generated by AI should be reviewed before being relied upon.

13. Future Enhancements
Future versions can include:
Student login
Progress tracking
Personalized dashboards
More quiz types
Voice interaction
Multilingual support
Learning history
Database integration
Advanced analytics

13. Conclusion
EduGenie demonstrates how generative AI can be integrated into an educational web application.
The project combines FastAPI, Python, HTML, CSS, and Google Gemini to provide students with an interactive learning assistant.

Phase 8 — PROJECT DEMONSTRATION:

Project Title:
EduGenie: Google Gemini Powered Learning Assistant
Objective:
To demonstrate the working of the EduGenie application and its main features.
Demonstration Includes:
Project introduction
Project purpose
Technologies used
Q&A demonstration
Topic Explanation
Quiz Generation
Text Summarization
Learning Path Recommendation
Final output

Demo Video:
A screen-recorded video with voice-over will demonstrate the complete working of the project.
Google Drive Demo Link:
Paste your Google Drive video link here
Conclusion:
The demonstration shows the successful working of the EduGenie AI-powered learning assistant.
