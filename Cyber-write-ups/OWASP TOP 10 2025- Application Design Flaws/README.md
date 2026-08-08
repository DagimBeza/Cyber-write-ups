# OWASP TOP 10 2025- Application Design Flaws
## Room Information

- Platform: TryHackMe

- Room: OWASP Top 10 2025: Application Design Flaws


## Obbjective

 - The purpose of this room is to understand vulnerabilities related to application architecture and system design by performing practical exercises involving:

    A02 – Security Misconfiguration

    A03 – Software Supply Chain Failures

    A04 – Cryptographic Failures

    A06 – Insecure Design

## Lab Environment

  - AttackBox 

  - Firefox Browser

  - Burp Suite

  - Browser Developer Tools


## Task 1 – Introduction

### Objective: 

 -Deploy the machine and understand the objectives of the room.

### Screenshot

- Room Overview: https://github.com/DagimBeza/Cyber-write-ups/blob/main/Cyber-write-ups/OWASP%20TOP%2010%202025-%20Application%20Design%20Flaws/images/Task%201%20Room%20overview.png


## Task 2 – Security Misconfiguration

### Objective :

 -  Analyze a web application that exposes unnecessary functionality because of improper configuration.

### Steps Performed

   - Open the web application.

   - Inspect available endpoints.

   - Enumerate exposed API routes.

   - Review HTTP requests and responses.

   - Identify sensitive information exposed by the server.

   - Access the required endpoint.

   - Obtain the challenge answer.

### Screenshots

    - Application Homepage: https://github.com/DagimBeza/Cyber-write-ups/blob/main/Cyber-write-ups/OWASP%20TOP%2010%202025-%20Application%20Design%20Flaws/images/Task%202%20Application%20Homepage.png

    - Inspect available endpoints: https://github.com/DagimBeza/Cyber-write-ups/blob/main/Cyber-write-ups/OWASP%20TOP%2010%202025-%20Application%20Design%20Flaws/images/Task%202%20Inspect%20available%20endpoints%20.png

    - Challenge Completed: https://github.com/DagimBeza/Cyber-write-ups/blob/main/Cyber-write-ups/OWASP%20TOP%2010%202025-%20Application%20Design%20Flaws/images/Task%202%20Challenge%20Completed.png

### Findings

    - The application exposed information that should not be publicly accessible because unnecessary endpoints remained enabled.

### Risk

Attackers can:

   -  Discover internal APIs

   -  Enumerate users

   - Reveal configuration data

### Prevention

    - Disable debugging

    - Remove unnecessary endpoints

    - Restrict administrative APIs

    - Implement authentication



## Task 3 – Software Supply Chain Failures

### Objective

- Investigate an application using outdated or insecure third-party components.

### Steps Performed

   - Review application files.

   - Identify imported libraries.

   - Locate vulnerable component.

   - Understand how the vulnerable dependency affects the application.

   - Complete the challenge.

### Screenshots

    - Application Code: 

    - API Health: 

    - API Process:

    - Challenge Answer: 

### Findings

- The application relied on an outdated dependency containing a known vulnerability.

### Risk

 Using vulnerable libraries may allow attackers to:

   - Execute arbitrary code

   - Bypass authentication

   - Read sensitive files

   - Compromise the application

### Prevention

   - Update dependencies regularly

   - Use dependency scanners

   - Remove unused libraries

   - Enable Software Composition Analysis (SCA)


## Task 4 – Cryptographic Failures

### Objective

  - Investigate improper cryptographic implementation and recover encrypted information through the intended   lab exercise.

### Steps Performed

   - Inspect the application.

   - Locate encrypted data.

   - Identify where the decryption key is referenced.

   - Use the intended decryption process provided by the exercise.

   - Recover the plaintext and complete the task.


### Screenshot

- Encrypted Document: 

- Source page:

- Secret page:

- Recovered Plaintext:

### Findings

- Sensitive information was protected using an insecure key management approach.

### Risk

  Poor cryptographic practices can expose:

   - Passwords

   - Secrets

   - API Keys

   - Confidential files

### Prevention

    - Store secrets securely

    - Use strong encryption

    - Rotate keys regularly

    - Never hardcode secrets

    - Use secure key management systems


### Task 5 – Insecure Design

### Objective

 - Understand how insecure application logic can lead to security vulnerabilities.

### Steps Performed

   - Analyze application workflow.

   - Observe assumptions made by developers.

   - Test application behavior.

   - Identify design weakness.

   - Complete the exercise.

### Screenshot

   - Application Homepage: 

   - Application Source page: 

   - API Testing:

   - Challenge Completed: 

### Findings

 - The application trusted assumptions about client behavior instead of enforcing security controls on the server.

### Risk

 Insecure design can result in:

   - Authentication bypass

   - Business logic abuse

   - Privilege escalation

   - Unauthorized access

### Prevention

   - Apply secure-by-design principles

   - Validate requests server-side

   - Perform threat modeling

   - Conduct security architecture reviews

   - Test business logic thoroughly
   

## Task 6 - Conclusion

### Lessons Learned

 - Secure software depends not only on writing safe code but also on sound architecture and operational practices.
 
 - Misconfigurations, outdated dependencies, weak cryptographic implementations, and flawed design decisions can all introduce exploitable vulnerabilities.

 - Following the OWASP Top 10 guide helps reduce these risks through secure configuration, dependency management, proper cryptography, and security-focused design.

 ### Screenshot

  - Completed:

