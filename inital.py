import azure.functions as func
import json
import pandas as pd
from typing import List

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        document_data = req_body.get('document_data', [])

        # Process document data
        df = pd.DataFrame(document_data)
        
        # Perform calculations
        results = []
        for _index, row in df.iterrows():
            # Some complex businmess logic
            processed_value = row['value'] * 1.5 if row['type'] == 'A' else row['value'] * 0.8
            results.append({
                'id': row['id'],
                'processed_value': processed_value
            })

        # Return the processed data as JSON response
        return func.HttpResponse(
            json.dumps({"results": results}),
            mimetype="application/json",
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500
        )
