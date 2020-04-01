import json
import pandas as pd


def supply_estimation(event, context):
    # POST-web receiver
    load_data = json.loads(event['body'])

    # Destructuring POST data
    population, cases, hospital_info = [load_data[k]
                                        for k in ('population', 'cases', 'hospital_info')]
    mild, severe, critical = [cases[k]
                              for k in ('mild', 'severe', 'critical')]

    hospital_name, contact_email = [hospital_info[k]
                                    for k in ('name', 'email')]

    # calculate total cases
    total_case = mild + severe + critical

    # Prepare response
    body = {
        "population": population,
        "total_case": total_case,
        "send_report_email_to": contact_email
    }
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
