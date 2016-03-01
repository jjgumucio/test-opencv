from libs import gcs_client, tq_client
import time

print "== [START] == TASK GETTER SCRIPT [START] =="
TQ = tq_client.TaskqueueClient("test-opencv", "image-processing-queue")
# GCS = gcs_client.CloudStorageClient()

TQ.create_task("Hello World")

time.sleep(10)

task = TQ.lease_task(1, 20)

TQ.delete_task(task["items"][0]["id"])

print "== [END] == TASK GETTER SCRIPT [END] =="
