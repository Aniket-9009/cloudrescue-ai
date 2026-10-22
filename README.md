CloudRescue AI
AI-Powered AWS Cloud Troubleshooting Assistant
CloudRescue AI is an experimental AI-powered cloud troubleshooting assistant that uses Strands Decider 2B to select diagnostic tools based on user-reported AWS infrastructure issues.

The application provides an interactive Streamlit interface for demonstrating intelligent tool selection and simulated cloud troubleshooting workflows.

Key Features
AI-powered diagnostic tool selection using Strands Decider 2B
Interactive Streamlit dashboard
SSH connectivity troubleshooting scenarios
Internet connectivity troubleshooting scenarios
Application Load Balancer troubleshooting scenarios
Tool-selection confidence and probability visualization
CPU-compatible 4-bit quantized model loading
Amazon Bedrock integration under development
Technologies Used
Python
Strands Decider 2B
PyTorch
Hugging Face Transformers
BitsAndBytes
Streamlit
Amazon Bedrock (Integration Pending)
AWS SDK for Python (Boto3)
Architecture
User Request | v Streamlit Interface | v Strands Decider 2B | v AI Tool Selection | +---- SSH Diagnostic Tool | +---- Internet Diagnostic Tool | +---- Load Balancer Diagnostic Tool | v Simulated Diagnostic Result | v Streamlit Dashboard

Planned Extension:

Diagnostic Result | v Amazon Bedrock | v AI-Generated Troubleshooting Explanation

Installation
1. Clone Repository
git clone <YOUR_REPOSITORY_URL>

cd cloudrescue-ai

2. Create Virtual Environment
python3 -m venv .venv

source .venv/bin/activate

3. Install Dependencies
python -m pip install -r requirements.txt

4. Run Application
python -m streamlit run app.py

Note: The model is downloaded during initial setup or first use. Model loading can take several minutes on CPU-only systems.

Diagnostic Tools
SSH Checker
Demonstrates troubleshooting for SSH connectivity problems, including security group and port 22 configuration scenarios.

Internet Checker
Demonstrates troubleshooting for internet connectivity problems involving routing and network configuration.

Load Balancer Checker
Demonstrates troubleshooting for Application Load Balancer connectivity and target health scenarios.

These tools currently return simulated diagnostic findings and do not inspect live AWS infrastructure.

Amazon Bedrock Integration Status
Amazon Bedrock is planned for generating AI-powered troubleshooting explanations and recommendations.

The Bedrock integration is currently pending because model invocation returns:

ValidationException: Operation not allowed

An AWS Support case is under review.

The current working application demonstrates Strands Decider 2B tool selection and simulated diagnostic responses.

Project Status
Strands Decider 2B: Implemented
Diagnostic Tool Selection: Implemented
Streamlit Dashboard: Implemented
Simulated Diagnostics: Implemented
Amazon Bedrock Integration: Pending
Hackathon
Developed for the AWS Builder Center Agent Experience Hackathon.

Focus: Intelligent tool selection using Strands Decider 2B.

Security
AWS credentials, environment files, model weights, and virtual environments should not be committed to this repository.

License
MIT License.
