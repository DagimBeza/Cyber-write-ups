## Airplane

## Room Information

 - Room: Airplane

 - Platform: TryHackMe

 - Difficulty: Medium

 - Category: CTF / Linux / Web / Privilege Escalation

## Learning Objectives

 - Practice reconnaissance and enumeration with Nmap.

 - Identify and analyze web/application vulnerabilities.

 - Exploit command injection to gain initial access.

 - Perform Linux post-exploitation enumeration.

 - Identify a privilege-escalation path and obtain root access.

 - Understand the complete attack chain from enumeration to privilege escalation.

## Start the Machine

 - Start the Airplane machine in TryHackMe and wait until the platform assigns an address. 

 - Start the machine: 


##  Nmap Scan

 - A full TCP scan establishes the attack surface. The important ports are 22/SSH, 6048/an unusual service, and 8000/HTTP. 

 - Full Nmap scan:

 - Run service/version and default-script enumeration against the three discovered ports. Port 8000 is a Python/Werkzeug web service. Port 6048 is deliberately unusual and deserves follow-up rather than being ignored.

 - Detailed Nmap scan:

## Configuration

- The web application redirects to airplane.thm. Add the target hostname to /etc/hosts so browser and command-line requests resolve correctly.


- The web application redirects to: airplane.thm

- /etc/hosts: 


## Enumeratation

 - The application appears to retrieve a local file based on the value supplied to page

 - That makes this parameter worth testing for Local File Inclusion (LFI) / Path Traversal.

 - Gobuster results:


## Identify the LFI / Path Traversal

 - The URL contains a page parameter such as ?page=index.html. Testing traversal with ../../../../etc/passwd confirms that the server reads files outside its intended web directory.

 - The page parameter can be manipulated to access files outside the intended web directory.

 - The application returns /etc/passwd. This is the first major vulnerability

 - LFI: 


## Find the Flask Application
 
 - The LFI can also read process information. /proc/self/environ identifies the web process context as hudson, and the application source can be recovered from /home/hudson/app/app.py. The source shows that the page parameter is used to select a file and that the application listens on port 8000

 - The /proc filesystem exposes information about running processes.

 - The process command line can reveal how the web server was started.

 - The result indicates that Python is executing:app.py

 - Then attempt to locate the application source, a successful response reveals the Flask source.

 - Analyze the app.py


## Enumerate /proc Processes

 - Identify which process is listening on 6048/tcp

 - Because the application can read /proc/<PID>/..., we can enumerate process IDs.

 - /proc enumeration:


## Identify the GDB Process

 - Because the LFI can access /proc/<PID>/cmdline, enumerate PIDs and inspect command lines. The key discovery is a gdbserver process listening on TCP/6048.

 - Inspect the command line of the interesting PID.

 - The process reveals that a GDB server is listening on 6048. This explains the previously unidentified port.

 - Since GDB supports remote debugging. If a GDB server is exposed without appropriate authentication or 
 
   network restrictions, an attacker can  potentially connect to it and manipulate a debugging session. 

 - GDB discovery:


## Reverse Shell Configuration

- Use an msfvenom linux/x64/shell_reverse_tcp payload with PrependFork=true. 

- Prepare a Reverse Shell Payload and make the payload executable.

- Start the Listener and keep this terminal open.

- Connect to the Remote GDB Server by uploading the payload and set it as executable. Then run it.

- Receive the Reverse Shell by returning to the listenner.

- Payload Generation:

- Use the publicly documented Airplane GDB-server exploitation workflow to connect to TCP/6048, transfer the payload, mark it executable, and trigger execution.

- GDB connection:

- The reverse connection should arrive at the listener as hudson. Confirm with whoami and optionally upgrade the shell with Python PTY. This establishes the initial foothold.

- Reverse shell:


## Upgrade to SSH Access

 - Generate an SSH key pair, then display the public key.

 - On the hudson shell, create the SSH directory and add the public key.

 - Set permissions and connect.

 - SSH session:


## Retrieve the User Flag

 - Once the effective identity is Carlos, read /home/carlos/user.txt.

 - Search for the flag, then read it.

 - User flag: 


## Privilege Escalation

 - For a cleaner Carlos shell, create an SSH key pair on Kali, place the public key into Carlos's authorized_keys, set restrictive permissions, and connect over SSH. This is optional for the core exploit chain but makes the privilege-escalation stage easier to manage.

 - Enumerate SUID binaries and look for unusual binaries.

 - The unusual binary is /usr/bin/find.

 - Because find executes with Carlos's effective privileges, its command-execution functionality can be       abused to obtain a shell with Carlos's effective UID.

 - SUID enumeration:


 ## Check Sudo Privileges

  - Add the public key to Carlos's SSH configuration.

  - Set permissions and confirm.

  - Run sudo -l to see the permission.

  - The wildcard: /root/*.rb is permissive. 
  
  - This is vulnerability. As dangerous wildcard use in sudo configuration can give elvated previlages.

  - Carlos shell:

  - Wildcard:


## Create and Execute the Malicious Ruby Script

 - Create nano /tmp/pwn.rb
 
 - Run chmod 755 /tmp/pwn.rb to change /bin/bash so that it has the SUID bit.

 - Run sudo /usr/bin/ruby /root/../../../../tmp/pwn.rb 

 - Run ls -la /bin/bash to see SUID permission

 - Ruby exploit:


## Obtain a Root Shell

 - The Ruby program executes as root, so the resulting shell has UID 0. If using a SUID bash stage, bash -p preserves the effective privileges. Verify with whoami and id before accessing root-only files.

 - Run /bin/bash -p

 - -p option preserves the effective privileges of the SUID Bash binary.

 - Then whoami and verify id.

 - SUID Bash:

 - Root shell:


## Retrieve root flag

 - Search for the flag and read it.

 - Root flag:

## Lessons Learned

 - Thorough enumeration is essential.

 - Always investigate unusual services and application behavior.

 - Validate user-controlled input for injection vulnerabilities.

 - After gaining access, systematically enumerate the Linux system.

 - Check SUID permissions, files, processes, and services for privilege escalation.

 - Apply secure input validation and least-privilege principles to prevent these attacks.
