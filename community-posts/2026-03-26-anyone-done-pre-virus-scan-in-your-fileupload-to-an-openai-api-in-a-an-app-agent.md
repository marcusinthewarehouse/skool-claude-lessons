# Anyone Done Pre-Virus Scan in your fileupload to an OpenAI API in a an app agent??

**Created:** 2026-03-26
**Upvotes:** 1
**Comments:** 3
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/anyone-done-pre-virus-scan-in-your-fileupload-to-an-openai-api-in-a-an-app-agent

---

Does anyone have any experience handling user uploaded files being fed into an OpenAI Agent the users would then have a Chat Agent window to interact with which connects back to Open AI which analyzes the file. Our Product team is complaining the current AWS Clambda \(Lambda, S3, and ClamAV\) process is too slow to go through and they want to go directly to the agent. As a security architect and our current virus scanning policy \(SOC2\) we need to be scanning all files prior to the upload process. Outside of that uploading a file directly into the infrastructure is a security recipe for disaster.

We are using AWS and currently do not have GuardDuty which can perform S3 object scans and tagging \(which is an alternative approach to the AWS Clamba solution\), I have no idea how fast it is. Another option is a Light Scan concept in a Sandbox which still opens up to parser or prompting injection exploits.. So this does become a Security vs. Risk Appetite decision.

Has anyone come across this problem? How did you solve it???
