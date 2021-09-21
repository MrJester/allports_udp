# allports

Simple script to open sockets on as many UDP ports as you want to test egress firewall settings of systems. 

Updating the range Line 22 you can change how many and which ports are open then from a client machine you can run something like

sudo nmap -sU -p99-150 -v --max-retries=3 [HOST HERE]

Ensure you use the -v or you will not get the full output from nmap since it is not getting data back from the ports. 

Changing the above ports to match the sockets you have open to test firewall rules. 