from flask import Flask
from config import Config
from devices.paloalto.device import Device 
import os
import connexion

app = connexion.App(__name__, specification_dir='./configuration')
app.add_api('swagger.yml')

## Global settings
## TODO: refactor

cleverman_config = Config.getConfig()

# Get port from Config Object
if os.getenv("PORT") is not None:
   dyn_port = int(os.getenv("PORT"))
else:
   dyn_port = 8080


@app.route('/')
def index():
    """
    Main access
    """
    return "Hello from Cleverman"


@app.route('/v1/vrf')
def return_all_vrf():
    return mock.all_vrf()


@app.route('/v1/devices')
def return_devices_infos():
    return mock.devices_infos()


@app.route('/v1/device/{name:str}')
def return_device_infos(name):
    return mock.devices_infos(name)


if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.56.140', port=dyn_port)