from dataclasses import dataclass
import os
import yaml
import daiquiri


config_path = "configuration/application.yaml"

daiquiri.setup()
config_logger = daiquiri.getLogger("cleverman")

@dataclass
class Config(object):
    '''Configuration FActory'''

    _app_instance_name: str = None
    _app_socker_port: int = None


    def __init__(self):
        self._import_static_config()

    @classmethod
    def getConfig(cls) -> map:
        dict_cfg: dict = {}

        dict_cfg['name'] = cls._app_instance_name
        dict_cfg['port'] = cls._app_socker_port
        
        return dict_cfg 


    def _import_dyn_config(self) -> dict():
        config_logger.debug("_import_dyn_config:os.environ", os.environ)
        ## Constuire le dict içi
        self._app_instance_name = os.getenv("VCAP_APPLICATION")
        self._app_socker_port = os.getenv("PORT")


    @classmethod
    def _import_static_config(cls) -> dict():

        try:
            with open(r''+config_path, 'r') as file:
                config_map = yaml.load(file, Loader=yaml.FullLoader)
                return config_map
        except Exception as ex:
            config_logger.error("Erreur de chargement de la configuration :",
            config_path=config_path, exception=ex)
            return dict()


    def _import_config(self) -> None:
        
        stage = os.getenv("STAGE")

        if stage in "PROD":
            self._import_dyn_config()

        config_map = self._import_static_config()

        self._app_instance_name = config_map['appconfig']['instance_name']
        self._app_socker_port = config_map['appconfig']['port']


if __name__ == '__main__':
    test_config = Config()
    print(test_config.getConfig())