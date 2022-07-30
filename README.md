# proxy-list-to-switchyomega
This simple python script converts a list of proxies in the format ip:port:username:password into a file that can be imported into the SwitchyOmega Chrome extension. It converts all of the proxies contained within the selected proxy file.

To use simply use the open file dialog to select your proxy list.

The proxy list should be in the format ip:port:username:password
<br>E.g.:
<br>
<br>231.164.184.120:54669:user1:password1<br>
226.206.24.213:31777:user1:password1<br>
34.205.213.167:36595:user1:password1<br>
133.251.63.250:54745:user1:password1<br>
51.176.50.96:35651:user1:password1<br>
245.253.112.154:92544:user1:password1<br>
153.118.204.112:90645:user1:password1<br>
64.13.247.72:90786:user1:password1<br>
92.12.81.50:59676:user1:password1<br>
177.177.211.228:87392:user1:password1<br>

This will generate a new file 'converted_proxies_omega.bak' which can be imported into SwitchyOmega. On SwitchyOmega go to Settings -> Import/Export -> Restore from File. 

**There is also a pre-compiled (.exe) included for convenience (built from main.py)**
