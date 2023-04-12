### get-reach-svhc-list
- py script to fetch the current svhc list as an xml file
- This script is geared toward helping people who are just kickstarting material compliance automation
- If you have questions about this script, or material compliance automation in general, please email me at jayferreira256@gmail.com

### Instructions
##### Instructions assume Windows 10 environment
- You will need to have a python interpreter installed, version 3.7 or higher. You can get this from the Microsoft Store app
- If you're unable to set up a repo, just copy-paste the code from "regulatory_list_fetching.py" above into a text file (use the notepad app). You'll need to save the text file as a python file.
- Use pip to install requests package
- run regulatory_list_fetching.py, and you will have the current SVHC list downloaded as an xml file

### Considerations
- If the SVHC list exceeds 1000, then the value should be updated on line 31
- This script will save the SVHC list in the same folder as itself as an xml file
