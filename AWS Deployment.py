
# # AWS Deployment Steps
# 

# # Initiate empty git folder
Open the project folder : 
    Open in terminal/GitBash here
    git init
    git status
    git add .  (You can add individual files with commit)
    git commit -m "Added all files"Open the github account : 
    Create new repository
    Copy the link createdOpen the terminal : 
    git remote add origin (paste your link)
    git branch -M main
    git push origin main
    Type your github username
    Type your Personal Access Token (PAT)
    Refresh your git repository (All the files will be pushed on your github repo)
    
    
# # Personal Access Token
Steps to create PAT:
    Login to your Github account
    Click on your profile
    Setings
    Developer Settings
    Personal Access Token
    Generate new token
    Select expiration date (Copy your PAT and save fr future reference)
    
    
# # AWS Account Creation

AWS Account Creation:
    Search AWS
    Click on the first link
    Create new account
    Enter your email id
    Create username
    Click on next
    Enter the verification code sent on your email id and verufy your account
    Next
    Choose password
    Fill the details
    Enter your mobile number and address
    Next
    Enter the credit card number
    Expiration month and year
    CVV
    Cardholder name
    Billing address
    PAN number
    Next
    Enter the otp sent on creadit card cardholder number
    Once it is verified you will be able to login in the AWS account


# # AWS Instance Creation


AWS Instance:
    Login on AWS account through signin to the console
    Search for ec2 in search bar
    Launch Instance
    Name of the instance
    Select the OS (Ubuntu 22.04 with free tier eligible)
    Select instance type (t2.micro with free tier eligible)
    Create new key pair (Name the key pair and download it. Save the key pair in project folder)
    Network Security Group (Edit-- Add new security group rule-- type-All Traffic-- Source Type-Anywhere)
    Storage (1*8 -- Free tier has 30 GiB memory)
    Launch Instance


# # Connect Instance and Deployment

Select instance:
    Connect
    Connect with SSH Client
    Open terminal
    cd key (the folder or directory where you have stored the key)
    ls
    Copy the step 3 and paste
    Copy the step 4 and paste
    yes
You will switch on private ip address:
    python3  -- exit()
    sudo apt-get update  (To get updates)
    sudo apt-get install python3-pip (to install pip) ---> Y
    pip --version
    git --version
Open the github repo --- Click on code --- Copy the https link

Open the terminal:
    git clone (Paste the https link)
    cd (Github repo name)
    ls
    python3 app.py
    Copy the public IPv4 DNS and paste in the browser:Port number
    nohup python3 app.py


