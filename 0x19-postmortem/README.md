# Postmortem: Web Stack Outage Incident
Issue Summary
Duration: From 10:00 AM to 2:00 PM (UTC-07:00)
Impact: The user authentication service experienced a complete outage, affecting 30% of our active users.
Root Cause: A misconfigured firewall rule inadvertently blocked traffic to the authentication server.
Timeline
9:45 AM: Issue detected by monitoring alerts showing a sudden drop in successful login requests.
9:50 AM: Engineers noticed increased latency in user authentication.
10:00 AM: Investigation began, focusing on the authentication service and related components.
10:30 AM: Initial assumption: Database connection issues due to high load.
11:00 AM: Debugging paths explored: Checked database logs, analyzed query performance.
11:30 AM: Escalated incident to the DevOps team for further analysis.
12:00 PM: Misleading path: Investigated load balancer settings, but no issues found.
1:00 PM: Realized the firewall rules were recently updated.
1:30 PM: Corrective action: Rolled back the firewall rule changes.
2:00 PM: Service restored; users could log in successfully.
Root Cause and Resolution
Cause: The new firewall rule blocked incoming traffic to the authentication server.
Resolution: Reverted the firewall rule to its previous state, allowing traffic flow.
Corrective and Preventative Measures
Automated Testing: Implement automated tests for firewall rule changes.
Monitoring Enhancements:
Set up alerts for sudden traffic drops to critical services.
Monitor firewall rule changes and their impact.
Documentation Update:
Clearly document firewall rules and their purpose.
Include rollback procedures.
Incident Response Training:
Train engineers on efficient debugging techniques.
Foster cross-team collaboration during incidents.
Tasks
Patch Firewall Rules:
Add a validation step to prevent accidental blocking.
Regularly review and update rules.
Implement Canary Deployments:
Gradually roll out changes to minimize impact.
Automate Rollback Procedures:
Create scripts to revert changes quickly.
Review Incident Communication:
Improve communication channels during outages.
