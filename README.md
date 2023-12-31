## Components of My Assignment:

**GitHub Actions**: GitHub Actions is a key component of this solution. It is used to automate the deployment of code to a server hosted on DigitalOcean. GitHub Actions allows continuous integration and continuous deployment (CI/CD) and ensures that changes made to the codebase are automatically built and deployed when merged into the main branch.

**SSH (Secure Shell)**: SSH is utilized for secure remote access to the DigitalOcean server. It plays a critical role in authorizing the automated deployment process. SSH keys are used for authentication, ensuring a secure connection between the GitHub Actions workflow and the remote server.

**DigitalOcean Droplet**: DigitalOcean provides the server infrastructure for hosting the application. The DigitalOcean Droplet is the virtual machine instance where the application runs and is where the code is deployed using GitHub Actions. The SSH key authentication ensures secure communication between GitHub Actions and the Droplet.

## Problems Encountered and Solutions:
**SSH Authentication**: One of the initial challenges was setting up SSH authentication between GitHub Actions and the DigitalOcean Droplet. It involved generating and managing SSH keys. The solution was to create paired SSH keys, store the private key as a GitHub secret HOST, USERNAME, KEY and PORT, create an authorized key both in local and on the server, and finally use it in the GitHub Actions workflow. This enabled secure authentication without exposing sensitive information.

**Host Resolution**: The issue of hostname resolution arose during SSH connections. To address this, I ensured that the hostname used in the SSH command was correctly formatted and resolvable.

**Debugging and Logging**: Debugging issues in the CD pipeline required effective logging and error handling. I implemented logging mechanisms in the GitHub Actions workflow to capture relevant information and diagnose problems quickly, then delete it when the debug was done. Additionally, I used appleboy to execute remote SSH commands.

## Note about the Process:
This assignment showed me the importance of automation and continuous development. GitHub Actions, combined with DigitalOcean's infrastructure, create a robust and efficient deployment pipeline, and it is esyer in the end to be able to work on local and deploy on the server. It also highlights the significance of security in SSH key management and access control.

Overall, the solution's success hinged on the integration of working both local and in the server, and a focus on security best practices. It demonstrates the power of DevOps tools in automating the software delivery process while maintaining a high level of security and reliability.