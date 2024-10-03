# Fill in this file with the code from parsing XML exercise
import xml.etree.ElementTree as ET
import re
import json
import yaml

xml = ET.parse('myfile.xml')
root = xml.getroot()

ns = re.match('{.*}', root.tag).group(0)
editconf = root.find("{}edit-config".format(ns))
defop = editconf.find("{}default-operation".format(ns))
testop = editconf.find("{}test-option".format(ns))


print("The default-operation contains: {}".format(defop.text))
print("The test-option contains: {}".format(testop.text))



with open('myfile.yaml', 'r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)

    print(ouryaml)
    print("The access token is {}".format(ouryaml['access_token']))
    print("The token expires in {} seconds.".format(ouryaml['expires_in']))
    print("\n\n")
    print(json.dumps(ouryaml, indent=4))

    yaml_file.close()

with open('myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)
    print(ourjson)

    print("The access token is: {}".format(ourjson['access_token']))
    print("The token expires in {} seconds.".format(ourjson['expires_in']))
    print("\n\n---")
    print(yaml.dump(ourjson))


    json_file.close()