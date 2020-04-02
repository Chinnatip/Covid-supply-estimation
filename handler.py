import json
import pandas as pd


def supply_estimation(event, context):
    # POST-web receiver
    load_data = json.loads(event['body'])

    # Destructuring POST data
    population, case_mild, case_severe, case_critical, doubling_time, hospital_name, hospital_region, contact_email, writing_date = [load_data[k]
                                                                                                                                     for k in ("population", "case_mild", "case_severe", "case_critical", "doubling_time", "hospital_name", "hospital_region", "contact_email", "writing_date")]

    # calculate total cases
    total_case = case_mild + case_severe + case_critical

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
