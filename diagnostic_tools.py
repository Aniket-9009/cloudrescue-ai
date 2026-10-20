"""
CloudRescue AI
AWS Networking Diagnostic Tools

Simulation Mode:
These tools do not access real AWS resources.
"""


# =====================================
# 1. EC2 SSH CHECKER
# =====================================

def check_ssh():

    return {
        "status": "error",

        "message": (
            "Simulated EC2 SSH connection failure."
        ),

        "finding": (
            "The sample EC2 Security Group "
            "does not allow inbound TCP port 22."
        ),

        "recommendation": (
            "1. Open AWS EC2 Console.\n\n"
            "2. Select your EC2 instance.\n\n"
            "3. Open the Security tab.\n\n"
            "4. Check Security Group inbound rules.\n\n"
            "5. Allow SSH (TCP 22) from your trusted IP address.\n\n"
            "6. Verify the instance is running, "
            "the correct SSH username and key are used, "
            "and the instance is reachable."
        ),

        "mode": "simulation",
    }


# =====================================
# 2. EC2 INTERNET CHECKER
# =====================================

def check_internet():

    return {
        "status": "error",

        "message": (
            "Simulated EC2 internet connectivity failure."
        ),

        "finding": (
            "The sample EC2 network configuration "
            "does not have a working internet route."
        ),

        "recommendation": (
            "1. Open AWS VPC Console.\n\n"
            "2. Check the subnet's Route Table.\n\n"
            "3. For a public subnet, verify the route "
            "0.0.0.0/0 points to an attached Internet Gateway.\n\n"
            "4. Verify the EC2 instance has a public IP address "
            "if direct internet connectivity is required.\n\n"
            "5. For a private subnet, verify the outbound route "
            "points to a working NAT Gateway when applicable.\n\n"
            "6. Check Security Group and Network ACL rules."
        ),

        "mode": "simulation",
    }


# =====================================
# 3. LOAD BALANCER CHECKER
# =====================================

def check_load_balancer():

    return {
        "status": "error",

        "message": (
            "Simulated Application Load Balancer failure."
        ),

        "finding": (
            "The sample Application Load Balancer "
            "target group contains an unhealthy target."
        ),

        "recommendation": (
            "1. Open AWS EC2 Console.\n\n"
            "2. Select Target Groups under Load Balancing.\n\n"
            "3. Check the registered target health status.\n\n"
            "4. Verify the health check path, port, "
            "protocol, and success codes.\n\n"
            "5. Ensure the application is running "
            "on the target EC2 instance.\n\n"
            "6. Check Security Group rules between "
            "the Load Balancer and its targets."
        ),

        "mode": "simulation",
    }


# =====================================
# TOOL REGISTRY
# =====================================

DIAGNOSTIC_TOOLS = {
    "check_ssh": check_ssh,
    "check_internet": check_internet,
    "check_load_balancer": check_load_balancer,
}


# =====================================
# TOOL DESCRIPTIONS FOR DECIDER
# =====================================

TOOL_DESCRIPTIONS = {
    "check_ssh": (
        "Diagnose SSH login and remote connection failures to an EC2 instance. "
        "Choose this tool when the user mentions SSH, port 22, "
        "Permission denied (publickey), SSH timeout, or connecting "
        "to an EC2 instance through a terminal."
    ),

    "check_internet": (
        "Diagnose an EC2 instance that cannot access the public internet. "
        "Choose this tool for outbound internet failures, "
        "failed internet access, Internet Gateway, NAT Gateway, "
        "or inability to download packages from the internet. "
        "Do not choose for SSH login failures."
    ),

    "check_load_balancer": (
        "Diagnose AWS Application Load Balancer and target group problems. "
        "Choose this tool when the user mentions load balancer, "
        "ALB, unhealthy targets, health check failures, "
        "or target group issues."
    ),
}