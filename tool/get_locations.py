from context import config
from context import network_utils
from context import storage
import flags

firebase_storage = storage.firebase_storage
location = storage.location

FLAGS = flags.FLAGS

flags.DEFINE_string('firebaseio_url', None, 'Set the firebase url.')
flags.DEFINE_string('firebaseio_base_path', None, 'Set the firebase base path.')
flags.DEFINE_string('firebaseio_service_account_json', None,
                    'Set the file path to the firebase service account key json file.')

c = config.Config()
if FLAGS.firebaseio_url:
  c.firebaseio_url = FLAGS.firebaseio_url
if FLAGS.firebaseio_base_path:
  c.firebaseio_base_path = FLAGS.firebaseio_base_path
if FLAGS.firebaseio_service_account_json:
  c.firebaseio_service_account_json = FLAGS.firebaseio_service_account_json

fbs = firebase_storage.FirebaseStorage(c)

# Get locations.
print 'firebase get locations:'
locations = fbs.GetLocations()
for my_location in locations:
  print my_location.ToString()