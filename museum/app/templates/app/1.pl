C:\xampp\perl\bin\perl.exe
print "content-type: text/html", "\n\n";
print "<HTML>", "\n";
print "<HEAD><TITLE>ABOUT THIS SERVER</TITLE></HEAD>", "\n";
print "<BODY><H1>ABOUT THIS SERVER</H1>", "\n";
print"<HR><PRE>";
print "server name: ", $ENV{'SERVER_NAME'}, "<br>", "\n";
print "Running on the port: ", $ENV{'SERVER_PORT'}, "<br>", "\n";
print "Server software:
", $ENV{'SERVER_SOFTWARE'}, "<br>", "\n";
print "Server protocol:
", $ENV{'SERVER_PROTOCOL'}, "<br>", "\n";
print "CGI VERSION:
", $ENV{'GATEWAY_INTERFACE'}, "<br>", "\n";
print "root document:
", $ENV{'DOCUMENT_ROOT'}, "<br>", "\n";
print "<HR></PRE>", "\n";
print "</BODY></HTML>", "\n";
exit(0);