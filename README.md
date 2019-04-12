# SSRF-vuln-example

use "docker-compose up" to spin up the challenge. listens on port 2000 by default.

this image will help you understand SSRF vulns better.
1. there is a "website tester" that will take a URL and return the server response. 
2. if you point it to a system you control, you can capture the "X_SECRET_AUTH_KEY" in its request headers.
3. next, you can port scan localhost using the tester by trying "http://localhost:22","http://localhost:23","http://localhost:24", and so on. 
4. once you find the open port, you can pass in the "X_SECRET_AUTH_KEY" and access the sensitive data..
