from dataclasses import dataclass

def get_vsys(self) -> list:
    """
    Renvoie un ensemble de vsys
    """
    vsys_baremetal = {"vsysname": "baremetal"}
    vsys_cfy = {"vsysname": "aerofoundry"}

    return [vsys_baremetal, vsys_cfy]

@dataclass
class VirtualSystem(object):

    name: str = None
    id: int = None
    adresses: dict = None
    snat_pools: dict = None

    def get_vsys(self) -> list:
        """
        Renvoie un ensemble de vsys
        """
        vsys_baremetal = VirtualSystem("metallikaas", 6, \
            {"front": "10.100.180.0/26", "vip_1": "10.101.48.0/28"}, \
            {"front" : "80.80.80.0/29", "vip_1": "90.90.90.0/29"} )

        vsys_cfy = VirtualSystem("aerofoundry", 2, \
            {"front": "10.100.180.0/26", "vip_1": "10.101.48.0/28"}, \
            {"front" : "80.80.80.0/29", "vip_1": "90.90.90.0/29"} )

        return [vsys_baremetal, vsys_cfy]