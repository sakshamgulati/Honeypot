### Background
A very effective way of combating the impact of cyberattacks on computer infrastructure is to set
up a honeypot. A honeypot is a computer or computer system intended to mimic likely targets of
cyberattacks. It can be used to detect attacks or deflect them from a legitimate target. It can also
be used to gain information about how cybercriminals operate. The principle behind a honeypot
is simple: don’t stop attacks; instead, prepare something that would attract attacks — the
honeypot — and then wait for the attackers to strike the honeypot instead of your servers.
Cybercriminals are attracted to honeypots because they think each honeypot is a legitimate target,
something worthy of their time. That’s because the bait includes applications and data that
simulate real computer systems.

### Data
We have been provided data gathered from honeypots for analysis. The file honeypot.json is a subset of our honeypot data.

Here is the data dictionary for the file:
<ol>
  <li>"timestamp": date of the event
  <li>"tags": events are known to us and we have a tag for it
  <li>"payload": actual network payload seen by our honeypots
  <li>"port": "0" port where connection was seen
  <li>"country_name": country of our honeypot
  <li>"as_num": "8075" AS number of the IP targeting us
  <li>"proxy_type": "DCH" type of proxy of the IP targeting us (if it is a proxy)
  <li>"ip": "13.42.34.10" target IP address that connected to our honeypots
  <li>"country_name_1": "United Kingdom" country of IP connecting to our honeypot
</ol>

### Question/Objective-
Using the data on the file create an analysis of your choice. This exercise is meant to act as a way to explore your imagination and analytics experience. You're welcome to enrich this data with other sources, or build any type of product or analysis with it.

### Notebook
https://colab.research.google.com/drive/123jgxOuIuBkQliNkBXmsA_vSJiRfJbHm#scrollTo=EPjW9Z0QLI-U
