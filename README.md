## Alternative Location Tool in Python

The alternative location is to help locate a computer based with the external ip address, the
internal ip addresses assigned along with the mac address associated with it. The alternative
location tool takes the ip address information and saves it to Firebase.

## Getting Started

```
virtual env
source venv/bin/activate
pip install -r requirements.txt
```

## Firebase setup

Create a new Firebase project and go to the console.

From the Firebase Console, click 'Database' in the left menu bar. Then in the realtime database,
click on the 'rules' tab. Next set the authentication for read and write to be not null. This will
allow only authenticated reads and writes from the database.

```
{
  "rules": {
    ".read": "auth != null",
    ".write": "auth != null"
  }
}
```

After publishing the realtime database rules, we'll next need a service account key json file.
This is found in the 'Project Settings'. From there, navigate to the 'Service Account' tab and
click the 'Generate New Private Key' button. This will download the service account key json file.

## Running the tools

There are several tools that help manage locations:

* Getting the location - `python tool/get_locations.py`
* Removing a location - `python tool/remove_location.py`
* Updating a location - `python tool/update_location.py`

These could be executed with either by passing the vars by flags or by environment variables.

**Using flags**

To get a full list of flags, in each tool type:

```
python tool/get_locations.py --help

usage: get_locations.py [-h] [--firebaseio_url FIREBASEIO_URL]
                        [--firebaseio_base_path FIREBASEIO_BASE_PATH]
                        [--firebaseio_service_account_json FIREBASEIO_SERVICE_ACCOUNT_JSON]

optional arguments:
  -h, --help            show this help message and exit
  --firebaseio_url FIREBASEIO_URL
                        Set the firebase url.
  --firebaseio_base_path FIREBASEIO_BASE_PATH
                        Set the firebase base path.
  --firebaseio_service_account_json FIREBASEIO_SERVICE_ACCOUNT_JSON
                        Set the file path to the firebase service account key
                        json file.
```

**Using environment variables**

You could alternatively set these values in a bash profile or zprofile. These values are
capitalized with a prefix of 'ALT_'. So for the flag `--firebaseio_url`, the environment variable
is `ALT_FIREBASEIO_URL`.

In my zprofile, I have set my firebaseio base path to `alt`: `export ALT_FIREBASEIO_BASE_PATH=alt`.
For example if my firebaseio url is https://some-foo-bar.firebaseio.com, and my base path is set
up 'alt', then the location will be saved to
https://some-foo-bar.firebaseio.com/alt/<some_location>.