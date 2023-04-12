### get-reach-svhc-list
- py script to fetch the current svhc list as an xml file
- This script is geared toward helping people who are just kickstarting material compliance automation
- If you have questions about this script, or material compliance automation in general, please email me at jayferreira256@gmail.com

### Instructions
##### If you made it here, and you're reading this, then getting this script to work is within your power even if you've never executed a single line of code. However, do note that this isn't a comprehensive tutorial, and absolute beginners will need to do some research.
- If you know how to set up a repo, and have programmed in python, then you don't need to read on. There's only a single file and there's no special set up required. Skip ahead to the considerations section.
- You will need to have a python interpreter installed, version 3.7 or higher. You can get this from the Microsoft Store app if it's not installed. Linux and Mac ship with python interpreters installed.
- To get a copy of the script, I would just copy-paste the code from "regulatory_list_fetching.py" above into a text file. You'll need to save the text file as a python file. Save as "regulatory_list_fetching.py" for consistency.
- Use pip to install the requests package
- Run regulatory_list_fetching.py (you might need to set environment variables, but don't quit now)
- You now have the current SVHC list downloaded as an xml file!

### Considerations
- If the SVHC list exceeds 1000, then the value should be updated on line 31
- This script will save the SVHC list in the same folder as itself as an xml file
