# API Testing

## Lab Information

- Platform: PortSwigger Web Security Academy

- Topic: API Testing

## Objective

- The objective of this lab is to understand common API security vulnerabilities and learn how attackers can identify and exploit weaknesses in API endpoints.

## Tools Used

| Tool              | Purpose                                  |
| ----------------- | ---------------------------------------- |

| Browser           | Interacting with the web application     |

| Burp Suite        | Intercepting and modifying HTTP requests |

| Burp Proxy        | Capturing requests                       |

| Burp Repeater     | Testing modified requests                |

| HTTP              | Understanding requests and responses     |

| API documentation | Discovering API endpoints and methods    |


## LAB 1 — Exploiting an API Endpoint Using Documentation

### Lab Objective

- The objective of this lab is to use API documentation to identify an API endpoint and exploit functionality   that is not exposed through the normal website interface.

### Start the Lab

Lab started: 

### Initial Reconnaissance

- Initial application: 

- Login: 

- Update email:


### Capture Requests Using Burp Suite

- HTTP request captured using Burp Proxy: 

- Modified request:

- Modified response:

- Show response in browser:

### Look for API Documentation

- API Documentation:

### Inspect the Documentation

Exposed API documentation: 

Delete carlos:

 
### Result

- The API documentation exposed an API endpoint that was not apparent from the normal application interface.  By analyzing the documented endpoint and sending the appropriate HTTP request, I was able to access the required functionality and complete the lab.

Lab solved: 

### Vulnerability

Exposed API documentation

### Root Cause

The application exposes documentation containing information about API functionality that should not necessarily be publicly accessible.

### Security Impact

Attackers can use the documentation to:

    Discover hidden functionality

    Identify endpoints

    Identify HTTP methods

    Understand parameters

    Build malicious requests

### Remediation

API documentation should:

    Be appropriately access-controlled.

    Avoid exposing sensitive administrative endpoints.

    Require authentication where appropriate.

    Be reviewed before deployment.

    Not be treated as a security boundary.

## LAB 2 — Finding and Exploiting an Unused API Endpoint

### Objective

The objective is to identify an unused API endpoint and exploit it.
An endpoint may still be accessible even if the application's current frontend no longer uses it.

### Login

Login:

### Application Reconnaissance

- Browse the application and intercept requests with Burp Suite.

Initial Application: 

### Analyze API Requests

API request in Burp: 

Send to Repeater:

### Test HTTP Methods

Test OPTIONS:

Try PATCH:


### Identify an Unused Endpoint

Unused endpoint discovered:


### Exploit

Exploit:

### Result

During reconnaissance, I identified an API endpoint that was not used by the application's current frontend.  By analyzing existing API requests and testing the available API functionality, I discovered that the unused endpoint was still accessible. I then used it to complete the lab.

Lab solved:


### Vulnerability

Unused/undocumented API endpoint

### Root Cause

An old API endpoint remains accessible even though the current application does not use it.

### Impact

An attacker may discover functionality that:

    Was forgotten by developers.

    Is insufficiently protected.

    Is not tested as part of the current application.

    Provides access to sensitive operations.

### Remediation

    Remove obsolete endpoints.

    Maintain an API inventory.

    Test all active endpoints.

    Apply authentication and authorization consistently.

    Monitor API usage.


## LAB 3 — Exploiting a Mass Assignment Vulnerability

### Objective

The goal is to exploit mass assignment by adding an unexpected parameter to an API request.

### Initial application

Login:

Homepage:

### Capture a Normal Request

Normal API request and response: 


### Compare GET and POST

Compare:

### Modify the Request

- Add hidden parameter:

Modified request and response: 


### Verify Privilege Change

Refresh the page or revisit the relevant functionality.

Privilege/state change:

### Result

I identified a mass assignment vulnerability by comparing the properties submitted in the request with properties returned by the server. An internal property that should not have been controlled by the client was accepted when included in the request. This allowed the application's internal state to be modified and enabled completion of the lab.

### Vulnerability

Mass assignment

### Root Cause

The application automatically binds user-supplied parameters to internal object properties without sufficiently restricting which properties users can modify.

### Impact

    Privilege escalation

    Unauthorized account modification

    Modification of security settings

    Modification of financial values

    Changing account ownership

### Remediation

   Use an allowlist of writable properties.