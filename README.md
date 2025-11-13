
# **AWS Cloud Cost Optimization – Automated EBS Snapshot Cleanup**

This project implements an automated solution to reduce AWS storage expenses by identifying and deleting stale EBS snapshots. A scheduled Lambda function evaluates all snapshots in the account, checks their association with active volumes, and removes those that are no longer in use. This ensures efficient storage utilization and minimizes unnecessary costs.

---

## **Features**

* Automatically scans all EBS snapshots owned by the account
* Compares snapshots with active EC2 volumes
* Removes snapshots that are not linked to any active resources
* Uses a CloudWatch schedule to run the cleanup periodically
* Follows least-privilege permissions for safe operation

---

## **Files Included**

* `lambda_function.py` – Lambda function implementation
* `requirements.txt` – Dependencies list
* `iam_policy.json` – Required IAM policy for snapshot operations
* `cloudwatch_rule.json` – CloudWatch scheduling configuration
* `sample_output.json` – Example output after cleanup
* `SETUP.md` – Steps for deployment and configuration
* `.gitignore` – Ignore rules for repository
* `architecture.txt` – Workflow description

---

## **Architecture**

```
CloudWatch Scheduler → AWS Lambda → EC2 Snapshot API → Delete Stale Snapshots
```

---

## **Deployment Steps**

1. Create an IAM role for Lambda using the permissions supplied in `iam_policy.json`.
2. Set up a Lambda function using Python and assign the created IAM role.
3. Upload the code from `lambda_function.py`.
4. Configure a CloudWatch rule (using `cloudwatch_rule.json`) to schedule the function.
5. Test the function manually and verify the output in CloudWatch Logs.

---

## **Example Output**

```
{
  "deleted_snapshots": [
    "snap-0a12b34c56d78e900"
  ],
  "message": "Stale snapshots removed successfully."
}
```

---

## **Author**

**Karthik C**
Cloud and DevOps Enthusiast


If you want, I can also generate a **ZIP file** for this version or help you make a **GitHub-ready structure**.
