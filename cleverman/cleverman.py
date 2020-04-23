from flask import Flask
from cleverman.config import Config
from cleverman.devices.paloalto.device import Device 
import os

app = Flask(__name__)

## Global settings
## TODO: refactor

cleverman_config = Config.getConfig()

# Get port from Config Object
if os.getenv("VCAP_APP_PORT") > 1024:
   cfPort = int(os.getenv("VCAP_APP_PORT"))
else:
   cfPort = 8080


@app.route('/')
def index():
    return "Hello from Cleverman"


@app.route('/v1/vrf')
def return_all_vrf():
    return mock.all_vrf()


@app.route('/v1/devices')
def return_devices_infos():
    return mock.devices_infos()


@app.route('/v1/device/{name:str}')
def return_devices_infos(name):
    return mock.devices_infos(name)


@app.route('/v1/admin/infos')
def return_all_vrf():
    return mock.get_vrf()




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=dynPort)