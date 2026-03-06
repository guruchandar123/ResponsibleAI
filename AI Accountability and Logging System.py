import json
import datetime
import hashlib

class RAIAccountabilityTracker:
    def __init__(self, model_name, owner_name):
        self.model_metadata = {
            "model_name": model_name,
            "accountable_owner": owner_name,
            "deployment_date": str(datetime.datetime.now()),
            "logs": []
        }

    def log_audit(self, action, status, details):
        entry = {
            "timestamp": str(datetime.datetime.now()),
            "action": action,
            "status": status,
            "details": details,
            "entry_hash": self._generate_hash(action, details)
        }
        self.model_metadata["logs"].append(entry)
        
    def _generate_hash(self, action, details):
        content = f"{action}{details}{datetime.datetime.now()}"
        return hashlib.sha256(content.encode()).hexdigest()

    def export_audit_trail(self, filename="audit_log.json"):
        with open(filename, 'w') as f:
            json.dump(self.model_metadata, f, indent=4)
        print(f"Audit trail exported to {filename}")

# Usage
tracker = RAIAccountabilityTracker("Credit_Scoring_v1", "Data_Science_Dept_Head")
tracker.log_audit("Model Calibration", "Success", "Adjusted threshold for fairness")
tracker.log_audit("Robustness Test", "Passed", "Model resilient to noise at 5% epsilon")
tracker.export_audit_trail()
