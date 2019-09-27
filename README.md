DNS Blocklists (And a whitelist)
---------------------------------


This project contains a few DNS blocklists that I have created for various purposes, mostly related to other projects 
  I am working on. There's also a whitelist that I actively curate & use to prevent dns based adblockers from 
  blocking domains that are commonly blocked by public dns blocklists and break functionality of needed sites.
  

### Current Lists

* **https://zebpalmer.github.io/dns_blocklists/whitelist.txt** is the whitelist mentioned above. Feel free to use it, 
 additions are welcome, just open an issue in the github repo (see below), a pull request would be fantastic or reach 
 out to me on twitter @zebpalmer. 

* **https://zebpalmer.github.io/dns_blocklists/slim.txt** This blocklist is actively curated based on network activity I see on networks I manage (including a few public
 wifi networks). It is intended to be lightweight, while blocking a large number of ads/trackers/etc with a minimum of 
 false positives. Additions are welcome, but this list is not intended to block everything. If I don't see a domain 
 getting hit on any of those networks, the domain will be removed. 

* **https://zebpalmer.github.io/dns_blocklists/blocklist.txt** This file contains the 10,000 most common domains in 
 roughly 100 publicly available blocklists I've found. That doesn't imply quality, just that these domains are in 
 a lot of blocklists. It's mainly a test file I'm using for a related project. See note in the file's header comment 
 for more info about this one. 
 
### DNS Blockworkr

One of the other DNS related projects I'm working on is a tool that enables anyone to mix and match blocklists 
 and whitelists to provide any DNS blocking tool one unified blocklist. This might be useful if you maintain multiple 
 instances of dns blocking tools, lets say you have a firewall based blocking tool (i.e. pfblockerng), maybe you've 
 given some family members a raspberry pi with pihole installed, or you use mobile apps, whatever... anyway, if you want 
 to add or remove a blocklist from these instances you'd need to either update them all manually or automate it in some 
 way. With blockworkr, each device uses one blocklist url, that blocklists is dynamicly populated by deduping your 
 configured blocklists, throwing out anything in your configured whitelists and providing the result to the dns blocking
 tool. It even supports multiple configs in case you want a more (or less) agressive configuration for some networks.
 This may also be useful for **blocklist maintainers** to create various mixs of their blocklists to provide to users.
 
 Visit the blockworkr repo for more info: https://github.com/zebpalmer/blockworkr 
 
 
### Adding Domains

`./add-domains.py temp/add.txt slim.txt --whitelist whitelist.txt`
 
### Feedback / Suggestions / Contributions

Feel free to open an issue on this repo, submit a pull request or reach me on twitter @zebpalmer. 