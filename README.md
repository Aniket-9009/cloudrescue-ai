☁️ CloudRescue AI
AI-Powered AWS Cloud Troubleshooting Assistant

CloudRescue AI is an experimental AI-powered cloud troubleshooting assistant developed to demonstrate intelligent diagnostic tool selection for common AWS infrastructure problems.

The project uses Strands Decider 2B, a Streamlit-based interface, and Python diagnostic tools to demonstrate how AI-assisted workflows can help identify potential cloud networking issues.

The current application focuses on simulated AWS troubleshooting scenarios. Amazon Bedrock integration is under development.

🎯 Problem Statement

Troubleshooting AWS infrastructure issues can be challenging, especially for beginners.

Common problems include:

SSH connection failures
EC2 internet connectivity issues
Incorrect security group configurations
Route table configuration problems
Application Load Balancer connectivity issues
Unhealthy load balancer targets

Identifying the correct diagnostic tool and understanding the possible cause can require significant manual investigation.

💡 Proposed Solution

CloudRescue AI demonstrates an AI-assisted troubleshooting workflow that helps users identify relevant diagnostic tools based on reported cloud infrastructure problems.

The application provides:

An interactive troubleshooting dashboard
AI-based diagnostic tool selection using Strands Decider 2B
Simulated AWS network diagnostics
Troubleshooting findings and suggested actions
Tool-selection confidence and probability visualization

The long-term goal is to extend the application with live AWS infrastructure diagnostics and AI-generated explanations.

🚀 Key Features
1. Intelligent Diagnostic Tool Selection

Uses Strands Decider 2B to select a relevant diagnostic tool for a reported infrastructure issue.

2. Interactive Streamlit Dashboard

Provides a user-friendly interface for exploring AWS troubleshooting scenarios.

3. SSH Connectivity Troubleshooting

Demonstrates common SSH connectivity problems involving port 22 and security group configurations.

4. Internet Connectivity Troubleshooting

Demonstrates network troubleshooting scenarios involving routing and internet access.

5. Load Balancer Troubleshooting

Demonstrates Application Load Balancer connectivity and target health troubleshooting scenarios.

6. Tool Selection Visualization

Displays model tool-selection confidence and probability information.

7. CPU-Compatible Model Configuration

Includes support for a 4-bit quantized model configuration.

8. Amazon Bedrock Integration

Integration is under development and is not currently part of the working demonstration.

🛠️ Technologies Used
Technology	Purpose
Python	Application development
Streamlit	Interactive web dashboard
Strands Decider 2B	Diagnostic tool selection
PyTorch	Machine learning framework
Hugging Face Transformers	Model loading and inference
BitsAndBytes	Model quantization
Boto3	AWS SDK for Python
Amazon Bedrock	Planned AI explanation integration
Git	Version control
GitHub	Source code hosting
🏗️ System Architecture
                 USER
                   |
                   v
          Streamlit Dashboard
                   |
                   v
          Strands Decider 2B
                   |
                   v
          Diagnostic Tool Selection
                   |
          +--------+--------+
          |        |        |
          v        v        v
         SSH    Internet   Load
        Checker  Checker  Balancer
                           Checker
          |        |        |
          +--------+--------+
                   |
                   v
         Simulated Diagnostics
                   |
                   v
        Troubleshooting Findings
                   |
                   v
          Streamlit Dashboard
Planned Extension
       Diagnostic Findings
                |
                v
          Amazon Bedrock
                |
                v
      AI-Generated Explanation
                |
                v
       Troubleshooting Advice

Note: The current diagnostic tools simulate AWS infrastructure findings rather than querying live AWS resources.

📂 Project Structure
cloudrescue-ai/
│
├── app.py
├── bedrock_ai.py
├── decider_4bit.py
├── diagnostic_tools.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
File Descriptions

app.py

Main Streamlit application containing the user interface.

decider_4bit.py

Contains the model-related logic for Strands Decider 2B.

diagnostic_tools.py

Contains diagnostic functions for simulated AWS troubleshooting scenarios.

bedrock_ai.py

Contains the Amazon Bedrock integration code under development.

requirements.txt

Lists the Python dependencies required by the application.

⚙️ Installation and Setup
Prerequisites
Python 3
Git
Internet connection for installing dependencies and downloading model files
Sufficient memory and compatible hardware for model inference
Step 1: Clone the Repository
git clone https://github.com/<YOUR_USERNAME>/cloudrescue-ai.git
cd cloudrescue-ai

