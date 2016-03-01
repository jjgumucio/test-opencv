from libs import gcs_client, gds_client, tq_client
import time


GCS = gcs_client.CloudStorageClient()
GDS = gds_client.DatastoreClient()

print "== [START] == TASK GETTER SCRIPT [START] =="
TQ = tq_client.TaskqueueClient("test-opencv", "image-processing-queue")
# GCS = gcs_client.CloudStorageClient()

TQ.create_task("Hello World")

time.sleep(10)

task = TQ.lease_task(1, 20)

TQ.delete_task(task["items"][0]["id"])

print "== [END] == TASK GETTER SCRIPT [END] =="

# Create file for testing
print "== [START] GCS TEST =="
f = open("test-file.txt", "wb")
f.write("Hello Cloud Storage Reference")
f.close()

# Upload file to opencv-worker bucket
GCS.upload_media("opencv-worker", "test-file.txt", "test-file.txt")
print "== [END] GCS TEST =="

print "== [START] DATASTORE TEST =="
# Test reference saving
transactionId = GDS.beginTransaction("test-opencv")["transaction"]

insertion = {
    "insertAutoId": [
        {
            "properties": {
                "file_path": {
                    "stringValue": "opencv-worker/test-file.txt"
                }
            },
            "key": {
                "path": [
                    {
                        "kind": "FileReference"
                    }
                ]
            }
        },
    ]
}

GDS.commit("test-opencv", transactionId, insertion)

print "== [END] DATASTORE TEST =="
