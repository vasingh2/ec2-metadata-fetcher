import boto.utils
import json
import argparse

class awsMetadata(object):
    def __init__(self,args):
        self.args = args
        self.metaData =  self.getMetadata()

    def getMetadata(self):
        awsDict = boto.utils.get_instance_metadata()
        return json.loads(json.dumps(awsDict))

    def printMetadata(self):
        isDataKeyPassed = False
        for arg in vars(self.args):
            if getattr(self.args,arg) == True:
                self.printDataKey(arg)
                isDataKeyPassed = True
        
        if isDataKeyPassed == False:
            self.printDataKey()

    def printDataKey(self, dataKey=None):
        if dataKey:
            keyFound = False
            for key in self.metaData:
                if key == dataKey.replace("_","-"):
                    print("{" + "'{}':'{}'".format(key,self.metaData[key]) + "}")
                    keyFound = True
            if not keyFound:
                print ("WARN: DataKey {} not available in AWS Metadata.".format(dataKey.replace("_","-")))
        else:
            print(json.dumps(self.metaData))

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--ami-id", action="store_true", help="AMI ID", default=False)
    parser.add_argument("-al", "--ami-launch-index", action="store_true", help="AMI Launch Index", default=False)
    parser.add_argument("-am", "--ami-manifest-path", action="store_true", help="AMI Manifest Path", default=False)
    parser.add_argument("-b", "--block-device-mapping", action="store_true", help="Block Device Mapping", default=False)
    parser.add_argument("-e", "--events", action="store_true", help="Events", default=False)
    parser.add_argument("-hi", "--hibernation", action="store_true", help="Hibernation", default=False)
    parser.add_argument("-ho", "--hostname", action="store_true", help="Hostname", default=False)
    parser.add_argument("-ic", "--identity-credentials", action="store_true", help="Identity Credentials", default=False)
    parser.add_argument("-im", "--iam", action="store_true", help="IAM", default=False)
    parser.add_argument("-ia", "--instance-action", action="store_true", help="Instance Action", default=False)
    parser.add_argument("-i", "--instance-id", action="store_true", help="Instance ID", default=False)
    parser.add_argument("-il", "--instance-life-cycle", action="store_true", help="Instance Life Cycle", default=False)
    parser.add_argument("-it", "--instance-type", action="store_true", help="Instance Type", default=False)
    parser.add_argument("-lh", "--local-hostname", action="store_true", help="Local Hostname", default=False)
    parser.add_argument("-li", "--local-ipv4", action="store_true", help="Local IPV4", default=False)
    parser.add_argument("-m", "--mac", action="store_true", help="Mac", default=False)
    parser.add_argument("-me", "--metrics", action="store_true", help="Metrics", default=False)
    parser.add_argument("-n", "--network", action="store_true", help="Network", default=False)
    parser.add_argument("-pl", "--placement", action="store_true", help="Placement", default=False)
    parser.add_argument("-p", "--profile", action="store_true", help="Profile", default=False)
    parser.add_argument("-ph", "--public-hostname", action="store_true", help="Public Hostname", default=False)
    parser.add_argument("-pi", "--public-ipv4", action="store_true", help="Public IPV4", default=False)
    parser.add_argument("-pk", "--public-keys", action="store_true", help="Public Keys", default=False)
    parser.add_argument("-r", "--reservation-id", action="store_true", help="Reservation ID", default=False)
    parser.add_argument("-sg", "--security-groups", action="store_true", help="Security Groups", default=False)
    parser.add_argument("-s", "--services", action="store_true", help="Services", default=False)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    awsMetadataFetcher = awsMetadata(args)
    awsMetadataFetcher.printMetadata()