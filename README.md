## force-protect
----------------------------------------------------------
##IPs banning through Apache log analysis and IPTABLES usage
----------------------------------------------------------

This little script was born as a need to block flooding attacks to my server. Basically what it does is analyzing the Apache 
log file and searching for certain key words into a defined filter list and thus determine possible intrusions, script 
execution or port scanning.

Just put the file in any secure directory and give root permissions to run it. Please, notice you need Python previously 
installed in order to be executed.

*USAGE:*

**python force-protect.py**


<br>
Just a few considerations:

**1)** The script analyzes the "other_vhosts_access.log" file, but you can change the filepath according to your system and web 
server.

**2)** There are some filters already declared, but new ones can be added or simply modified from the list, which contains some 
common identifiers.

**3)** As the log file also saves your access, you could prevent being blacklisted by adding your IP(s) into the IF..THEN 
statement.

**4)** In order to monitor the process all the banned IPs are dumped out to "bannedips" file once the script is executed. This 
step is optional and you can remove it if necessary.