Replace <YOUR_USERNAME> with your actual GitHub username.

Step 2: Create a Virtual Environment
python3 -m venv .venv

Activate the virtual environment:

Linux / Ubuntu / WSL

source .venv/bin/activate

Windows PowerShell

.\.venv\Scripts\Activate.ps1
Step 3: Install Dependencies
python -m pip install -r requirements.txt
Step 4: Run the Application
python -m streamlit run app.py

The application should be accessible at:

http://localhost:8501

Note: Initial model loading may require downloading model files. CPU-based inference can take additional time, and 4-bit quantization requires compatible dependencies and hardware.

🔍 Diagnostic Modules
SSH Diagnostic Tool

Demonstrates troubleshooting scenarios involving:

SSH port 22
Security group inbound rules
EC2 connectivity
Potential SSH access restrictions
Internet Diagnostic Tool

Demonstrates troubleshooting scenarios involving:

Internet gateways
Route tables
Network routing
Internet connectivity
Load Balancer Diagnostic Tool

Demonstrates troubleshooting scenarios involving:

Application Load Balancers
Target groups
Target health
Connectivity problems

Important: These modules currently return simulated diagnostic findings. They do not directly inspect or modify live AWS infrastructure.

🧪 Example Troubleshooting Scenario
User Problem

"My EC2 instance is not accessible through SSH."

Diagnostic Workflow
User reports SSH problem
          |
          v
Diagnostic tool selection
          |
          v
SSH Diagnostic Tool
          |
          v
Simulated configuration check
          |
          v
Potential Issue:
SSH Port 22 is blocked
          |
          v
Suggested Action:
Review Security Group
Inbound Rules
Expected Demonstration

The application illustrates how a relevant diagnostic tool can identify a possible cause and suggest an appropriate troubleshooting action.

The result is illustrative and does not confirm the configuration of an actual EC2 instance.

🤖 Amazon Bedrock Integration Status

Amazon Bedrock integration is being developed to provide AI-generated explanations and troubleshooting recommendations.

During testing, the Bedrock invocation returned:

ValidationException: Operation not allowed

The model access issue is awaiting resolution.

Until Bedrock access is available, the project demonstrates its Streamlit interface, diagnostic workflow, and simulated troubleshooting capabilities.

📊 Project Status
Component	Status
Python Application	Implemented
Streamlit Dashboard	Implemented
Strands Decider 2B Integration	Implemented; runtime validation required
Diagnostic Tool Selection	Implemented; runtime validation required
SSH Troubleshooting Simulation	Implemented
Internet Troubleshooting Simulation	Implemented
Load Balancer Troubleshooting Simulation	Implemented
Tool Selection Visualization	Implemented; runtime validation required
Amazon Bedrock Integration	Pending
Live AWS Infrastructure Diagnostics	Future Enhancement
🔮 Future Enhancements

Potential future improvements include:

Live EC2 security group inspection using Boto3
Automated VPC route table analysis
Live Application Load Balancer health checks
Amazon Bedrock-generated troubleshooting explanations
CloudWatch monitoring integration
AI-assisted root cause analysis
Additional AWS diagnostic tools
Improved model performance and deployment options
🏆 Hackathon

Project: CloudRescue AI

Event: AWS Builder Center Agent Experience Hackathon

Project Focus: Intelligent diagnostic tool selection using Strands Decider 2B.

The project explores how AI-based tool selection can support cloud troubleshooting workflows.

🔐 Security

This repository should not contain:

AWS access keys
AWS secret access keys
Personal access tokens
Passwords
Environment files containing secrets
AWS credential files
Private keys

Sensitive configuration files and unnecessary generated files should be excluded using .gitignore.

The application is intended for demonstration and learning purposes.

⚠️ Limitations
Diagnostic findings are simulated.
Live AWS resource inspection is not implemented.
Amazon Bedrock invocation is currently unavailable.
Model execution depends on compatible hardware and installed dependencies.
The application should not be used as a replacement for production AWS monitoring or security tools.
📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

⭐ Conclusion

CloudRescue AI demonstrates an approach to AI-assisted AWS troubleshooting through diagnostic tool selection, simulated network analysis, and an interactive Streamlit interface.

The project provides a foundation for future integration with live AWS infrastructure diagnostics and Amazon Bedrock-powered troubleshooting explanations.
