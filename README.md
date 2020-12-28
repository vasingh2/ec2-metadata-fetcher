# AWS EC2 Metadata Fetcher
AWS EC2 metadata fetcher is to get the AWS EC2 metadata in the json format.

### Requirement
1. Python Version Installed > 3.5
2. Pip Installed for Python3.

### Install Dependencies
Install the dependecies using pip.

```python
pip3 install -r requirements.txt
```

### Usage

By default aws ec2 metadata fetcher will display output the complete metadata as JSON object.
```python
python3 awsMetadata.py
```

To retrieve the specific values for the datakey pass the options/arguments.

##### Options
```
usage: awsMetadata.py [-h] [-a] [-al] [-am] [-b] [-e] [-hi] [-ho] [-ic] [-im] [-ia] [-i] [-il] [-it] [-lh] [-li] [-m] [-me] [-n]
                      [-pl] [-p] [-ph] [-pi] [-pk] [-r] [-sg] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -a, --ami-id          AMI ID
  -al, --ami-launch-index
                        AMI Launch Index
  -am, --ami-manifest-path
                        AMI Manifest Path
  -b, --block-device-mapping
                        Block Device Mapping
  -e, --events          Events
  -hi, --hibernation    Hibernation
  -ho, --hostname       Hostname
  -ic, --identity-credentials
                        Identity Credentials
  -im, --iam            IAM
  -ia, --instance-action
                        Instance Action
  -i, --instance-id     Instance ID
  -il, --instance-life-cycle
                        Instance Life Cycle
  -it, --instance-type  Instance Type
  -lh, --local-hostname
                        Local Hostname
  -li, --local-ipv4     Local IPV4
  -m, --mac             Mac
  -me, --metrics        Metrics
  -n, --network         Network
  -pl, --placement      Placement
  -p, --profile         Profile
  -ph, --public-hostname
                        Public Hostname
  -pi, --public-ipv4    Public IPV4
  -pk, --public-keys    Public Keys
  -r, --reservation-id  Reservation ID
  -sg, --security-groups
                        Security Groups
  -s, --services        Services
```