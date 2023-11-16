import os
import re
from collections import defaultdict
import time
import json
from flask import Flask, render_template
from list import *

directory_path = r'C:\Users\madsb\Downloads\mails\mail'

app = Flask(__name__)

# Check if directory exists
if os.path.exists(directory_path) and os.path.isdir(directory_path):

    directory_path = r'C:\Users\madsb\Downloads\mails\mail'
    file_name = ''
    output_file_path = 'main_folder/output.json'
    Backup_File = f"backups\output-{random.randint(1, 600)}.json"
    if os.path.dirname("backups"):
        os.mkdir("backups")

    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        country_groups = defaultdict(dict)

        ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        access_pattern = r'ACCESS (BLOCK|FORWARD)'
        for f in os.listdir(directory_path):
            file_path = os.path.join(directory_path, f)

            if os.path.exists(file_path) and os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    lines = content.split('\n')

                    current_country = None
                    blocked = False
                    for line in lines:
                        print(line)
                        
                        # Check ip pattern
                        access_match = re.search(access_pattern, line)
                        if access_match:
                            access_status = access_match.group(1)
                            if access_status == 'BLOCK':
                                blocked = True
                            else:
                                blocked = False

                        # Check IP address
                        match = re.search(ip_pattern, line)
                        if match:
                            ip_address = match.group()

                            # Get country
                            time.sleep(.6)
                            response = ip(ip_address)
                            if response:
                                country = response["country"] if response["country"] else "Unknown"
                                if current_country != country:
                                    current_country = country


                                if country == 'ZZ':
                                    country = "Unknown"
                                if ip_address not in country_groups[country]:
                                    country_groups[country][ip_address] = {
                                        'continent': response["continent"],
                                        'country': response["country"],
                                        'city': response["city"],
                                        'zipcode': response["zipcode"],
                                        'timezone': response["timezone"],
                                        'isp': response["isp"],
                                        'organisation': response["organisation"],
                                        'proxy': response["proxy"],
                                        'hosting': response["hosting"],
                                        "Blocked" : blocked
                                        }

                        # Save Data to file
                        writefile(output_file_path, country_groups)

                print(f"Data saved to {output_file_path}")
                print(f"Backup Data saved to {Backup_File}")
                response2 = readfile(output_file_path)
                writefile(Backup_File, response2)

                @app.route('/')
                @app.route('/index')
                def index():
                    with open(output_file_path) as f:
                        data = json.load(f)
                    return render_template('index.html', d=data)

                if __name__ == '__main__':
                    app.run(debug=True)

            else:
                print(f"The file '{file_name}' does not exist in the specified directory.")

else:
    print(f"The directory '{directory_path}' does not exist.")
    