import requests
import json
import re
#drodr
#
url = "https://michaelgathara.com/api/python-challenge"

# on windows terminal, backlash is not accepted, escape each slash

# https://stackoverflow.com/questions/54517547/curl-having-issue-with-brace-bracket

# used following guide for api help
# https://www.dataquest.io/blog/python-api-tutorial/


response = requests.get(url)

if response.status_code == 200:
    challenges = response.json()

    if challenges:
        for problem in challenges:
            problemID = problem.get('id')
            problemText = problem.get('problem')

            # divide operator values and problem values
            
            match = re.search(r'(\d+)\s*([+*/-])\s*(\d+)', problemText)
            
            if match:
                operand1 = float(match.group(1))
                operator = match.group(2)
                operand2 = float(match.group(3))

                # basic conditional to compute result based on operator type
                if operator == '+':
                    result = operand1 + operand2
                elif operator == '-':
                    result = operand1 - operand2
                elif operator == '*':
                    result = operand1 * operand2
                elif operator == '/':
                    result = operand1 / operand2

                # output problemid and result
                print(f"Problem {problemID}: {problemText} = {result}")
            