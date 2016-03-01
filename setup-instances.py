from libs import gce_client
import sys


def main():
    ACTION = sys.argv[1]
    PROJECT = sys.argv[2]
    ZONE = sys.argv[3]

    GCE = gce_client.ComputeEngineClient(PROJECT, ZONE)

    test_script = "#!/bin/bash mkdir TEST-DIR"

    if ACTION == "create_instance_template":
        it = GCE.create_instance_template(
            "opencv-worker",
            "debian-jessie-opencv",
            "520053389007-compute@developer.gserviceaccount.com",
            sScript_url=test_script)

        print "Instance creation response: %s" % it

    elif ACTION == "create_instance_group":
        mg = GCE.create_managed_instance_group(
            "opencv-worker",
            "opencv-managed-group",
            "https://www.googleapis.com/compute/v1/projects/test-opencv/global/instanceTemplates/opencv-worker")

        print "Managed Group creation response: %s" % mg

    elif ACTION == "create_cpu_autoscaler":
        ae = GCE.create_cpu_autoscaler(
            "opencv-managed-group",
            "https://www.googleapis.com/compute/v1/projects/test-opencv/zones/" + ZONE + "/instanceGroupManagers/opencv-managed-group",
            10,
            0.8,
            60)

        print "Autoscaler creation response: %s" % ae

if __name__ == '__main__':
    main()
